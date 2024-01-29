#logging functionality
#instead of creating one separate logging folder we can write like this
# just to make import easy

import os
import sys
import logging
#information lavel log or bug level log,which module code is running,shows massage
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#creating logs folder
#inside that running_logs folder
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        #create log folder and inside that save all logging
        logging.FileHandler(log_filepath),
        #to print log
        logging.StreamHandler(sys.stdout)       
    ]
)

logger = logging.getLogger("mlProjectLogger")
