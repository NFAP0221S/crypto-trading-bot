# trading/trade_executor.py

import pyupbit
from utils.config import UPBIT_ACCESS_KEY, UPBIT_SECRET_KEY, TRADE_CONFIG
from utils.logger import logger

class TradeExecutor:
    def __init__(self):
        self.upbit = pyupbit.Upbit(UPBIT_ACCESS_KEY, UPBIT_SECRET_KEY)
        self.ticker = f"{TRADE_CONFIG['base_currency']}-{TRADE_CONFIG['trade_currency']}"

    def execute_trade(self, decision, percentage):
        if decision == "buy":
            self.buy(percentage)
        elif decision == "sell":
            self.sell(percentage)
        else:
            logger.info("No trade executed (hold)")

    def buy(self, percentage):
        krw_balance = self.upbit.get_balance("KRW")
        amount_to_invest = krw_balance * (percentage / 100)
        if amount_to_invest >= TRADE_CONFIG['min_trade_amount']:
            result = self.upbit.buy_market_order(self.ticker, amount_to_invest)
            logger.info(f"Buy order executed: {result}")
        else:
            logger.warning("Insufficient funds to execute buy order")

    def sell(self, percentage):
        coin_balance = self.upbit.get_balance(TRADE_CONFIG['trade_currency'])
        amount_to_sell = coin_balance * (percentage / 100)
        current_price = pyupbit.get_current_price(self.ticker)
        if current_price * amount_to_sell >= TRADE_CONFIG['min_trade_amount']:
            result = self.upbit.sell_market_order(self.ticker, amount_to_sell)
            logger.info(f"Sell order executed: {result}")
        else:
            logger.warning("Insufficient coin balance to execute sell order")
