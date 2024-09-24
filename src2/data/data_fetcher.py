# data/data_fetcher.py

import pyupbit
import pandas as pd
from utils.logger import logger

def fetch_market_data(ticker="KRW-BTC", interval="minute60", count=200):
    try:
        df = pyupbit.get_ohlcv(ticker, interval=interval, count=count)
        logger.info(f"Market data fetched: {len(df)} rows")
        return df
    except Exception as e:
        logger.error(f"Failed to fetch market data: {e}")
        return None
