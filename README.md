# Lodgify MCP Server

A Model Context Protocol (MCP) server for the Lodgify vacation rental API. Provides tools for managing properties, bookings, and calendar data.

## Quick Start

1. **Get the Docker image:**

   ```bash
   docker pull ghcr.io/shanephall/lodgify-mcp-server:latest
   ```

2. **Test your API key:**

   ```bash
   # Single line (works on all platforms)
   docker run --rm -e LODGIFY_API_KEY=your_api_key_here ghcr.io/shanephall/lodgify-mcp-server:latest --mode test
   
   # Multi-line for Linux/macOS/WSL
   docker run --rm -e LODGIFY_API_KEY=your_api_key_here \
     ghcr.io/shanephall/lodgify-mcp-server:latest --mode test
   
   # Multi-line for Windows PowerShell
   docker run --rm -e LODGIFY_API_KEY=your_api_key_here `
     ghcr.io/shanephall/lodgify-mcp-server:latest --mode test
   ```

3. **Run the MCP server:**

   ```bash
   # Single line (works on all platforms)
   docker run -d --name lodgify-mcp-server -e LODGIFY_API_KEY=your_api_key_here ghcr.io/shanephall/lodgify-mcp-server:latest --mode server
   
   # Multi-line for Linux/macOS/WSL
   docker run -d --name lodgify-mcp-server \
     -e LODGIFY_API_KEY=your_api_key_here \
     ghcr.io/shanephall/lodgify-mcp-server:latest --mode server
   
   # Multi-line for Windows PowerShell  
   docker run -d --name lodgify-mcp-server `
     -e LODGIFY_API_KEY=your_api_key_here `
     ghcr.io/shanephall/lodgify-mcp-server:latest --mode server
   ```

## Using Docker Compose

1. Clone and setup:

   ```bash
   git clone https://github.com/shanephall/lodgify-mcp-server.git
   cd lodgify-mcp-server
   cp .env.example .env
   # Edit .env with your LODGIFY_API_KEY
   ```

2. Start the server:

   ```bash
   docker-compose up -d server
   ```

## MCP Tools

The server provides these tools for LLM interactions:

- **Properties**: `get_properties`, `get_property_by_id`
- **Bookings**: `get_bookings`, `get_booking_by_id`, `create_booking`, `update_booking_status`
- **Calendar**: `get_calendar`

## Configuration

Set your Lodgify API key as an environment variable:

```bash
export LODGIFY_API_KEY=your_api_key_here
```

## Local Development

Requirements: Python 3.10+, [uv](https://github.com/astral-sh/uv)

```bash
git clone https://github.com/shanephall/lodgify-mcp-server.git
cd lodgify-mcp-server
uv sync
export LODGIFY_API_KEY=your_api_key_here
python lodgify_server.py
```

## Support

- **Lodgify API**: [docs.lodgify.com](https://docs.lodgify.com/)
- **This Server**: [GitHub Issues](https://github.com/shanephall/lodgify-mcp-server/issues)
- **MCP Protocol**: [modelcontextprotocol.io](https://modelcontextprotocol.io/)