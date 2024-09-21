# agent.py - AI 트레이딩 봇의 핵심 로직
from strategies.strategy import make_decision
from strategies.sentiment_analysis import fetch_fear_greed_index
from utils.data_fetcher import fetch_upbit_data
from utils.indicator import calculate_rsi

def run_trading_bot():
    """
    실시간 데이터를 가져와서 트레이딩 전략을 실행하는 함수.
    """
    # 실시간 데이터 가져오기
    market_data = fetch_upbit_data()
    
    # 보조 지표 계산 (RSI 등)
    rsi_value = calculate_rsi(market_data['trade_price'])
    indicators = {'RSI': rsi_value}
    
    # 시장 심리 분석 (공포 탐욕 지수)
    fear_greed_value, sentiment_classification = fetch_fear_greed_index()
    sentiment = {'fear_greed_index': fear_greed_value, 'classification': sentiment_classification}
    
    # 트레이딩 결정 내리기
    decision = make_decision(market_data, indicators, sentiment)
    
    # 트레이딩 기록 저장
    log_trade(decision, market_data)
    
    print(f"트레이딩 결정: {decision}")

def log_trade(decision, market_data):
    """
    트레이딩 기록을 저장하는 함수.
    """
    with open('data/trading_records/trade_log.json', 'a') as f:
        log_data = {
            "decision": decision,
            "price": market_data['trade_price'],
            "volume": market_data['acc_trade_volume'],
            "timestamp": market_data['timestamp']
        }
        f.write(json.dumps(log_data) + '\n')
