import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum,ripple"  # نام توکن‌ها را با کاما جدا کنید
}

response = requests.get(url, params=params)
data = response.json()

for coin in data:
    print(f"{coin['name']} ({coin['symbol']})")
    print(f"  Price: ${coin['current_price']}")
    print(f"  Market Cap: ${coin['market_cap']}")
    print(f"  24h Volume: ${coin['total_volume']}")
    print(f"  24h High: ${coin['high_24h']}")
    print(f"  24h Low: ${coin['low_24h']}")
    print(f"  Price Change 24h: ${coin['price_change_24h']}")
    print(f"  Price Change Percentage 24h: {coin['price_change_percentage_24h']}%\n")
