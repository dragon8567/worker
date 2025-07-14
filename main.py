import asyncio
import websockets

PORT = 8080

async def echo(websocket, path):
    print(f"🔌 Connection from {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"📩 Received: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.exceptions.ConnectionClosed:
        print(f"❌ Disconnected from {websocket.remote_address}")

start_server = websockets.serve(echo, "0.0.0.0", PORT)

print(f"🚀 WebSocket server running on ws://0.0.0.0:{PORT}")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
