#!/usr/bin/env python3
"""
TAPI YANG Module Version Comparator

Compares YANG modules between two TAPI versions and generates reports
of backwards incompatible changes using pyang's --check-update-from feature.
"""

import argparse
import subprocess
import sys
import os
import shutil
import re
import tempfile
import difflib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from collections import defaultdict


class BreakingChange:
    """Represents a single breaking change detected by pyang."""
    
    def __init__(self, error_line: str):
        self.raw_line = error_line
        self.file = None
        self.line_number = None
        self.node_type = None
        self.node_name = None
        self.change_type = None
        self.details = None
        self.severity = 'CRITICAL'
        
        self._parse(error_line)
    
    def _parse(self, error_line: str):
        """Parse pyang error message to extract structured information."""
        # Parse location: /path/file.yang:123: error: ...
        # Also handle: /path/file.yang:123 (at /path/file.yang:456): error: ...
        location_match = re.match(r'^([^:]+):(\d+)(?:\s*\([^)]+\))?:\s*error:\s*(.+)$', error_line)
        if location_match:
            self.file = location_match.group(1)
            self.line_number = location_match.group(2)
            message = location_match.group(3)
        else:
            message = error_line
        
        # Parse node type and name: "the container 'name' ... is illegally removed"
        node_match = re.search(r'the (container|list|leaf|leaf-list|choice|case|grouping|typedef|identity|rpc|notification) [\'"]([^\'"]+)[\'"]', message)
        if node_match:
            self.node_type = node_match.group(1)
            self.node_name = node_match.group(2)
        
        # Parse "path for X" pattern (config/state mismatch errors)
        if not self.node_name:
            path_match = re.search(r'the path for ([^\s]+)', message)
            if path_match:
                self.node_name = path_match.group(1)
                self.node_type = 'leafref'
        
        # Determine change type
        if 'illegally removed' in message:
            self.change_type = 'REMOVED'
        elif 'illegally changed' in message or 'has changed' in message:
            self.change_type = 'CHANGED'
            # Extract old and new values for type changes
            type_change = re.search(r'changed from (\S+) to (\S+)', message)
            if type_change:
                self.details = f"Type changed: {type_change.group(1)} → {type_change.group(2)}"
        elif 'now mandatory' in message or 'is now mandatory' in message:
            self.change_type = 'MANDATORY_ADDED'
        elif 'illegally added' in message:
            self.change_type = 'ADDED'
            self.severity = 'WARNING'
        elif 'is config but refers to a non-config' in message:
            self.change_type = 'CONFIG_STATE_MISMATCH'
            self.severity = 'WARNING'
        elif 'new revision' in message and 'is not newer than old revision' in message:
            self.change_type = 'REVISION_ORDER'
            self.severity = 'INFO'
        else:
            self.change_type = 'OTHER'
        
        if not self.details:
            self.details = message
    
    def get_file_context(self, context_lines: int = 3) -> str:
        """Extract context lines around the error location from the file."""
        if not self.file or not self.line_number:
            return None
        
        # For REMOVED items, try to extract from the "defined at" location in source
        # Prefer the second location (at ...) if it exists, as it shows the actual definition
        # when items are used via groupings
        source_location = None
        if self.change_type == 'REMOVED' and self.details:
            # Try to find "(at file:line)" first - this is the actual definition
            match = re.search(r'\(at ([^:]+):(\d+)\)', self.details)
            if not match:
                # Fall back to "defined at file:line"
                match = re.search(r'defined at ([^:]+):(\d+)', self.details)
            if match:
                source_location = (match.group(1), int(match.group(2)))
        
        # Use source location if available, otherwise use the error location
        if source_location:
            file_path, line_num = source_location
            file_label = "Source"
        else:
            file_path = self.file
            line_num = int(self.line_number)
            file_label = "Target"
        
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                return None
            
            with open(file_path, 'r', encoding='utf-8') as f:
                all_lines = f.readlines()
            
            start = max(0, line_num - context_lines - 1)
            end = min(len(all_lines), line_num + context_lines)
            
            context = []
            for i in range(start, end):
                prefix = ">>>" if i == line_num - 1 else "   "
                context.append(f"{prefix} {i+1:4d} | {all_lines[i].rstrip()}")
            
            # Add file label
            header = f"[{file_label}: {Path(file_path).name}]"
            return header + '\n' + '\n'.join(context)
        except Exception:
            return None
    
    def to_markdown(self, include_context: bool = True) -> str:
        """Convert to markdown format."""
        lines = []
        lines.append(f"**{self.node_type.title() if self.node_type else 'Node'} {self.change_type}**")
        if self.node_name:
            lines.append(f"- **Node:** `{self.node_name}`")
        if self.line_number:
            lines.append(f"- **Location:** Line {self.line_number}")
        if self.details:
            lines.append(f"- **Details:** {self.details}")
        
        # Add file context
        if include_context:
            context = self.get_file_context()
            if context:
                lines.append("")
                lines.append("**Context:**")
                lines.append("```yang")
                lines.append(context)
                lines.append("```")
        
        return '\n'.join(lines)


