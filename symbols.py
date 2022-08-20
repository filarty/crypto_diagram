import requests

URL = "https://api.binance.com/api/v3/exchangeInfo"
response = requests.get(URL)
symbols = [i["symbol"] for i in response.json()["symbols"]]
print(symbols)