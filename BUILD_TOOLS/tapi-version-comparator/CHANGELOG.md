# Changelog

All notable changes to the TAPI Version Comparator will be documented in this file.

## [1.0.0] - 2026-09-02

### Added

- Initial release of TAPI Version Comparator
- Core comparison engine using pyang's `--check-update-from` feature
- Automatic dependency resolution for all YANG modules
- Breaking change detection and categorization:
  - REMOVED: Deleted nodes (containers, lists, leafs, identities)
  - CHANGED: Type changes, cardinality changes
  - MANDATORY_ADDED: New required fields
  - OTHER: Other incompatible changes
- Markdown report generation:
  - Master comparison report with executive summary
  - Summary report with module-by-module statistics
  - Detailed per-module reports with categorized changes
- Plain text diff generation for all modules
- Built-in dependency verification (`--verify-deps`)
- Command-line interface with argparse
- Comprehensive documentation:
  - README.md with full documentation
  - QUICKSTART.md for immediate use
  - IMPLEMENTATION_SUMMARY.md with technical details
- Example scripts for common comparisons
- Progress indicators and helpful error messages
- Automatic cleanup of temporary files

### Technical Details

- **Language**: Python 3.8+
- **Dependencies**: GitPython 3.1.0+, pyang 2.6.0+, git
- **Lines of Code**: 566 (main script)
- **Documentation**: 302 lines (README)
- **Test Coverage**: Tested with v2.5.2 → v2.6.0 (15 modules, 194 breaking changes)

### Features

- ✅ No LLM required - pure rule-based parsing
- ✅ Full YANG module dependency resolution
- ✅ Structured error parsing using regex
- ✅ Template-based markdown generation
- ✅ Handles new/removed modules gracefully
- ✅ Supports any TAPI version tags
- ✅ Clean output directory structure
- ✅ Automatic git repository cloning and cleanup

### Known Limitations

- Requires network access to clone repository
- Clones entire repository (not just YANG files)
- First run may take 1-2 minutes depending on network speed
- Output is markdown only (no JSON/HTML yet)

### Future Enhancements

Planned for future releases:
- JSON output format for CI/CD integration
- HTML report with interactive filtering
- Configurable breaking change rules
- Support for comparing specific modules only
- Integration with GitHub Actions
- Caching of cloned repositories
- Parallel module comparison
- Custom report templates

## Version History

- **1.0.0** (2026-09-02): Initial release

---

## Semantic Versioning

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality in a backwards compatible manner
- **PATCH** version for backwards compatible bug fixes
