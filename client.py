import asyncio
import websockets

clients = set()

async def handler(websocket):
    clients.add(websocket)
    print(f"[JOIN] Users: {len(clients)}")

    try:
        async for message in websocket:
            # broadcast to all connected users
            dead = set()

            for client in clients:
                try:
                    await client.send(message)
                except:
                    dead.add(client)

            for d in dead:
                clients.remove(d)

    finally:
        clients.remove(websocket)
        print(f"[LEAVE] Users: {len(clients)}")

async def main():
    print("[SERVER] ws://0.0.0.0:8765 running")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()

asyncio.run(main())
