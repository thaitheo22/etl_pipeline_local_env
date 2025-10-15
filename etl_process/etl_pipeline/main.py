import pandas as pd 

import time, schedule, threading
etl_lock = threading.Lock()
#-------------------------------------
import logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#-------------------------------------
from run_etl import process_config



def main():
    logging.info("ETL job triggered.")
    try:
        if etl_lock.acquire(blocking=False):
            try:
                process_config()
                logging.info("ETL job completed successfully.")
            except Exception as e:
                logging.error(f"ETL job failed: {e}")
            finally:
                etl_lock.release()
        else:
            logging.warning("ETL job skipped because another instance is running.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        





if __name__ == "__main__":
    schedule.every(10).seconds.do(main)
    
    while True:    
        schedule.run_pending()
        time.sleep(1)
    
    