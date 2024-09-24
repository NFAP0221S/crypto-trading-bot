# utils/config.py

import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
UPBIT_ACCESS_KEY = os.getenv("UPBIT_ACCESS_KEY")
UPBIT_SECRET_KEY = os.getenv("UPBIT_SECRET_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# Trading Configurations
TRADE_CONFIG = {
    'base_currency': 'KRW',
    'trade_currency': 'BTC',
    'investment_ratio': 0.1,  # 투자 비율 (자산의 10%)
    'min_trade_amount': 5000,  # 최소 거래 금액
    'trade_times': ["00:01", "08:01", "16:01"]  # 거래 실행 시간
}

# Database Configurations
DB_PATH = 'trading_bot.sqlite'

# Logging Configurations
LOG_FILE = 'trading_bot.log'

# Scheduler Configurations
SCHEDULE_INTERVAL = 1  # 초 단위로 스케줄러를 실행할 주기

# Other Configurations
CHROME_DRIVER_PATH = '/usr/local/bin/chromedriver'
