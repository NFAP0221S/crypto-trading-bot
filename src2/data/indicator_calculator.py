# data/indicator_calculator.py

import pandas_ta as ta
from utils.logger import logger

def add_indicators(df):
    try:
        # 이동 평균선
        df['SMA_10'] = ta.sma(df['close'], length=10)
        df['EMA_10'] = ta.ema(df['close'], length=10)
        # RSI
        df['RSI_14'] = ta.rsi(df['close'], length=14)
        # MACD
        macd = ta.macd(df['close'])
        df = df.join(macd)
        # Bollinger Bands
        bb = ta.bbands(df['close'])
        df = df.join(bb)
        # 기타 지표 추가 가능
        logger.info("Indicators added to dataframe")
        return df
    except Exception as e:
        logger.error(f"Failed to add indicators: {e}")
        return df
