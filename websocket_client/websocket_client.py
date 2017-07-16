#!/usr/bin/env python3

import asyncio
import websockets

class websocket:
    """
    Super simple websocket client. Not efficient since it creates a new connection each time. Also, it's all symmetric.

    Use:
    from websocket_client import websocket
    ws = websocket("ws://192.168.1.1/test")
    ws.send("Hello!")
    """

    def __init__(self, address):
        """address is something like "ws://<ip>/file" """
        self.address = address

    async def _do_send(self):
        async with websockets.connect(self.address) as ws:
            await ws.send(self.s)
            return await ws.recv()

    def send(self, s):
        self.s = s
        return asyncio.get_event_loop().run_until_complete(self._do_send())

def shell():
    address = input("Enter full url (i.e.: ws://<ip>/path): ")

    ws = websocket(address)

    while True:
        cmd = input("> ")
        print(ws.send(cmd))


# Default to a minimal shell if we call this directly
if __name__ == "__main__":
    shell()
