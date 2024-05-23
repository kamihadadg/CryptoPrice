import requests

url = "https://min-api.cryptocompare.com/data/pricemultifull"
params = {
    "fsyms": "BTC,ETH,XRP",  # نماد توکن‌ها را با کاما جدا کنید
    "tsyms": "USD"
}

response = requests.get(url, params=params)
data = response.json()["RAW"]

for symbol in data:
    coin = data[symbol]["USD"]
    print(f"{symbol}")
    print(f"  Price: ${coin['PRICE']}")
    print(f"  Market Cap: ${coin['MKTCAP']}")
    print(f"  24h Volume: ${coin['TOTALVOLUME24H']}")
    print(f"  24h High: ${coin['HIGH24HOUR']}")
    print(f"  24h Low: ${coin['LOW24HOUR']}")
    print(f"  Price Change 24h: ${coin['CHANGE24HOUR']}")
    print(f"  Price Change Percentage 24h: {coin['CHANGEPCT24HOUR']}%\n")
