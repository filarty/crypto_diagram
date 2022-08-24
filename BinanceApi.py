import asyncio

import json

import websockets

import time

from Diagramm import Diagramm

from threading import Thread

class BinanceDiagramm:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol
        self.diagramm = Diagramm()
        self.loop = asyncio.get_event_loop()
    
    async def main(self) -> json:
        async with websockets.connect(f'wss://stream.binance.com:9443/stream?streams={self.symbol.lower()}@miniTicker', ) as websocket:
            while True:
                data = json.loads(await websocket.recv())['data']
                event_time = time.localtime(data["E"] // 1000)
                event_time = f"{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec}"
                self.diagramm.x_time = event_time
                self.diagramm.y_price = float(data['c'])
                
    
    def run(self) -> None:
        self.loop.run_until_complete(self.main())

    def view(self) -> None:
        t1 = Thread(target=self.run, daemon=True)
        t1.start()
        self.diagramm.update()

if __name__ == "__main__":
    binance = BinanceDiagramm("ETHBTC")
    t1 = Thread(target=binance.run, daemon=True)
    t1.start()
    binance.view()