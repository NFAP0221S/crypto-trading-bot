# trading/db_manager.py

import sqlite3
from utils.config import DB_PATH
from utils.logger import logger

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS decisions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            decision TEXT,
            percentage REAL,
            reason TEXT,
            btc_balance REAL,
            krw_balance REAL,
            btc_avg_buy_price REAL,
            btc_current_price REAL
        );
        '''
        self.conn.execute(query)
        self.conn.commit()
        logger.info("Database table initialized")

    def save_decision(self, decision_data, asset_status):
        query = '''
        INSERT INTO decisions (decision, percentage, reason, btc_balance, krw_balance, btc_avg_buy_price, btc_current_price)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        data = (
            decision_data.get('decision'),
            decision_data.get('percentage'),
            decision_data.get('reason'),
            asset_status.get('btc_balance'),
            asset_status.get('krw_balance'),
            asset_status.get('btc_avg_buy_price'),
            asset_status.get('btc_current_price')
        )
        self.conn.execute(query, data)
        self.conn.commit()
        logger.info("Decision saved to database")

    def fetch_recent_decisions(self, limit=10):
        query = '''
        SELECT * FROM decisions ORDER BY timestamp DESC LIMIT ?
        '''
        cursor = self.conn.execute(query, (limit,))
        rows = cursor.fetchall()
        decisions = []
        for row in rows:
            decision = {
                'timestamp': row[1],
                'decision': row[2],
                'percentage': row[3],
                'reason': row[4],
                'btc_balance': row[5],
                'krw_balance': row[6],
                'btc_avg_buy_price': row[7],
                'btc_current_price': row[8]
            }
            decisions.append(decision)
        logger.info(f"Fetched {len(decisions)} recent decisions")
        return decisions

    def close(self):
        self.conn.close()
        logger.info("Database connection closed")
