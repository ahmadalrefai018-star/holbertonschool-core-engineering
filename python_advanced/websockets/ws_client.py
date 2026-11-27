#!/usr/bin/env python3
"""Send one message to a WebSocket server and receive its reply."""

import asyncio

import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Send text once and return the server's reply."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        return await websocket.recv()


async def main():
    """Send the required message and print the reply exactly."""
    response = await connect_and_send("ws://localhost:8765", "Hello WebSocket")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
