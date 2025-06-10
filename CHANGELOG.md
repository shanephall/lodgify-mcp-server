# Changelog

## [1.1.0] - 2025-06-10

### Changed
- **Simplified repository structure** - Removed redundant files and documentation
- **Streamlined README** - Consolidated setup instructions into concise format
- **Simplified Docker Compose** - Removed unnecessary complexity
- **Cleaned up build configuration** - Updated to reflect actual file structure

### Removed
- Multiple duplicate entrypoint files (`entrypoint_backup.py`, `entrypoint_fixed.py`)
- Unused `main.py` file
- Verbose `llms.txt` documentation (consolidated into README)
- Test configuration files no longer needed
- Cache directories and temporary files

## [1.0.0] - 2025-05-30

### Fixed
- Docker containerization and API key validation issues
- Claude Desktop Docker configuration environment variable passing
- MCP protocol communication in containerized environment

### Added
- Multi-mode entrypoint script with info/test/server modes
- Enhanced error handling and user feedback
- Docker health checks and proper logging

## [0.1.0] - 2025-05-29

### Added
- Initial Lodgify MCP Server implementation
- Complete Lodgify API integration with MCP protocol
- Property and booking management tools
- Docker containerization support
- GitHub Actions CI/CD pipeline
