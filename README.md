# Lodgify MCP Server

A Model Context Protocol (MCP) server for the Lodgify vacation rental API. Provides tools for managing properties, bookings, and calendar data.

## Quick Start

### Using with Claude Desktop (Recommended)

1. **Copy the example configuration:**
   ```bash
   # Copy the example file from this repository
   cp claude_desktop_config_example.json claude_desktop_config.json
   ```

2. **Edit with your API key:**
   Replace `your_lodgify_api_key_here` with your actual Lodgify API key in the config file.

3. **Add to Claude Desktop:**
   Merge the configuration into your Claude Desktop config file (see [Claude Desktop Integration](#claude-desktop-integration) section below).

### Manual Docker Usage

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

## Claude Desktop Integration

To use this MCP server with Claude Desktop, add it to your `claude_desktop_config.json` file:

### Option 1: Docker (Recommended)

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

### Option 2: Local Python Installation

First, clone and set up the repository:

```bash
git clone https://github.com/shanephall/lodgify-mcp-server.git
cd lodgify-mcp-server
uv sync
```

Then add to your Claude Desktop config:

```json
{
  "mcpServers": {
    "lodgify-api": {
      "command": "python",
      "args": ["/path/to/lodgify-mcp-server/entrypoint.py", "--mode", "server"],
      "env": {
        "LODGIFY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### Configuration File Locations

- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

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

## Troubleshooting

### Common Issues

#### "API key is required for this mode" Error

This error typically occurs when the API key isn't being passed correctly to the Docker container.

**Solution for Claude Desktop Docker config:**
- ❌ **Incorrect** (doesn't work):
  ```json
  {
    "command": "docker",
    "args": ["run", "-i", "--rm", "image-name", "--mode", "server"],
    "env": {
      "LODGIFY_API_KEY": "your_key"
    }
  }
  ```

- ✅ **Correct** (works):
  ```json
  {
    "command": "docker", 
    "args": [
      "run", "-i", "--rm",
      "-e", "LODGIFY_API_KEY=your_key",
      "image-name", "--mode", "server"
    ]
  }
  ```

#### Testing Your Setup

Test your API key before using with Claude Desktop:

```bash
# Test the Docker image
docker run --rm -e LODGIFY_API_KEY=your_api_key_here ghcr.io/shanephall/lodgify-mcp-server:latest --mode test

# Test local installation
export LODGIFY_API_KEY=your_api_key_here
python entrypoint.py --mode test
```

## Support

- **Lodgify API**: [docs.lodgify.com](https://docs.lodgify.com/)
- **This Server**: [GitHub Issues](https://github.com/shanephall/lodgify-mcp-server/issues)
- **MCP Protocol**: [modelcontextprotocol.io](https://modelcontextprotocol.io/)