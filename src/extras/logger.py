#Logger Module by: GalionSec [usr:GXFAnFg]
import os
import datetime

def update_log(path, logger_file_name, encode, content):

    log_structure = "[" + str(datetime.datetime.now().year) + " - " + str(datetime.datetime.now().month) + " - " + str(datetime.datetime.now().day) + "|| " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second) + "] - " + content

    with open(os.path.join(path, logger_file_name), 'a') as log_file:
        log_file.write('\n' + log_structure)
        log_file.close()