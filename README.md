# Lodgify MCP Server

A Model Context Protocol (MCP) server for the Lodgify vacation rental API. Provides tools for managing properties, bookings, and calendar data.

## Installation

### 🚀 Current Working Method

**Local Installation** (Recommended until PyPI publishing is complete):

```bash
# Clone and install locally
git clone https://github.com/Fast-Transients/lodgify-mcp-server.git
cd lodgify-mcp-server
uv sync

# Test with your API key
export LODGIFY_API_KEY="your_api_key_here"
uv run python entrypoint.py --mode info
```

### 📖 Platform-Specific Guides

- **Mac Users**: [Complete Mac Setup Guide](MAC_SETUP_GUIDE.md) - Step-by-step instructions
- **Windows Users**: See local installation above, then use Windows config below

### 🔮 Future Methods (Coming Soon)

**Via mcp-get:**
```bash
npx @michaellatman/mcp-get@latest install lodgify
```

**Via uvx:**
```bash
uvx lodgify-mcp-server
```

#### Local Claude Desktop Configuration

**Windows:**
```json
{
  "mcpServers": {
    "lodgify": {
      "command": "uv",
      "args": ["run", "--directory", "C:\\path\\to\\lodgify-mcp-server", "python", "entrypoint.py"],
      "env": {
        "LODGIFY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Mac/Linux:**
```json
{
  "mcpServers": {
    "lodgify": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/lodgify-mcp-server", "python", "entrypoint.py"],
      "env": {
        "LODGIFY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

## Claude Desktop Integration

**Currently use local installation** (until PyPI publishing is complete):

**Windows:**
```json
{
  "mcpServers": {
    "lodgify": {
      "command": "uv",
      "args": ["run", "--directory", "C:\\path\\to\\lodgify-mcp-server", "python", "entrypoint.py"],
      "env": {
        "LODGIFY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Mac/Linux:**
```json
{
  "mcpServers": {
    "lodgify": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/lodgify-mcp-server", "python", "entrypoint.py"],
      "env": {
        "LODGIFY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Future uvx method** (once published to PyPI):
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

### Getting "spawn uvx ENOENT" error?

📋 **[Quick Fix Guide](QUICK_FIX_UVX_ERROR.md)** - Fix the uvx error by using local installation

### Getting "spawn uv ENOENT" error?

📋 **[Mac UV PATH Fix](MAC_UV_PATH_FIX.md)** - Fix PATH issues with uv command on Mac

**"API key is required" error?** Make sure you're using `-e` flag in Docker:

✅ **Correct:**

```json
"args": ["run", "-i", "--rm", "-e", "LODGIFY_API_KEY=your_key", "image", "--mode", "server"]
```

❌ **Incorrect:**

```json
"env": {"LODGIFY_API_KEY": "your_key"}
```

## Security

After syncing dependencies with `uv sync`, run `pip-audit` to scan for known
vulnerabilities:

```bash
uv sync
pip-audit
```

This repository pins `starlette` to version 0.47.0 in `uv.lock` to address
upstream advisories.

## Links

- [Lodgify API Docs](https://docs.lodgify.com/)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [GitHub Issues](https://github.com/fast-transients/lodgify-mcp-server/issues)
