from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv("../.env")

# Create an MCP server
mcp = FastMCP(
    name="Time Service",
    host="0.0.0.0",
    port=8080
)

# Define the tool
@mcp.tool("get_current_time")
async def get_current_time() -> str:
    """Returns the current timestamp in ISO 8601 format."""
    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z")
    }

# Start the server
if __name__ == "__main__":
    print("Starting MCP server on http://0.0.0.0:8080")
    mcp.run()