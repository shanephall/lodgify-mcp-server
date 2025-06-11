# Changelog

## [0.2.0] - 2025-06-10

### Changed
- **Version strategy** - Updated to 0.2.0 to reflect beta-ready status with comprehensive feature set
- **Development status** - Upgraded from Alpha to Beta classification
- **Repository migration** - Updated all references from personal account (shanephall) to business account (fast-transients)
- **Simplified repository structure** - Removed redundant files and documentation
- **Streamlined README** - Consolidated setup instructions into concise format
- **Simplified Docker Compose** - Removed unnecessary complexity
- **Cleaned up build configuration** - Updated to reflect actual file structure
- **Documentation organization** - Moved project notes to docs/ folder (excluded from git)

### Fixed
- Docker compose YAML formatting issues
- Repository URL references across all files
- Docker image registry paths

### Removed
- Multiple duplicate entrypoint files (`entrypoint_backup.py`, `entrypoint_fixed.py`)
- Unused `main.py` file
- Verbose `llms.txt` documentation (consolidated into README)
- Test configuration files no longer needed
- Cache directories and temporary files

## [0.1.0] - 2025-05-30

### Added
- Initial beta release of Lodgify MCP Server
- Complete Lodgify API integration with MCP protocol
- Property and booking management tools
- Docker containerization support
- GitHub Actions CI/CD pipeline
- Initial Lodgify MCP Server implementation

