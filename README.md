# Lodgify MCP Server

A Model Context Protocol (MCP) server for interacting with the Lodgify vacation rental API. This server provides tools and resources for managing properties, bookings, rates, and calendar data through the Lodgify platform.

## Features

- 🏠 **Property Management**: List, view, and manage vacation rental properties
- 📅 **Booking Operations**: Create, view, and update bookings
- 📊 **Calendar & Availability**: Check property availability and rates
- 🔧 **Interactive Prompts**: Pre-built workflows for common tasks
- 🐳 **Docker Support**: Easy deployment with Docker containers
- ⚡ **Fast & Reliable**: Built with modern Python async/await patterns

## Quick Start with Docker

### Using Docker Compose (Recommended)

1. Clone this repository:
```bash
git clone https://github.com/shanephall/lodgify-mcp-server.git
cd lodgify-mcp-server
```

2. Create your environment file:
```bash
cp .env.example .env
```

3. Edit `.env` and add your Lodgify API key:
```bash
LODGIFY_API_KEY=your_actual_api_key_here
```

4. Start the server:
```bash
docker-compose up -d
```

### Using Docker directly

```bash
docker run -d \
  --name lodgify-mcp-server \
  -e LODGIFY_API_KEY=your_api_key_here \
  -p 8000:8000 \
  ghcr.io/shanephall/lodgify-mcp-server:latest
```

### Using the GitHub Container Registry

The Docker images are automatically built and published to GitHub Container Registry on every release:

```bash
docker pull ghcr.io/shanephall/lodgify-mcp-server:latest
```

Available tags:
- `latest` - Latest stable release from main branch
- `v1.0.0` - Specific version tags
- `main` - Latest development build

## Local Development

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/shanephall/lodgify-mcp-server.git
cd lodgify-mcp-server
```

2. Install dependencies:
```bash
uv sync
```

3. Set your Lodgify API key:
```bash
export LODGIFY_API_KEY=your_api_key_here
```

4. Run the server:
```bash
python lodgify_server.py
```

## Configuration

The server requires a Lodgify API key to function. You can obtain one from your Lodgify account settings.

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `LODGIFY_API_KEY` | Your Lodgify API key | Yes |

## API Tools

The MCP server provides the following tools:

### Property Management
- `get_properties` - List all properties with filtering options
- `get_property_by_id` - Get detailed information about a specific property

### Booking Management
- `get_bookings` - List bookings with filtering options
- `get_booking_by_id` - Get detailed information about a specific booking
- `create_booking` - Create a new booking
- `update_booking_status` - Update the status of an existing booking

### Calendar & Availability
- `get_calendar` - Get calendar/availability information for properties

## Resources

The server exposes these resources for LLM context:

- `lodgify://properties` - Summary list of all properties
- `lodgify://property/{property_id}` - Detailed property information
- `lodgify://bookings/recent` - Recent bookings summary

## Interactive Prompts

Pre-built prompts for common workflows:

- `analyze_lodgify_data` - Analyze property and booking data for insights
- `create_booking_workflow` - Step-by-step booking creation guide
- `property_management_review` - Comprehensive account review

## Building the Docker Image

To build the Docker image locally:

```bash
docker build -t lodgify-mcp-server .
```

### Multi-platform builds

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t lodgify-mcp-server .
```

## CI/CD

This repository includes GitHub Actions workflows that automatically:

- Build Docker images for multiple platforms (AMD64, ARM64)
- Push images to GitHub Container Registry
- Run basic tests on the built images
- Tag images with version numbers and `latest`

The workflow triggers on:
- Pushes to `main` branch
- Version tags (e.g., `v1.0.0`)
- Pull requests (build only, no push)

## Health Checks

The Docker container includes health checks that verify the application can start properly. The health check runs every 30 seconds and will mark the container as unhealthy if it fails 3 consecutive checks.

## Security

- The Docker container runs as a non-root user for security
- API keys should be provided via environment variables, never hardcoded
- The container only exposes necessary ports

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker: `docker build -t test .`
5. Submit a pull request

## License

[Add your license here]

## Support

For issues related to:
- **Lodgify API**: Check the [Lodgify API documentation](https://docs.lodgify.com/)
- **This MCP Server**: Open an issue on GitHub
- **Model Context Protocol**: See the [MCP documentation](https://modelcontextprotocol.io/)

## Changelog

### v0.1.0
- Initial release
- Basic property and booking management
- Docker containerization
- GitHub Actions CI/CD