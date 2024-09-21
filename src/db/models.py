# models.py - DB 모델 정의 (SQLAlchemy 사용)
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class TradeLog(Base):
    __tablename__ = 'trade_logs'

    id = Column(Integer, primary_key=True)
    decision = Column(String)
    price = Column(Float)
    volume = Column(Float)
    timestamp = Column(DateTime)

# 데이터베이스 연결 설정
engine = create_engine('sqlite:///trading_bot.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
