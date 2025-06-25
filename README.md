# Lodgify MCP Server

A Model Context Protocol (MCP) server for the Lodgify vacation rental API. It exposes tools for managing properties, bookings and calendar data.

## Quick start
Install dependencies with `uv` and run the server with `uvx`:

```bash
export LODGIFY_API_KEY=your_api_key
uvx lodgify-mcp-server
```

To run from source:

```bash
git clone https://github.com/fast-transients/lodgify-mcp-server.git
cd lodgify-mcp-server
uv sync
export LODGIFY_API_KEY=your_api_key
uv run python entrypoint.py
```

## Claude Desktop configuration
Add this block to your Claude Desktop configuration (see examples in the `examples/` folder):

```json
{
  "mcpServers": {
    "lodgify": {
      "command": "uvx",
      "args": ["lodgify-mcp-server"],
      "env": {
        "LODGIFY_API_KEY": "your_api_key"
      }
    }
  }
}
```

## Available tools
- **Properties**: `get_properties`, `get_property_by_id`
- **Bookings**: `get_bookings`, `get_booking_by_id`, `create_booking`, `update_booking_status`
- **Calendar**: `get_calendar`

## Troubleshooting
- Ensure the `LODGIFY_API_KEY` environment variable is set.
- Getting `spawn uvx ENOENT`? Install `uv` from [astral.sh/uv](https://astral.sh/uv/) and restart your shell.

## Security
After syncing dependencies, run `pip-audit` to check for known vulnerabilities. The `uv.lock` file pins `starlette` 0.47.0 to address upstream advisories.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and testing instructions.
