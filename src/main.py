# Is-Usb-Safe
"""
    Author: GalionSec
    Ver: 1.0.0
    Creation Date: 2022-09-08 [Using DMY Date Type]
    Documentation: https://galionsec.github.io/wiki/article/isusbsafe/?page=welcome
"""

#Import modules that we need for the correct work of the code
import os
import sys
import random
import hashlib
import configparser
import time
from extras import errors
from extras import restore

#Config File Search
def config():
    os.system('cls')
    time.sleep(1)
    if(os.path.exists('./config/')):
        print('Config Dir Existing')
        if(os.path.exists('./config/general.conf')):
            start_process()
        else:
            print('Root Config File is Corrupted or Non Existant!')
            print('Code Error: ' + str(errors.error_list[0])) #Code Error = #rcfcne423 [Check Documentation for more info!]
            print('\n')
            print('Use Restorer.py for restoring all data!')
            go_to_restore = input('You want to execute Restorer.py right now? [y/n]: ')
            if(go_to_restore == "y"):
                os.system('cls')
            elif(go_to_restore == "n"):
                os.system('cls')
                print('Thanks for using Is-Usb-Safe!')
                exit()
    else:
        path = os.mkdir('./config/')
        print('Config Path has been created successfuly!')
        conf_path = './config/'
        file_names = ['general.conf', 'log.txt']
        with open(os.path.join(conf_path, file_names[0]), 'w') as file:
            pass

        
def start_process():
    print('Process Started!')


config()