#!/usr/bin/env python3
"""Run a WebSocket server that echoes text messages."""

import asyncio

import websockets


async def connection_handler(websocket):
    """Echo each text message to the client that sent it."""
    async for message in websocket:
        if isinstance(message, str):
            await websocket.send(message)


async def main():
    """Listen for WebSocket connections on the IPv4 loopback address."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
