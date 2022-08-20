import asyncio
import json
import websockets

class BinanceApi:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol
    
    async def get_thread(self) -> json:
        async with websockets.connect(f'wss://stream.binance.com:9443/stream?streams={self.symbol.lower()}@miniTicker') as websocket:
            while True:
                print(await websocket.recv())

