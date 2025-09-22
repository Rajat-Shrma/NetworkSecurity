import os 
import logging
from datetime import datetime
logs_folder_path=os.path.join(os.getcwd(),'logs')

os.makedirs(logs_folder_path,exist_ok=True)

LOG_FILE_NAME=f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

LOG_FILE_PATH=os.path.join(logs_folder_path,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | Line: %(lineno)d | Message: %(message)s'
)