class TAPIVersionComparator:
    """Main class for comparing TAPI YANG module versions."""
    
    def __init__(self, repo_url: str, source_version: str, target_version: str, output_dir: Path):
        self.repo_url = repo_url
        self.source_version = source_version
        self.target_version = target_version
        self.output_dir = Path(output_dir)
        self.temp_repo = None
        self.source_yang_dir = None
        self.target_yang_dir = None
        self.results = {}
        
    def run(self):
        """Main execution method."""
        # Quick dependency check before starting
        if not shutil.which('pyang'):
            print("\n" + "="*70)
            print("ERROR: pyang not found")
            print("="*70)
            print("\npyang is required to compare YANG modules.")
            print("\nTo install pyang, choose one of:")
            print("  • pipx install pyang           (recommended)")
            print("  • pip install --user pyang")
            print("  • pip install pyang            (in virtual environment)")
            print("\nFor more details, run:")
            print("  python3 compare_tapi_versions.py --verify-deps")
            print("="*70 + "\n")
            sys.exit(1)
        
        print(f"\n{'='*70}")
        print(f"TAPI Version Comparator")
        print(f"{'='*70}")
        print(f"Repository: {self.repo_url}")
        print(f"Source Version: {self.source_version}")
        print(f"Target Version: {self.target_version}")
        print(f"Output Directory: {self.output_dir}")
        print(f"{'='*70}\n")
        
        try:
            # Create output directories
            self._setup_output_dirs()
            
            # Clone repository and extract modules
            print("Step 1: Cloning repository and extracting YANG modules...")
            self._clone_and_extract_modules()
            
            # Discover modules to compare
            print("\nStep 2: Discovering modules...")
            common_modules, new_modules, removed_modules = self._discover_modules()
            
            print(f"  - Common modules: {len(common_modules)}")
            print(f"  - New modules: {len(new_modules)}")
            print(f"  - Removed modules: {len(removed_modules)}")
            
            # Compare each module
            print(f"\nStep 3: Comparing {len(common_modules)} modules...")
            for i, module in enumerate(sorted(common_modules), 1):
                print(f"  [{i}/{len(common_modules)}] Comparing {module}...")
                self.results[module] = self._compare_module(module)
            
            # Generate diffs
            print("\nStep 4: Generating plain diffs...")
            self._generate_diffs(common_modules)
            
            # Generate reports
            print("\nStep 5: Generating reports...")
            self._generate_reports(common_modules, new_modules, removed_modules)
            
            print(f"\n{'='*70}")
            print("Comparison complete!")
            print(f"{'='*70}")
            print(f"\nResults saved to: {self.output_dir}")
            print(f"  - Master report: {self.output_dir / 'comparison-report.md'}")
            print(f"  - Analysis: {self.output_dir / 'analysis' / 'summary.md'}")
            print(f"  - Diffs: {self.output_dir / 'diff' / '*.diff'}")
            print(f"  - Raw pyang output: {self.output_dir / 'raw' / '*.pyang.txt'}")
            print()
            
        except Exception as e:
            print(f"\nError: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            sys.exit(1)
        finally:
            # Clean up temporary repository
            if self.temp_repo and self.temp_repo.exists():
                print("Cleaning up temporary files...")
                shutil.rmtree(self.temp_repo)
                print(f"Removed temporary repository: {self.temp_repo}")
    
    def _setup_output_dirs(self):
        """Create output directory structure."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        (self.output_dir / 'source' / 'YANG').mkdir(parents=True, exist_ok=True)
        (self.output_dir / 'target' / 'YANG').mkdir(parents=True, exist_ok=True)
        (self.output_dir / 'analysis').mkdir(parents=True, exist_ok=True)
        (self.output_dir / 'diff').mkdir(parents=True, exist_ok=True)
        (self.output_dir / 'raw').mkdir(parents=True, exist_ok=True)
        
        self.source_yang_dir = self.output_dir / 'source' / 'YANG'
        self.target_yang_dir = self.output_dir / 'target' / 'YANG'
    
    def _clone_and_extract_modules(self):
        """Clone repository and extract YANG modules for both versions."""
        # Create temporary directory for repo
        self.temp_repo = Path(tempfile.mkdtemp(prefix='tapi_repo_'))
        
        try:
            # Clone repository
            print(f"  Cloning {self.repo_url}...")
            subprocess.run(
                ['git', 'clone', '--quiet', self.repo_url, str(self.temp_repo)],
                check=True,
                capture_output=True
            )
            
            # Extract source version modules
            print(f"  Extracting {self.source_version} modules...")
            self._extract_yang_modules(self.source_version, self.source_yang_dir)
            
            # Extract target version modules
            print(f"  Extracting {self.target_version} modules...")
            self._extract_yang_modules(self.target_version, self.target_yang_dir)
            
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Git operation failed: {e.stderr.decode() if e.stderr else str(e)}")
    
    def _extract_yang_modules(self, version: str, output_dir: Path):
        """Extract all YANG modules from a specific git tag."""
        # Get list of YANG files at this version
        result = subprocess.run(
            ['git', 'ls-tree', '-r', '--name-only', version, 'YANG/'],
            cwd=self.temp_repo,
            capture_output=True,
            text=True,
            check=True
        )
        
        yang_files = [f for f in result.stdout.strip().split('\n') if f.endswith('.yang')]
        
        # Extract each file
        for yang_file in yang_files:
            module_name = Path(yang_file).name
            result = subprocess.run(
                ['git', 'show', f'{version}:{yang_file}'],
                cwd=self.temp_repo,
                capture_output=True,
                text=True,
                check=True
            )
            
            output_file = output_dir / module_name
            output_file.write_text(result.stdout)
    
    def _discover_modules(self) -> Tuple[List[str], List[str], List[str]]:
        """Discover modules in source and target versions."""
        source_modules = set(f.name for f in self.source_yang_dir.glob('*.yang'))
        target_modules = set(f.name for f in self.target_yang_dir.glob('*.yang'))
        
        common_modules = sorted(source_modules & target_modules)
        new_modules = sorted(target_modules - source_modules)
        removed_modules = sorted(source_modules - target_modules)
        
        return common_modules, new_modules, removed_modules
    
    def _compare_module(self, module_name: str) -> Dict:
        """Compare a single module using pyang."""
        source_file = self.source_yang_dir / module_name
        target_file = self.target_yang_dir / module_name
        
        cmd = [
            'pyang',
            '--check-update-from', str(source_file),
            str(target_file),
            '-P', str(self.source_yang_dir),
            '-p', str(self.target_yang_dir),
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Save raw pyang output
        raw_dir = self.output_dir / 'raw'
        raw_file = raw_dir / f"{module_name}.pyang.txt"
        raw_file.write_text(result.stderr if result.stderr else "No errors detected\n")
        
        # Parse errors
        all_changes = []
        if result.stderr:
            for line in result.stderr.strip().split('\n'):
                if line and 'error:' in line:
                    all_changes.append(BreakingChange(line))
        
        # Filter out non-critical errors (but keep them in raw output)
        ignored_types = {'REVISION_ORDER', 'CONFIG_STATE_MISMATCH'}
        breaking_changes = [c for c in all_changes if c.change_type not in ignored_types]
        
        # Categorize changes
        categorized = defaultdict(list)
        for change in breaking_changes:
            categorized[change.change_type].append(change)
        
        return {
            'breaking_changes': breaking_changes,
            'categorized': dict(categorized),
            'total_count': len(breaking_changes),
            'raw_output': result.stderr
        }
    
    def _generate_diffs(self, modules: List[str]):
        """Generate plain text diffs for each module."""
        diff_dir = self.output_dir / 'diff'
        
        for module in modules:
            source_file = self.source_yang_dir / module
            target_file = self.target_yang_dir / module
            
            # Read both files
            with open(source_file, 'r', encoding='utf-8') as f:
                source_lines = f.readlines()
            with open(target_file, 'r', encoding='utf-8') as f:
                target_lines = f.readlines()
            
            # Generate unified diff using Python's difflib
            diff_lines = difflib.unified_diff(
                source_lines,
                target_lines,
                fromfile=f'a/{module}',
                tofile=f'b/{module}',
                lineterm=''
            )
            
            diff_file = diff_dir / f"{module}.diff"
            diff_file.write_text('\n'.join(diff_lines) + '\n' if diff_lines else '')
    
    def _generate_reports(self, common_modules: List[str], new_modules: List[str], removed_modules: List[str]):
        """Generate all markdown reports."""
        analysis_dir = self.output_dir / 'analysis'
        
        # Generate per-module reports
        for module in common_modules:
            if self.results[module]['total_count'] > 0:
                self._generate_module_report(module, analysis_dir)
        
        # Generate summary report
        self._generate_summary_report(common_modules, new_modules, removed_modules, analysis_dir)
        
        # Generate master report
        self._generate_master_report(common_modules, new_modules, removed_modules)
    
    def _generate_module_report(self, module_name: str, analysis_dir: Path):
        """Generate report for a single module."""
        result = self.results[module_name]
        report_file = analysis_dir / f"{module_name}.md"
        
        lines = []
        lines.append(f"# Module: {module_name}")
        lines.append("")
        lines.append(f"## Comparison: {self.source_version} → {self.target_version}")
        lines.append("")
        
        if result['total_count'] == 0:
            lines.append("✅ **No breaking changes detected**")
        else:
            lines.append(f"### ❌ Breaking Changes ({result['total_count']} found)")
            lines.append("")
            
            # Group by change type - show in priority order, then others
            priority_types = ['REMOVED', 'CHANGED', 'MANDATORY_ADDED']
            other_types = [ct for ct in result['categorized'].keys() if ct not in priority_types]
            
            for change_type in priority_types + sorted(other_types):
                changes = result['categorized'].get(change_type, [])
                if changes:
                    lines.append(f"#### {change_type.replace('_', ' ').title()} ({len(changes)})")
                    lines.append("")
                    for change in changes:
                        lines.append(change.to_markdown())
                        lines.append("")
            
            # Summary
            lines.append("### Summary")
            lines.append("")
            for change_type, changes in result['categorized'].items():
                lines.append(f"- **{change_type.replace('_', ' ').title()}:** {len(changes)}")
        
        report_file.write_text('\n'.join(lines))
    
    def _generate_summary_report(self, common_modules: List[str], new_modules: List[str], 
                                 removed_modules: List[str], analysis_dir: Path):
        """Generate summary report across all modules."""
        summary_file = analysis_dir / 'summary.md'
        
        lines = []
        lines.append(f"# TAPI Version Comparison Summary")
        lines.append("")
        lines.append(f"**Source Version:** {self.source_version}")
        lines.append(f"**Target Version:** {self.target_version}")
        lines.append("")
        
        # Overall statistics
        total_breaking = sum(r['total_count'] for r in self.results.values())
        modules_with_breaking = sum(1 for r in self.results.values() if r['total_count'] > 0)
        
        lines.append("## Overview")
        lines.append("")
        lines.append(f"- **Total Modules Compared:** {len(common_modules)}")
        lines.append(f"- **Modules with Breaking Changes:** {modules_with_breaking}")
        lines.append(f"- **Total Breaking Changes:** {total_breaking}")
        lines.append(f"- **New Modules:** {len(new_modules)}")
        lines.append(f"- **Removed Modules:** {len(removed_modules)}")
        lines.append("")
        
        # Module-by-module summary
        lines.append("## Module Summary")
        lines.append("")
        lines.append("| Module | Breaking Changes | Status |")
        lines.append("|--------|------------------|--------|")
        
        for module in sorted(common_modules):
            count = self.results[module]['total_count']
            status = "❌" if count > 0 else "✅"
            lines.append(f"| {module} | {count} | {status} |")
        
        if new_modules:
            lines.append("")
            lines.append("## New Modules")
            lines.append("")
            for module in new_modules:
                lines.append(f"- {module}")
        
        if removed_modules:
            lines.append("")
            lines.append("## Removed Modules")
            lines.append("")
            for module in removed_modules:
                lines.append(f"- {module}")
        
        summary_file.write_text('\n'.join(lines))
    
    def _generate_master_report(self, common_modules: List[str], new_modules: List[str], 
                               removed_modules: List[str]):
        """Generate master comparison report."""
        report_file = self.output_dir / 'comparison-report.md'
        
        lines = []
        lines.append(f"# TAPI YANG Module Comparison Report")
        lines.append("")
        lines.append(f"## Version Comparison: {self.source_version} → {self.target_version}")
        lines.append("")
        lines.append(f"**Repository:** {self.repo_url}")
        lines.append(f"**Generated:** {datetime.now().strftime('%a %b %d %H:%M:%S %Z %Y')}")
        lines.append("")
        
        # Executive summary
        total_breaking = sum(r['total_count'] for r in self.results.values())
        modules_with_breaking = sum(1 for r in self.results.values() if r['total_count'] > 0)
        
        lines.append("## Executive Summary")
        lines.append("")
        if total_breaking == 0:
            lines.append("✅ **No backwards incompatible changes detected between these versions.**")
        else:
            lines.append(f"⚠️ **{total_breaking} backwards incompatible changes detected across {modules_with_breaking} modules.**")
        lines.append("")
        lines.append(f"- **Modules Analyzed:** {len(common_modules)}")
        lines.append(f"- **Modules with Breaking Changes:** {modules_with_breaking}")
        lines.append(f"- **New Modules:** {len(new_modules)}")
        lines.append(f"- **Removed Modules:** {len(removed_modules)}")
        lines.append("")
        
        # Detailed findings
        lines.append("## Detailed Findings")
        lines.append("")
        lines.append("### Modules with Breaking Changes")
        lines.append("")
        
        modules_with_issues = [(m, self.results[m]['total_count']) 
                              for m in common_modules if self.results[m]['total_count'] > 0]
        modules_with_issues.sort(key=lambda x: x[1], reverse=True)
        
        if modules_with_issues:
            for module, count in modules_with_issues:
                lines.append(f"#### {module} ({count} changes)")
                lines.append("")
                lines.append(f"See detailed analysis: [`analysis/{module}.md`](analysis/{module}.md)")
                lines.append("")
                lines.append(f"Plain diff: [`diff/{module}.diff`](diff/{module}.diff)")
                lines.append("")
        else:
            lines.append("*No modules with breaking changes.*")
            lines.append("")
        
        # Links to other reports
        lines.append("## Additional Resources")
        lines.append("")
        lines.append("- [Summary Report](analysis/summary.md) - Overview statistics and module-by-module summary")
        lines.append("- [Analysis Directory](analysis/) - Detailed reports for each module with breaking changes")
        lines.append("- [Diff Directory](diff/) - Plain text diffs for all modules")
        lines.append("")
        
        report_file.write_text('\n'.join(lines))
    
    def __del__(self):
        """Cleanup temporary repository."""
        if self.temp_repo and self.temp_repo.exists():
            shutil.rmtree(self.temp_repo, ignore_errors=True)


def verify_dependencies() -> int:
    """Verify all required dependencies are installed."""
    import shutil
    
    checks = []
    
    # Check Python version
    py_version = sys.version_info
    py_ok = py_version >= (3, 8)
    checks.append(('Python', f'{py_version.major}.{py_version.minor}.{py_version.micro}', 
                   '>= 3.8', py_ok))
    
    # Check git
    git_path = shutil.which('git')
    if git_path:
        git_version = subprocess.run(['git', '--version'], capture_output=True, text=True)
        checks.append(('Git', git_version.stdout.strip(), 'required', True))
    else:
        checks.append(('Git', 'NOT FOUND', 'required', False))
    
    # Check pyang
    pyang_path = shutil.which('pyang')
    if pyang_path:
        pyang_version = subprocess.run(['pyang', '--version'], capture_output=True, text=True)
        version_str = pyang_version.stdout.strip()
        # Parse version (e.g., "pyang 2.7.1")
        version_match = re.search(r'(\d+)\.(\d+)', version_str)
        if version_match:
            major, minor = int(version_match.group(1)), int(version_match.group(2))
            pyang_ok = (major, minor) >= (2, 6)
        else:
            pyang_ok = False
        checks.append(('pyang', version_str, '>= 2.6.0', pyang_ok))
    else:
        checks.append(('pyang', 'NOT FOUND', '>= 2.6.0', False))
    
    # Check GitPython
    try:
        import git
        checks.append(('GitPython', git.__version__, 'required', True))
    except ImportError:
        checks.append(('GitPython', 'NOT INSTALLED', 'required', False))
    
    # Print results
    print("\nDependency Check:\n")
    all_ok = True
    for name, version, requirement, ok in checks:
        status = '✓' if ok else '✗'
        print(f"{status} {name}: {version} ({requirement})")
        all_ok = all_ok and ok
    
    print()
    if all_ok:
        print("All dependencies satisfied!")
        return 0
    else:
        print("Some dependencies are missing or outdated.")
        print("\n" + "="*70)
        print("INSTALLATION INSTRUCTIONS")
        print("="*70)
        
        # Check what's missing and provide specific instructions
        missing = []
        for name, version, requirement, ok in checks:
            if not ok:
                missing.append(name)
        
        if 'Git' in missing:
            print("\n📦 Git:")
            print("  Linux:   sudo apt-get install git")
            print("  macOS:   brew install git")
            print("  Windows: Download from https://git-scm.com/download/win")
        
        if 'pyang' in missing:
            print("\n📦 pyang:")
            print("  Option 1 (recommended): pipx install pyang")
            print("  Option 2:               pip install --user pyang")
            print("  Option 3 (venv):        pip install pyang")
        
        if 'GitPython' in missing:
            print("\n📦 GitPython:")
            print("  Linux:   sudo apt-get install python3-git")
            print("  macOS:   pip install GitPython")
            print("  Windows: pip install GitPython")
            print("  Or:      pip install -r requirements.txt")
        
        if 'Python' in missing:
            print("\n📦 Python 3.8+:")
            print("  Please upgrade to Python 3.8 or later")
            print("  Download from https://www.python.org/downloads/")
        
        print("\n" + "="*70)
        print("After installing, run: python3 compare_tapi_versions.py --verify-deps")
        print("="*70)
        return 1


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Compare TAPI YANG modules between two versions',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Compare v2.5.2 to v2.6.0
  %(prog)s --repo-url https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI.git \\
           --source-version v2.5.2 --target-version v2.6.0 \\
           --output-dir ./output-comparison

  # Verify dependencies
  %(prog)s --verify-deps
        """
    )
    
    parser.add_argument('--repo-url', 
                       help='TAPI git repository URL')
    parser.add_argument('--source-version',
                       help='Source version tag (e.g., v2.5.2)')
    parser.add_argument('--target-version',
                       help='Target version tag (e.g., v2.6.0)')
    parser.add_argument('--output-dir',
                       help='Output directory for results')
    parser.add_argument('--verify-deps', action='store_true',
                       help='Verify dependencies and exit')
    
    args = parser.parse_args()
    
    # Handle dependency verification
    if args.verify_deps:
        return verify_dependencies()
    
    # Validate required arguments
    if not all([args.repo_url, args.source_version, args.target_version, args.output_dir]):
        parser.error('--repo-url, --source-version, --target-version, and --output-dir are required '
                    '(unless using --verify-deps)')
    
    # Run comparison
    comparator = TAPIVersionComparator(
        repo_url=args.repo_url,
        source_version=args.source_version,
        target_version=args.target_version,
        output_dir=Path(args.output_dir)
    )
    
    comparator.run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
