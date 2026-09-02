# TAPI Version Comparator

Automated tool for comparing TAPI YANG modules between versions and detecting backwards incompatible changes.

## Features

- **Cross-platform** - works on Windows, macOS, and Linux
- **Automated comparison** using pyang's `--check-update-from` feature
- **Full dependency resolution** for accurate validation
- **Markdown reports** with categorized breaking changes and code context
- **Plain text diffs** for detailed analysis
- **No LLM required** - pure rule-based parsing

## Prerequisites

### Required

- **Python 3.8+**
- **git** command-line tool
- **pyang 2.6.0+** (for `--check-update-from` support)

### Python Packages

- GitPython >= 3.1.0

## Installation

### Quick Start

```bash
cd tapi-version-comparator

# Verify dependencies
python3 compare_tapi_versions.py --verify-deps

# If dependencies are missing, install them:
pip install -r requirements.txt

# If pyang is not installed or too old:
pip install --user pyang
# or
pipx install pyang
```

### Option 1: Using Virtual Environment (Recommended)

```bash
cd tapi-version-comparator

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate      # On Linux/macOS
# OR
.venv\Scripts\activate         # On Windows

# Install dependencies
pip install -r requirements.txt

# Verify installation
python compare_tapi_versions.py --help
```

### Option 2: User Installation

```bash
cd tapi-version-comparator

# Install dependencies for current user
pip install --user -r requirements.txt

# Verify installation
python3 compare_tapi_versions.py --help
```

## Usage

### Basic Usage

```bash
python3 compare_tapi_versions.py \
  --repo-url https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI.git \
  --source-version v2.5.2 \
  --target-version v2.6.0 \
  --output-dir ./output-comparison
```

### Verify Dependencies

```bash
python3 compare_tapi_versions.py --verify-deps
```

Expected output:
```
Dependency Check:

✓ Python: 3.12.0 (>= 3.8)
✓ Git: git version 2.43.0 (required)
✓ pyang: pyang 2.7.1 (>= 2.6.0)
✓ GitPython: 3.1.43 (required)

All dependencies satisfied!
```

### Example: Compare v2.5.2 to v2.6.0

```bash
python3 compare_tapi_versions.py \
  --repo-url https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI.git \
  --source-version v2.5.2 \
  --target-version v2.6.0 \
  --output-dir ./output-v2.5.2-to-v2.6.0
```

Or use the example script:

```bash
cd examples
./compare_v2.5.2_to_v2.6.0.sh
```

## Output Structure

```
output-dir/
├── comparison-report.md         # Master report with executive summary
├── source/                      # Source version YANG modules
│   └── YANG/
│       ├── tapi-common.yang
│       ├── tapi-photonic-media.yang
│       └── ...
├── target/                      # Target version YANG modules
│   └── YANG/
│       ├── tapi-common.yang
│       ├── tapi-photonic-media.yang
│       └── ...
├── analysis/                    # Detailed analysis reports
│   ├── summary.md              # Overall summary
│   ├── tapi-photonic-media.yang.md  # Per-module reports
│   └── ...
├── diff/                        # Plain text diffs
│   ├── tapi-photonic-media.yang.diff
│   └── ...
└── raw/                         # Raw pyang output
    ├── tapi-photonic-media.yang.pyang.txt
    └── ...
```

## Understanding the Reports

### Master Report (`comparison-report.md`)

- Executive summary of all changes
- Links to detailed module reports
- Overview statistics

### Summary Report (`analysis/summary.md`)

- Module-by-module statistics
- List of new/removed modules
- Quick reference table

### Module Reports (`analysis/<module>.md`)

- Detailed breaking changes for each module
- Categorized by change type:
  - **REMOVED**: Containers, lists, leafs that were removed
  - **CHANGED**: Type changes, cardinality changes
  - **MANDATORY_ADDED**: New mandatory fields
  - **OTHER**: Other incompatible changes
- **Includes context snippets**: Each error shows 3 lines of YANG code before and after the problem location
- For REMOVED items: shows the definition from the source file
- For CHANGED items: shows the new definition from the target file

### Plain Diffs (`diff/<module>.diff`)

- Standard unified diff format
- Useful for detailed line-by-line comparison

### Raw pyang Output (`raw/<module>.pyang.txt`)

- Unprocessed pyang `--check-update-from` output
- Contains **all** error messages exactly as pyang generated them
- Includes filtered errors (CONFIG_STATE_MISMATCH, REVISION_ORDER) not shown in analysis reports
- Useful for debugging or custom analysis
- One file per module

## Breaking Change Categories

The tool detects and categorizes the following types of changes:

### Critical Breaking Changes

