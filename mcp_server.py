import datetime
import logging
import asyncio
from typing import Optional

from fastapi import FastAPI, Response, Request
from starlette.responses import StreamingResponse

logger = logging.getLogger(__name__)

class MCPServer:
    def __init__(self, transport: str = "sse"):
        self.app = FastAPI(title="MCP Server", version="1.0")
        self.transport = transport
        self._setup_routes()

    def _setup_routes(self):
        @self.app.get("/time")
        async def get_current_time(request: Request):
            """Endpoint to return current time via Server-Sent Events"""
            if self.transport == "sse":
                async def time_generator():
                    while True:
                        current_time = datetime.datetime.now().isoformat()
                        yield f"data: {current_time}\n\n"
                        await asyncio.sleep(1)  # Update every second

                return StreamingResponse(time_generator(), media_type="text/event-stream")
            elif self.transport == "streamable-http":
                # Fallback to streamable HTTP
                return Response(
                    content=datetime.datetime.now().isoformat(),
                    media_type="text/plain"
                )
            else:
                raise ValueError(f"Unknown transport: {self.transport}")

        @self.app.get("/")
        async def root():
            return {"message": "MCP Server is running"}

    def run(self, host: str = "0.0.0.0", port: int = 8080):
        """Start the server with the configured transport"""
        if self.transport == "sse":
            logger.info("Running server with SSE transport")
        elif self.transport == "streamable-http":
            logger.info("Running server with Streamable HTTP transport")
        else:
            raise ValueError(f"Unknown transport: {self.transport}")

        import uvicorn
        uvicorn.run(self.app, host=host, port=port)

# Convenience function to run the server
def run(transport: str = "sse"):
    server = MCPServer(transport=transport)
    server.run()

# Example usage
if __name__ == "__main__":
    # Run with SSE transport by default
    run(transport="sse")
