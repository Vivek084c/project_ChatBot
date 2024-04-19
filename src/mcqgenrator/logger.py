# import logging
# import os 
# from datetime import datetime

# #creating a logger file- the use of this file is to understand when we have executed out pipeline
# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# #path to store the log file 
# # os.chdir("d:\\work\\projects\\project_ChatBot")
# log_path=os.path.join(os.getcwd(),"logs")
# os.makedirs(log_path, exist_ok=True)

# #creating the log file inside this directory
# LOG_FILEPATH=os.path.join(log_path,LOG_FILE)
# logging.basicConfig(
#     level=logging.INFO,
#     filename=LOG_FILEPATH,
#     format="[%(asctime)s] %(lineon)d %(name)s - %(levelname)s - %(message)e"
# )
import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs")

os.makedirs(log_path,exist_ok=True)


LOG_FILEPATH=os.path.join(log_path,LOG_FILE)


logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)