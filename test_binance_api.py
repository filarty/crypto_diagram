import asyncio

from BinanceApi import BinanceApi

api = BinanceApi(symbol='LRCBTC')

async def main():
    await api.get_thread()



if __name__ == "__main__":
    asyncio.run(main())