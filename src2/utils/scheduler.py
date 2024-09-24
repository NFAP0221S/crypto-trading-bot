# utils/scheduler.py

import schedule
import time
from threading import Thread
from utils.config import TRADE_CONFIG, SCHEDULE_INTERVAL
from utils.logger import logger

def run_schedule(task_function):
    for trade_time in TRADE_CONFIG['trade_times']:
        schedule.every().day.at(trade_time).do(task_function)
        logger.info(f"Scheduled task at {trade_time}")

    while True:
        schedule.run_pending()
        time.sleep(SCHEDULE_INTERVAL)

def start_scheduler(task_function):
    scheduler_thread = Thread(target=run_schedule, args=(task_function,))
    scheduler_thread.start()
    logger.info("Scheduler started")