- **REMOVED**: Containers, lists, leafs, leaf-lists, identities, typedefs removed
- **CHANGED**: Base type changed (e.g., decimal64 → uint64)
- **MANDATORY_ADDED**: Previously optional fields now mandatory
- **Cardinality changes**: min-elements or max-elements changed

### Warnings (Filtered from Reports)

The following error types are **excluded from analysis reports** but remain in raw pyang output:

- **CONFIG_STATE_MISMATCH**: Config leafref points to non-config leaf (YANG validation issue, not a breaking API change)
- **REVISION_ORDER**: New revision date is not newer than old revision (informational only)

These are filtered because they don't represent backwards incompatible API changes.

### Other

- **OTHER**: Other pyang errors not matching known patterns (included in reports)

### Examples

#### Example 1: Identity Removed

```markdown
**Identity REMOVED**
- **Node:** `FEC_TYPE_E_FEC`
- **Location:** Line 1
- **Details:** the identity 'FEC_TYPE_E_FEC', defined at source/YANG/tapi-photonic-media.yang:2011 is illegally removed

**Context:**
```yang
[Source: tapi-photonic-media.yang]
    2008 |         base FEC_TYPE;
    2009 |         description "Generic FEC.";
    2010 |     }
>>> 2011 |     identity FEC_TYPE_E_FEC {
    2012 |         base FEC_TYPE;
    2013 |         description "Enhanced FEC.";
    2014 |     }
```
```

#### Example 2: Type Changed

```markdown
**Node CHANGED**
- **Location:** Line 975
- **Details:** Type changed: decimal64 → uint64

**Context:**
```yang
[Target: tapi-photonic-media.yang]
     972 |             description "The gross bitrate...";
     973 |         }
     974 |         leaf max-diff-group-delay {
>>>  975 |             type uint64;
     976 |             config false;
     977 |             description "Maximum Differential group delay...";
     978 |                 Specified in picoseconds.";
```
```

## Troubleshooting

### pyang not found

```bash
pip install --user pyang
# or
pipx install pyang
```

### pyang version too old

```bash
pip install --upgrade pyang
```

### GitPython not installed

```bash
pip install GitPython
```

### Permission denied on git clone

Ensure you have network access and the repository URL is correct.

### No breaking changes detected but expected

- Verify both version tags exist: `git ls-remote --tags <repo-url>`
- Check if modules actually changed between versions
- Ensure pyang is working: `pyang --version`

## Advanced Usage

### Compare Specific Versions

```bash
# Compare any two tags
python3 compare_tapi_versions.py \
  --repo-url https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI.git \
  --source-version v2.4.1 \
  --target-version v2.5.0 \
  --output-dir ./output-v2.4.1-to-v2.5.0
```

### Use Local Repository

If you already have the TAPI repository cloned locally, you can still use this tool by providing the remote URL (it will clone to a temporary location for comparison).

## How It Works

1. **Clone Repository**: Clones TAPI repo to temporary directory
2. **Extract Modules**: Extracts all YANG modules from both version tags
3. **Dependency Resolution**: Ensures all imported modules are available
4. **pyang Comparison**: Runs `pyang --check-update-from` for each module
5. **Parse Results**: Parses pyang error messages using regex patterns
6. **Generate Reports**: Creates markdown reports with categorized changes
7. **Generate Diffs**: Creates plain text diffs for reference

## Technical Details

### Dependency Resolution

The tool extracts **all** YANG modules from both versions (not just the ones being compared) to ensure pyang can resolve all imports correctly. This is critical for modules like `tapi-photonic-media` which imports 5 other modules.

### pyang Flags Used

```bash
pyang --check-update-from <old_module> <new_module> \
      -P <old_yang_dir> \   # Search path for old modules
      -p <new_yang_dir>     # Search path for new modules
```

### Error Parsing

pyang outputs structured error messages that are parsed using regex patterns:

```
/path/file.yang:765: error: the container 'name' ... is illegally removed
```

Extracted information:
- File path and line number
- Node type (container, list, leaf, etc.)
- Node name
- Change type (removed, changed, etc.)

## Contributing

Suggestions and improvements welcome! This tool is designed to be:

- **Simple**: Pure Python with minimal dependencies
- **Reliable**: Uses pyang's official validation
- **Maintainable**: Clear code structure and documentation

## License

This tool is provided as-is for TAPI development and analysis.

## References

- [TAPI GitHub Repository](https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI)
- [pyang Documentation](https://github.com/mbj4668/pyang)
- [RFC 6020](https://tools.ietf.org/html/rfc6020) - YANG 1.0
- [RFC 7950](https://tools.ietf.org/html/rfc7950) - YANG 1.1
