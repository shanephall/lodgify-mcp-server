# Quick Fix for uvx ENOENT Error

## Problem
Getting this error in Claude Desktop:
```
spawn uvx ENOENT
```

## Cause
The package `lodgify-mcp-server` isn't published to PyPI yet, so `uvx` can't find it.

## Solution
Use local installation instead of uvx.

### Step 1: Install Locally
```bash
# Clone the repository
git clone https://github.com/Fast-Transients/lodgify-mcp-server.git
cd lodgify-mcp-server
uv sync
```

### Step 2: Update Claude Desktop Config

**Replace your current config that has:**
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

**With this local config:**

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

### Step 3: Update the Path
Replace the directory path with your actual path to where you cloned the repository.

### Step 4: Restart Claude Desktop
Completely quit and restart Claude Desktop.

## Test
Ask Claude: "What Lodgify tools are available?"
