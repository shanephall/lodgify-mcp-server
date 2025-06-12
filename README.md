# Lodgify MCP Server

A Model Context Protocol (MCP) server for the Lodgify vacation rental API. Provides tools for managing properties, bookings, and calendar data.

## Installation

### Via mcp-get (Recommended)

```bash
npx @michaellatman/mcp-get@latest install lodgify
```

### Via uv (Direct)

```bash
uvx lodgify-mcp-server
```

### Manual Installation

```bash
uv add lodgify-mcp-server
```

### Local Development Installation

If the package isn't available on PyPI yet, you can test locally:

```bash
# Clone and install locally
git clone https://github.com/Fast-Transients/lodgify-mcp-server.git
cd lodgify-mcp-server
uv sync
```

Then use this Claude Desktop configuration:

```json
{
  "mcpServers": {
    "lodgify-local": {
      "command": "uv",
      "args": ["run", "--directory", "C:\\path\\to\\lodgify-mcp-server", "python", "entrypoint.py"],
      "env": {
        "LODGIFY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

## Quick Start

### Claude Desktop Integration (Recommended)

Add this configuration to your Claude Desktop config file:

```json
{
  "mcpServers": {
    "lodgify": {
      "command": "uvx",
      "args": ["lodgify-mcp-server"],
      "env": {
        "LODGIFY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Alternative Docker configuration:**

```json
{
  "mcpServers": {
    "lodgify-docker": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm", 
        "-e", "LODGIFY_API_KEY=your_api_key_here",
        "ghcr.io/fast-transients/lodgify-mcp-server:latest",
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

```powershell
# Test Docker image with your API key
docker run --rm -e LODGIFY_API_KEY=your_api_key_here ghcr.io/fast-transients/lodgify-mcp-server:latest --mode test
```

## Available Tools

- **Properties**: `get_properties`, `get_property_by_id`
- **Bookings**: `get_bookings`, `get_booking_by_id`, `create_booking`, `update_booking_status`
- **Calendar**: `get_calendar` (availability checking)

## Local Development

```powershell
git clone https://github.com/fast-transients/lodgify-mcp-server.git
cd lodgify-mcp-server
uv sync
$env:LODGIFY_API_KEY="your_api_key_here"
python lodgify_server.py
```

## Docker Compose

```powershell
git clone https://github.com/fast-transients/lodgify-mcp-server.git
cd lodgify-mcp-server
Copy-Item .env.example .env
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
- [GitHub Issues](https://github.com/fast-transients/lodgify-mcp-server/issues)
