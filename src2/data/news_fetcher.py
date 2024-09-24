# data/news_fetcher.py

import requests
from utils.config import SERPAPI_API_KEY
from utils.logger import logger

def fetch_news_data(query="bitcoin"):
    url = f"https://serpapi.com/search.json?engine=google_news&q={query}&api_key={SERPAPI_API_KEY}"
    try:
        response = requests.get(url)
        news_results = response.json().get('news_results', [])
        simplified_news = []
        for news in news_results:
            title = news.get('title')
            source = news.get('source', {}).get('name')
            date = news.get('date')
            simplified_news.append({'title': title, 'source': source, 'date': date})
        logger.info(f"Fetched {len(simplified_news)} news articles")
        return simplified_news
    except Exception as e:
        logger.error(f"Failed to fetch news data: {e}")
        return []
