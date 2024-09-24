# data/sentiment_fetcher.py

import requests
from utils.logger import logger

def fetch_fear_and_greed_index():
    url = "https://api.alternative.me/fng/"
    try:
        response = requests.get(url)
        data = response.json().get('data', [])
        logger.info("Fear and Greed Index fetched")
        return data
    except Exception as e:
        logger.error(f"Failed to fetch Fear and Greed Index: {e}")
        return []
