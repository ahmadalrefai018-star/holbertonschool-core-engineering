#!/usr/bin/env python3
"""Broadcast WebSocket text messages to all connected clients."""

import asyncio

import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Track this connection and broadcast each incoming text message."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            if not isinstance(message, str):
                continue

            for client in connected_clients.copy():
                try:
                    await client.send(f"B:{message}")
                except ConnectionClosed:
                    connected_clients.discard(client)
    finally:
        connected_clients.discard(websocket)


async def main():
    """Run the broadcast server on the IPv4 loopback address."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
