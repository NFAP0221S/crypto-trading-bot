# main.py

from data.data_fetcher import fetch_market_data
from data.indicator_calculator import add_indicators
from data.news_fetcher import fetch_news_data
from data.sentiment_fetcher import fetch_fear_and_greed_index
from utils.image_capturer import capture_chart_image
from models.gpt_analyzer import analyze_with_gpt
from models.instructions import instructions
from trading.trade_executor import TradeExecutor
from trading.db_manager import DBManager
from utils.scheduler import start_scheduler
from utils.logger import logger

def get_asset_status(upbit):
    btc_balance = upbit.get_balance("BTC")
    krw_balance = upbit.get_balance("KRW")
    btc_avg_buy_price = upbit.get_avg_buy_price("BTC")
    btc_current_price = upbit.get_current_price("KRW-BTC")
    return {
        'btc_balance': btc_balance,
        'krw_balance': krw_balance,
        'btc_avg_buy_price': btc_avg_buy_price,
        'btc_current_price': btc_current_price
    }

def make_decision():
    logger.info("Starting decision-making process")

    # 데이터 수집
    market_data = fetch_market_data()
    if market_data is None:
        return
    market_data = add_indicators(market_data)
    market_data_str = market_data.tail(100).to_json()

    # 뉴스 데이터
    news_data = fetch_news_data()

    # 공포와 탐욕 지수
    sentiment_data = fetch_fear_and_greed_index()

    # 차트 이미지
    chart_image_base64 = capture_chart_image()

    # 자산 현황
    trade_executor = TradeExecutor()
    asset_status = get_asset_status(trade_executor.upbit)

    # 과거 거래 결정 내역
    db_manager = DBManager()
    recent_decisions = db_manager.fetch_recent_decisions()

    # GPT 분석
    user_prompts = [
        f"Market Data:\n{market_data_str}",
        f"News Data:\n{news_data}",
        f"Sentiment Data:\n{sentiment_data}",
        f"Asset Status:\n{asset_status}",
        f"Recent Decisions:\n{recent_decisions}",
        f"Chart Image (Base64):\n{chart_image_base64}"
    ]

    advice = analyze_with_gpt(instructions, user_prompts)
    if advice is None:
        return

    # JSON 파싱
    try:
        import json
        decision_data = json.loads(advice)
        logger.info(f"Received decision: {decision_data}")
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse GPT response: {e}")
        return

    # 거래 실행
    trade_executor.execute_trade(decision_data['decision'], decision_data['percentage'])

    # 거래 내역 저장
    db_manager.save_decision(decision_data, asset_status)

    # 데이터베이스 연결 종료
    db_manager.close()

if __name__ == "__main__":
    start_scheduler(make_decision)
