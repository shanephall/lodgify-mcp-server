# Complete Mac Setup Guide for Lodgify MCP Server

## Prerequisites Setup

### Step 1: Install Required Tools

```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install uv (Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.zshrc  # or restart your terminal

# Install Git (if not already installed)
brew install git
```

### Step 2: Get Your Lodgify API Key

1. Log into your Lodgify account
2. Navigate to **Settings** → **API** → **API Keys**
3. Generate a new API key and copy it safely

### Step 3: Install Claude Desktop

1. Download Claude Desktop from the official website
2. Install and sign in to your Claude account

## MCP Server Setup

### Step 4: Download and Install the Server

```bash
# Create a directory for MCP servers
mkdir -p ~/mcp-servers
cd ~/mcp-servers

# Clone the repository
git clone https://github.com/Fast-Transients/lodgify-mcp-server.git
cd lodgify-mcp-server

# Install dependencies
uv sync

# Test the server (replace YOUR_API_KEY with your actual key)
export LODGIFY_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
uv run python entrypoint.py --mode info
```

### Step 5: Configure Claude Desktop

#### Find Your Username

```bash
echo $USER
```

#### Create Configuration Directory

```bash
mkdir -p ~/Library/Application\ Support/Claude
```

#### Create Configuration File

```bash
# Open the config file in your default editor
open ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

#### Add This Configuration

Replace `YOUR_USERNAME` with the output from the `echo $USER` command above, and `YOUR_ACTUAL_API_KEY_HERE` with your Lodgify API key:

```json
{
  "mcpServers": {
    "lodgify": {
      "command": "uv",
      "args": ["run", "--directory", "/Users/YOUR_USERNAME/mcp-servers/lodgify-mcp-server", "python", "entrypoint.py"],
      "env": {
        "LODGIFY_API_KEY": "YOUR_ACTUAL_API_KEY_HERE"
      }
    }
  }
}
```

### Step 6: Test the Setup

1. **Completely restart Claude Desktop** (quit and reopen)
2. **Start a new conversation**
3. **Test the connection** by asking: "What Lodgify tools are available?"
4. **Try a real query**: "Show me my properties" or "Get my recent bookings"

## Troubleshooting

### Check Server Functionality

```bash
cd ~/mcp-servers/lodgify-mcp-server
export LODGIFY_API_KEY="YOUR_API_KEY"
uv run python entrypoint.py --mode info
```

### Verify API Key

```bash
uv run python -c "
import os
import httpx
api_key = os.getenv('LODGIFY_API_KEY')
response = httpx.get('https://api.lodgify.com/v2/properties?limit=1', 
                    headers={'X-ApiKey': api_key})
print(f'API Status: {response.status_code}')
if response.status_code == 200:
    print('✅ API key is working!')
else:
    print('❌ API key issue - check your key')
"
```

### Check Configuration Path

```bash
# Verify the config file exists and has content
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### Common Issues

1. **Path not found**: Make sure to replace `YOUR_USERNAME` with your actual username
2. **API key invalid**: Double-check your API key from Lodgify settings
3. **Server won't start**: Make sure you're in the correct directory and ran `uv sync`
4. **Claude doesn't see the server**: Restart Claude Desktop completely

## Testing Commands

Once connected, try these in Claude:

- "What Lodgify tools are available?"
- "Show me my properties"
- "Get my recent bookings"
- "What's the calendar availability for property ID 123?"

## Success Indicators

You'll know it's working when:
- Claude Desktop shows no error messages on startup
- Claude can list the Lodgify tools when asked
- You can successfully query your properties and bookings
- The server responds with real data from your Lodgify account
