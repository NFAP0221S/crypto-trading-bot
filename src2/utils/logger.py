# utils/logger.py

import logging
from utils.config import LOG_FILE

def setup_logger():
    logger = logging.getLogger('TradingBot')
    logger.setLevel(logging.DEBUG)

    # 파일 핸들러 설정
    fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(logging.DEBUG)

    # 콘솔 핸들러 설정
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 포맷터 설정
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 핸들러 추가
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

logger = setup_logger()
