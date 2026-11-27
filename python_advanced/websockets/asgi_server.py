#!/usr/bin/env python3
"""Serve an HTML page and a WebSocket echo endpoint."""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    """Return the required HTML heading."""
    return HTMLResponse("<h1>WebSocket Echo</h1>")


async def websocket_endpoint(websocket):
    """Echo text messages for the lifetime of the connection."""
    await websocket.accept()
    async for message in websocket.iter_text():
        await websocket.send_text(message)


app = Starlette(
    routes=[
        Route("/", homepage),
        WebSocketRoute("/ws", websocket_endpoint),
    ],
)
