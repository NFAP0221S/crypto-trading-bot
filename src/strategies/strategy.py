# strategy.py - 기본 트레이딩 전략
import json

def make_decision(market_data, indicators, sentiment):
    """
    트레이딩 결정 로직. RSI, 가격 추세, 시장 심리를 기반으로 매수, 매도 또는 보류를 결정합니다.
    """
    decision = None
    reason = None
    
    # RSI를 기준으로 매매 결정
    if indicators['RSI'] < 30:
        decision = "buy"
        reason = "RSI가 과매도 상태를 나타냅니다."
    elif indicators['RSI'] > 70:
        decision = "sell"
        reason = "RSI가 과매수 상태를 나타냅니다."
    else:
        decision = "hold"
        reason = "뚜렷한 매매 신호가 없습니다."
    
    return json.dumps({
        "decision": decision,
        "reason": reason
    })
