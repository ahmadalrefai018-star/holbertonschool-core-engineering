#!/usr/bin/env python3
"""Send WebSocket replies only to the client that sent the message."""

import asyncio

import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Track the connection and reply to its text messages."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            if isinstance(message, str):
                await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Run the unicast server on the IPv4 loopback address."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
