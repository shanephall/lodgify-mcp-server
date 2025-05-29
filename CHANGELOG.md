# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- Docker containerization issues resolved completely
- Python version mismatch between .python-version (3.11) and Dockerfile
- Virtual environment path issues in Docker container
- MCP protocol communication problems in containerized environment
- Health check commands updated to use correct Python executable
- API key validation with clear error messages
- Docker Compose configuration improved with proper networking and logging

### Added

- Comprehensive multi-mode entrypoint script (`entrypoint.py`)
  - Info mode: Shows server information and configuration status
  - Test mode: Validates API connectivity and configuration
  - Server mode: Runs MCP server with proper stdin/stdout communication
- Enhanced Docker health checks with proper validation
- Improved error handling and user feedback for containerized deployment
- Better logging configuration in Docker Compose

### Changed

- Dockerfile optimized to avoid package building conflicts
- Docker build process restructured for better layer caching
- Health check commands updated to use virtual environment Python
- Container security improved with non-root user execution

## [0.1.0] - 2025-05-29

### Features

- Initial release of Lodgify MCP Server
- Complete Lodgify API integration with MCP protocol
- Property management tools (list, view, manage properties)
- Booking operations (create, view, update bookings)
- Calendar and availability checking
- Interactive prompts for common workflows
- Docker containerization support
- GitHub Actions CI/CD pipeline
- Multi-platform Docker builds (AMD64, ARM64)
- Comprehensive API tools and resources
- Health check endpoints
- Environment-based configuration

### Security

- Non-root user execution in Docker containers
- API key management through environment variables
- Secure defaults for container deployment

## [0.0.1] - 2025-05-28

### Initial Features

- Basic project structure
- Initial MCP server implementation
- Lodgify API client integration
- Development tooling setup
