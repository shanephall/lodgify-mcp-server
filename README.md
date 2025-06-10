# Lodgify MCP Server

A Model Context Protocol (MCP) server for the Lodgify vacation rental API. Provides tools for managing properties, bookings, and calendar data.

## Quick Start

### Claude Desktop Integration (Recommended)

Add this configuration to your Claude Desktop config file:

```json
{
  "mcpServers": {
    "lodgify-api": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm", 
        "-e", "LODGIFY_API_KEY=your_api_key_here",
        "ghcr.io/shanephall/lodgify-mcp-server:latest",
        "--mode", "server"
      ]
    }
  }
}
```

**Config file locations:**
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`  
- Linux: `~/.config/Claude/claude_desktop_config.json`

### Test Your Setup

```bash
# Test Docker image with your API key
docker run --rm -e LODGIFY_API_KEY=your_api_key_here ghcr.io/shanephall/lodgify-mcp-server:latest --mode test
```

## Available Tools

- **Properties**: `get_properties`, `get_property_by_id`
- **Bookings**: `get_bookings`, `get_booking_by_id`, `create_booking`, `update_booking_status`
- **Calendar**: `get_calendar` (availability checking)

## Local Development

```bash
git clone https://github.com/shanephall/lodgify-mcp-server.git
cd lodgify-mcp-server
uv sync
export LODGIFY_API_KEY=your_api_key_here
python lodgify_server.py
```

## Docker Compose

```bash
git clone https://github.com/shanephall/lodgify-mcp-server.git
cd lodgify-mcp-server
cp .env.example .env
# Edit .env with your LODGIFY_API_KEY
docker-compose up -d server
```

## Troubleshooting

**"API key is required" error?** Make sure you're using `-e` flag in Docker:

✅ **Correct:**

```json
"args": ["run", "-i", "--rm", "-e", "LODGIFY_API_KEY=your_key", "image", "--mode", "server"]
```

❌ **Incorrect:**

```json
"env": {"LODGIFY_API_KEY": "your_key"}
```

## Links

- [Lodgify API Docs](https://docs.lodgify.com/)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [GitHub Issues](https://github.com/shanephall/lodgify-mcp-server/issues)