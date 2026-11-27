#!/usr/bin/env python3
"""Validate incoming WebSocket text messages."""

import asyncio

import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Validate each text message and reply on the same connection."""
    try:
        async for message in websocket:
            if not isinstance(message, str):
                continue

            if not message.strip():
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        return


async def main():
    """Run the validation server on the IPv4 loopback address."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
