from mcp.server.fastmcp import FastMCP
from datetime import datetime
from typing import Optional
import os

# Load environment variables
load_dotenv("../.env")

# Create an MCP server
mcp = FastMCP(
    name="TimeKeeper",
    host="0.0.0.0",  # Used for SSE transport (localhost)
    port=8050,      # Port for SSE transport
    stateless_http=True,
)

@mcp.tool()
def get_current_time() -> str:
    """Returns the current time in ISO 8601 format with millisecond precision."""
    now = datetime.now()
    return now.isoformat(timespec='milliseconds') + 'Z'

# Run the server with SSE transport
if __name__ == "__main__":
    transport = "sse"
    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    elif transport == "streamable-http":
        print("Running server with Streamable HTTP transport")
        mcp.run(transport="streamable-http")
    else:
        raise ValueError(f"Unknown transport: {transport}")

