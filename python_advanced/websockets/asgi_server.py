#!/usr/bin/env python3
"""Serve the browser client and a WebSocket echo endpoint."""

from pathlib import Path

from starlette.applications import Starlette
from starlette.responses import FileResponse, HTMLResponse
from starlette.routing import Route, WebSocketRoute

BASE_DIR = Path(__file__).resolve().parent
ASSETS = {
    "/chat.js": ("chat.js", "text/javascript"),
    "/style.css": ("style.css", "text/css"),
    "/styles.css": ("styles.css", "text/css"),
}


async def homepage(request):
    """Serve the browser client for requests that accept HTML."""
    accept = request.headers.get("accept", "")
    headers = {"Vary": "Accept"}
    if "text/html" in accept:
        return FileResponse(BASE_DIR / "index.html", headers=headers)
    return HTMLResponse("<h1>WebSocket Echo</h1>", headers=headers)


async def asset(request):
    """Serve a script or stylesheet used by the browser client."""
    filename, media_type = ASSETS[request.url.path]
    return FileResponse(BASE_DIR / filename, media_type=media_type)


async def websocket_endpoint(websocket):
    """Echo each text message on the originating connection."""
    await websocket.accept()
    async for message in websocket.iter_text():
        await websocket.send_text(message)


app = Starlette(
    routes=[
        Route("/", homepage),
        Route("/chat.js", asset),
        Route("/style.css", asset),
        Route("/styles.css", asset),
        WebSocketRoute("/ws", websocket_endpoint),
    ],
)
