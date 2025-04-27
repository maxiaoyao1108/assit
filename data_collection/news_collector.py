import requests
from config.config import API_KEY


def collect_news_data():
    try:
        url = f'https://example-news-api.com/data?api_key={API_KEY}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error collecting news data: {e}")
        return None

    