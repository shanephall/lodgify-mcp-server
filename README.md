# Lodgify MCP Server

A Model Context Protocol (MCP) server for the Lodgify vacation rental API. Provides tools for managing properties, bookings, and calendar data.

## Claude Desktop Integration

### 🚀 Recommended Method (uvx)

Add this to your Claude Desktop configuration:

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

### Local Development Method

If you're developing locally or prefer to run from source:

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

### Config File Locations

- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`  
- **Linux:** `~/.config/Claude/claude_desktop_config.json`

## Local Development

Clone and set up the project locally:

```bash
git clone https://github.com/fast-transients/lodgify-mcp-server.git
cd lodgify-mcp-server
uv sync
```

Run the server:

**Windows PowerShell:**

```powershell
$env:LODGIFY_API_KEY="your_api_key_here"
uv run python entrypoint.py
```

**Mac/Linux:**

```bash
export LODGIFY_API_KEY="your_api_key_here"
uv run python entrypoint.py
```

## Testing with MCP Inspector

Test your setup using the MCP Inspector:

**Windows PowerShell:**

```powershell
$env:LODGIFY_API_KEY="your_api_key_here"
uvx @modelcontextprotocol/inspector uvx lodgify-mcp-server
```

**Mac/Linux:**

```bash
export LODGIFY_API_KEY="your_api_key_here"
uvx @modelcontextprotocol/inspector uvx lodgify-mcp-server
```

## Installation Methods

### Coming Soon: mcp-get

```bash
npx @michaellatman/mcp-get@latest install lodgify
```

### Direct Installation (uvx)

**Windows PowerShell:**

```powershell
$env:LODGIFY_API_KEY="your_api_key_here"
uvx lodgify-mcp-server
```

**Mac/Linux:**

```bash
export LODGIFY_API_KEY="your_api_key_here"
uvx lodgify-mcp-server
```

## Available Tools

- **Properties**: `get_properties`, `get_property_by_id`
- **Bookings**: `get_bookings`, `get_booking_by_id`, `create_booking`, `update_booking_status`
- **Calendar**: `get_calendar` (availability checking)

## Troubleshooting

### Getting "LODGIFY_API_KEY environment variable is required" error?

This means you need to set your API key before running the server:

**Windows PowerShell:**

```powershell
$env:LODGIFY_API_KEY="your_actual_api_key_here"
uvx lodgify-mcp-server
```

**Mac/Linux:**

```bash
export LODGIFY_API_KEY="your_actual_api_key_here"
uvx lodgify-mcp-server
```

### Getting "spawn uvx ENOENT" error?

This means uvx is not installed or not in PATH. Install it:

**Windows:**

```powershell
# Install uv first, then uvx is included
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Mac/Linux:**

```bash
# Install uv (includes uvx)
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc  # or restart terminal
```

**Alternative**: Use local installation instead:

```bash
git clone https://github.com/fast-transients/lodgify-mcp-server.git
cd lodgify-mcp-server
uv sync
export LODGIFY_API_KEY="your_api_key_here"
uv run python entrypoint.py
```

### Getting "spawn uv ENOENT" error on Mac?

Claude Desktop can't find the `uv` command. Fix the PATH:

```bash
# Add to ~/.zshrc (or ~/.bashrc)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Then restart Claude Desktop.

### API key is required error?

Make sure you've set your LODGIFY_API_KEY environment variable with a valid API key from your Lodgify account.

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

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and testing instructions.
