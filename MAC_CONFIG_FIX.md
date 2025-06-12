# Mac Configuration Fix

## Your Current Config (WRONG)

You have:
```json
{
  "mcpServers": {
    "lodgify": {
      "command": "uvx",
      "args": ["run", "--directory", "/Users/shanehall/mcp-servers/lodgify-mcp-server", "python", "entrypoint.py"],
      "env": {
        "LODGIFY_API_KEY": "YOUR_ACTUAL_API_KEY_HERE"
      }
    }
  }
}
```

## Problem
You're using `uvx` with `--directory` which is incorrect. The `uvx` command is for running packages from PyPI, but you're pointing to a local directory.

## Correct Config
Change `"command": "uvx"` to `"command": "uv"`:

```json
{
  "mcpServers": {
    "lodgify": {
      "command": "uv",
      "args": ["run", "--directory", "/Users/shanehall/mcp-servers/lodgify-mcp-server", "python", "entrypoint.py"],
      "env": {
        "LODGIFY_API_KEY": "YOUR_ACTUAL_API_KEY_HERE"
      }
    }
  }
}
```

## Quick Fix Steps
1. Edit your Claude Desktop config file at: `~/Library/Application Support/Claude/claude_desktop_config.json`
2. Change `"uvx"` to `"uv"` 
3. Make sure your API key is set (replace `YOUR_ACTUAL_API_KEY_HERE`)
4. Restart Claude Desktop completely
5. Test by asking: "What Lodgify tools are available?"

## Why This Happens
- `uvx lodgify-mcp-server` - would work once published to PyPI
- `uv run --directory /path python entrypoint.py` - works with local installation
