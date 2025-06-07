import sys
import os

# Add src/extract/daily to sys.path so Python can find daily_update.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/extract/daily')))

from apscheduler.schedulers.blocking import BlockingScheduler
from daily_update import fetch_and_update

def job():
    fetch_and_update()

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', hour=6, minute=0)
    print("APScheduler started. Waiting for 6:00 AM daily run...")
    scheduler.start()