# Mac UV Path Fix

## Problem
Getting `spawn uv ENOENT` error - Claude Desktop can't find the `uv` command.

## Root Cause
`uv` is not in Claude Desktop's PATH. This happens because:
1. `uv` was installed but not added to system PATH
2. Claude Desktop runs with limited environment variables

## Solution 1: Fix PATH (Recommended)

```bash
# 1. Check if uv is installed
which uv

# 2. If not found, find where uv is installed
find ~ -name "uv" -type f 2>/dev/null

# 3. Add to your shell's PATH (choose your shell)
# For zsh (default on newer Macs):
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# For bash:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# 4. Verify uv works
uv --version
```

## Solution 2: Use Full Path (Quick Fix)

Update your Claude Desktop config with the full path:

```json
{
  "mcpServers": {
    "lodgify": {
      "command": "/Users/shanehall/.local/bin/uv",
      "args": ["run", "--directory", "/Users/shanehall/mcp-servers/lodgify-mcp-server", "python", "entrypoint.py"],
      "env": {
        "LODGIFY_API_KEY": "YOUR_ACTUAL_API_KEY_HERE"
      }
    }
  }
}
```

## Solution 3: Reinstall UV with Homebrew

```bash
# Remove existing uv
curl -LsSf https://astral.sh/uv/uninstall.sh | sh

# Install via Homebrew (better PATH integration)
brew install uv

# Test
uv --version
```

## After Fixing

1. Restart Claude Desktop completely
2. Test with: "What Lodgify tools are available?"

## Common Paths for UV

- **Direct install: `~/.local/bin/uv`** ← YOUR CASE
- Cargo install: `~/.cargo/bin/uv`
- Homebrew: `/usr/local/bin/uv` or `/opt/homebrew/bin/uv`
