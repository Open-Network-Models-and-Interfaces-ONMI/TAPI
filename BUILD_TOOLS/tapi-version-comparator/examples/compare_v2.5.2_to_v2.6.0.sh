#!/bin/bash
#
# Example script to compare TAPI v2.5.2 to v2.6.0
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPARATOR_DIR="$(dirname "$SCRIPT_DIR")"

echo "Running TAPI Version Comparison: v2.5.2 → v2.6.0"
echo "================================================"
echo ""

python3 "$COMPARATOR_DIR/compare_tapi_versions.py" \
  --repo-url https://github.com/Open-Network-Models-and-Interfaces-ONMI/TAPI.git \
  --source-version v2.5.2 \
  --target-version v2.6.0 \
  --output-dir "$SCRIPT_DIR/output-v2.5.2-to-v2.6.0"

echo ""
echo "Comparison complete!"
echo "Results: $SCRIPT_DIR/output-v2.5.2-to-v2.6.0/comparison-report.md"
