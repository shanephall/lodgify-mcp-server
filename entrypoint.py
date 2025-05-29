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
            print("Error: LODGIFY_API_KEY not found", file=sys.stderr)
            return False
            
        headers = {
            "X-ApiKey": api_key,
            "Content-Type": "application/json"
        }
        
        response = httpx.get(
            "https://api.lodgify.com/v2/properties?limit=1",
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            print("Lodgify API connection successful")
            return True
        else:
            print(f"API connection failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"API connection error: {e}")
        return False

def run_mcp_server():
    """Run the MCP server."""
    try:
        from lodgify_server import mcp
        print("Starting Lodgify MCP Server...")
        print("Server is ready to accept MCP protocol messages via stdin/stdout")
        mcp.run()
    except ImportError as e:
        print(f"Error importing lodgify_server: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)
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
        print("Lodgify MCP Server")
        print("================")
        print("This is a Model Context Protocol (MCP) server for the Lodgify API.")
        print("It provides tools and resources for managing vacation rental properties.")
        print(f"API key configured: {'Yes' if os.getenv('LODGIFY_API_KEY') else 'No'}")
        print("\nTo use this server, connect it to an MCP client like Claude Desktop.")
        print("The server communicates via JSON-RPC over stdin/stdout.")
        print("\nAvailable modes:")
        print("  --mode info   : Show this information (default)")
        print("  --mode test   : Test API connectivity")
        print("  --mode server : Run the MCP server")
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
