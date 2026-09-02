# Quick Start Guide

## 1. Verify Dependencies

```bash
cd tapi-version-comparator
python3 compare_tapi_versions.py --verify-deps
```

Expected output:
```
✓ Python: 3.12.x (>= 3.8)
✓ Git: git version 2.x.x (required)
✓ pyang: pyang 2.7.x (>= 2.6.0)
✓ GitPython: 3.1.x (required)

All dependencies satisfied!
```

If GitPython is missing:
```bash
sudo apt-get install python3-git
```

## 2. Run Your First Comparison

```bash
python3 compare_tapi_versions.py \
  --repo-url https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI.git \
  --source-version v2.5.2 \
  --target-version v2.6.0 \
  --output-dir ./output-v2.5.2-to-v2.6.0
```

This will:
- Clone the TAPI repository
- Extract YANG modules from both versions
- Compare all modules using pyang
- Generate detailed reports

## 3. View Results

### Master Report
```bash
cat ./output-v2.5.2-to-v2.6.0/comparison-report.md
```

### Summary
```bash
cat ./output-v2.5.2-to-v2.6.0/analysis/summary.md
```

### Specific Module
```bash
cat ./output-v2.5.2-to-v2.6.0/analysis/tapi-photonic-media.yang.md
```

### Plain Diff
```bash
cat ./output-v2.5.2-to-v2.6.0/diff/tapi-photonic-media.yang.diff
```

### Raw pyang Output
```bash
cat ./output-v2.5.2-to-v2.6.0/raw/tapi-photonic-media.yang.pyang.txt
```

## 4. Use Example Script

```bash
cd examples
./compare_v2.5.2_to_v2.6.0.sh
```

Results will be in `examples/output-v2.5.2-to-v2.6.0/`

## Common Comparisons

### v2.4.1 → v2.5.0 (Major changes)
```bash
python3 compare_tapi_versions.py \
  --repo-url https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI.git \
  --source-version v2.4.1 \
  --target-version v2.5.0 \
  --output-dir ./output-v2.4.1-to-v2.5.0
```

### v2.5.0 → v2.5.2 (Minor changes)
```bash
python3 compare_tapi_versions.py \
  --repo-url https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI.git \
  --source-version v2.5.0 \
  --target-version v2.5.2 \
  --output-dir ./output-v2.5.0-to-v2.5.2
```

## Understanding the Output

### Breaking Change Categories

- **REMOVED**: Nodes (containers, lists, leafs) that were deleted
- **CHANGED**: Type changes, cardinality changes
- **MANDATORY_ADDED**: New mandatory fields (breaks existing implementations)
- **OTHER**: Other incompatible changes

### Report Structure

```
output-dir/
├── comparison-report.md         # Start here - executive summary
├── analysis/
│   ├── summary.md              # Module-by-module statistics
│   └── <module>.md             # Detailed per-module reports
├── diff/
│   └── <module>.diff           # Plain text diffs
└── raw/
    └── <module>.pyang.txt      # Raw pyang output
```

## Tips

1. **Start with the master report** (`comparison-report.md`) for an overview
2. **Check the summary** (`analysis/summary.md`) to see which modules changed
3. **Dive into specific modules** that are relevant to your work
4. **Use plain diffs** for detailed line-by-line comparison
5. **Check raw pyang output** for the original unprocessed error messages

## Troubleshooting

### "GitPython NOT INSTALLED"
```bash
sudo apt-get install python3-git
```

### "pyang NOT FOUND"
```bash
pip install --user pyang
# or
pipx install pyang
```

### Slow performance
The tool clones the entire TAPI repository. First run may take a few minutes depending on network speed. Subsequent runs will be faster if you keep the output directory.

## Next Steps

See [README.md](README.md) for complete documentation.
