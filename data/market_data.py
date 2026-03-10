import requests

def get_crypto_data(coin="bitcoin"):

    url = f"https://api.coingecko.com/api/v3/coins/{coin}"

    response = requests.get(url)
    data = response.json()

    market_data = {
        "price": data["market_data"]["current_price"]["usd"],
        "market_cap": data["market_data"]["market_cap"]["usd"],
        "volume": data["market_data"]["total_volume"]["usd"],
        "github_repos": data["developer_data"]["forks"],
    }

    return market_data
