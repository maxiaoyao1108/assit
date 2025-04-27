import requests
from config.config import API_KEY


def collect_market_data():
    try:
        url = f'https://example-market-api.com/data?api_key={API_KEY}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error collecting market data: {e}")
        return None

    