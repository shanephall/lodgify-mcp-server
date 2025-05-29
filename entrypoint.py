#!/usr/bin/env python3
"""
Entry point script for the Lodgify MCP Server Docker container.
This provides a flexible way to start the server with different configurations.
"""

import os
import sys
import argparse
import asyncio
import json
from pathlib import Path

def test_api_connection():
    """Test the Lodgify API connection."""
    print("Testing Lodgify API connection...")
    try:
        import httpx
        api_key = os.getenv("LODGIFY_API_KEY")
        if not api_key:
            print("❌ Error: LODGIFY_API_KEY not found", file=sys.stderr)
            print("   Please set the LODGIFY_API_KEY environment variable", file=sys.stderr)
            return False
        
        if api_key.lower() in ['test', 'test123', 'dummy', 'fake']:
            print(f"⚠️  Warning: Using test API key '{api_key}' - this will fail")
            
        headers = {
            "X-ApiKey": api_key,
            "Content-Type": "application/json"
        }
        
        print(f"🔑 Using API key: {api_key[:8]}{'*' * (len(api_key) - 8)}")
        
        response = httpx.get(
            "https://api.lodgify.com/v2/properties?limit=1",
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ Lodgify API connection successful")
            data = response.json()
            if isinstance(data, dict) and 'items' in data:
                count = len(data['items'])
                print(f"   Found {count} properties in account")
            return True
        elif response.status_code == 401:
            print("❌ API connection failed: Invalid API key")
            print("   Please check your LODGIFY_API_KEY is correct")
            return False
        elif response.status_code == 403:
            print("❌ API connection failed: Access forbidden")
            print("   Please check your API key permissions")
            return False
        elif response.status_code >= 500:
            print(f"❌ API connection failed: Server error ({response.status_code})")
            print("   Lodgify API appears to be having issues")
            return False
        else:
            print(f"❌ API connection failed with status {response.status_code}")
            try:
                error_data = response.json()
                if isinstance(error_data, dict) and 'message' in error_data:
                    print(f"   Error: {error_data['message']}")
            except:
                print(f"   Response: {response.text[:200]}...")
            return False
    except httpx.TimeoutException:
        print("❌ API connection error: Request timed out")
        print("   Please check your internet connection")
        return False
    except Exception as e:
        print(f"❌ API connection error: {e}")
        return False

def run_mcp_server():
    """Run the MCP server."""
    try:
        # Ensure we have an API key for server mode
        api_key = os.getenv("LODGIFY_API_KEY")
        if not api_key:
            print("❌ Error: LODGIFY_API_KEY is required for server mode", file=sys.stderr)
            sys.exit(1)
            
        from lodgify_server import mcp
        print("🚀 Starting Lodgify MCP Server...")
        print("📡 Server is ready to accept MCP protocol messages via stdin/stdout")
        print("🔗 Connect this server to an MCP client like Claude Desktop")
        
        # Set up proper signal handling for graceful shutdown
        import signal
        def signal_handler(signum, frame):
            print(f"\n🛑 Received signal {signum}, shutting down gracefully...")
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        # Run the server
        mcp.run()
    except ImportError as e:
        print(f"❌ Error importing lodgify_server: {e}", file=sys.stderr)
        print("   Make sure all dependencies are installed correctly", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting server: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Lodgify MCP Server")
    parser.add_argument(
        "--mode",
        choices=["server", "test", "info"],
        default="info",
        help="Run mode: 'server' (MCP server), 'test' (test API connection), 'info' (show server info, default)"
    )
    parser.add_argument(
        "--api-key",
        default=os.getenv("LODGIFY_API_KEY"),
        help="Lodgify API key (can also use LODGIFY_API_KEY env var)"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode"
    )
    
    args = parser.parse_args()
    
    # Set environment variables
    if args.api_key:
        os.environ["LODGIFY_API_KEY"] = args.api_key
    
    if args.debug:
        os.environ["PYTHONPATH"] = "/app"
        print(f"Debug mode enabled")
        print(f"API key set: {'Yes' if args.api_key else 'No'}")
        print(f"Mode: {args.mode}")
    
    # Validate API key for modes that need it
    if args.mode in ["server", "test"] and not args.api_key:
        print("Error: LODGIFY_API_KEY environment variable or --api-key argument is required", file=sys.stderr)
        sys.exit(1)
      # Run based on mode
    if args.mode == "test":
        success = test_api_connection()
        sys.exit(0 if success else 1)
    elif args.mode == "info":
        print("🏠 Lodgify MCP Server")
        print("=" * 50)
        print("📋 This is a Model Context Protocol (MCP) server for the Lodgify API.")
        print("🏨 It provides tools and resources for managing vacation rental properties.")
        
        api_key = os.getenv('LODGIFY_API_KEY')
        if api_key:
            masked_key = api_key[:8] + '*' * (len(api_key) - 8) if len(api_key) > 8 else '*' * len(api_key)
            print(f"🔑 API key configured: Yes ({masked_key})")
        else:
            print("🔑 API key configured: ❌ No")
            
        print("\n📖 To use this server, connect it to an MCP client like Claude Desktop.")
        print("🔌 The server communicates via JSON-RPC over stdin/stdout.")
        print("\n⚙️  Available modes:")
        print("  --mode info   : Show this information (default)")
        print("  --mode test   : Test API connectivity")
        print("  --mode server : Run the MCP server")
        print("\n🐳 Docker usage:")
        print("  docker run -e LODGIFY_API_KEY=your_key lodgify-mcp-server --mode test")
        print("  docker run -e LODGIFY_API_KEY=your_key lodgify-mcp-server --mode server")
    elif args.mode == "server":
        # Test connection first
        if not test_api_connection():
            print("Warning: API connection test failed, but starting server anyway...")
        run_mcp_server()
    else:
        print(f"Unknown mode: {args.mode}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
