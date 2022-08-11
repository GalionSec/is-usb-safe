# Is-Usb-Safe
intro = """
Is-Usb-Safe

Author: GalionSec [usr:GXFAnFg]
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
import datetime
from extras import errors
from extras import restore
from extras import logger
from extras.loaders import loaders

#Config File Search
def config():
    os.system('cls')
    print(intro)
    time.sleep(5)
    if(os.path.exists('./src/config/')):
        print('Config Dir Existing')
        print('\n')
        if(os.path.exists('./src/config/general.conf') & os.path.exists('./src/custom/main.ius')):
            start_process()
        else:
            print('Root Config File or Root main.ius is Corrupted or Non Existant!')
            print('Code Error: ' + str(errors.error_list[0])) #Code Error = #rcfcne423 [Check Documentation for more info!]
            print('\n')
            print('Use Restorer.py for restoring all data!')
            go_to_restore = input('You want to execute Restorer.py right now? [y/n]: ')
            if(go_to_restore == "y"):
                os.system('cls')
                loaders.loading_text(name="recov_loader", secs=5, once_complete=restore.start())
            elif(go_to_restore == "n"):
                os.system('cls')
                print('Thanks for using Is-Usb-Safe!')
                exit()
    else:
        path = os.mkdir('./src/config/')
        logs = os.mkdir('./src/logs/')
        custom = os.mkdir('./src/custom/')
        print('Config Path has been created successfuly!')
        conf_path = './src/config/'
        logs_path = './src/logs/'
        customs_path = './src/custom/'

        """
        <--GALION CONNECTION SERVERS-->
            req_key: "REQUEST_KEY"
            username: "USERNAME"
            password: "PASSWORD"
            galion_proxy: "PROXY_NAME"
            using_vpn: FALSE
        <--GALION CONNECTION SERVERS-->
        """

        verif_data_structure = "<--GALION CONNECTION SERVERS-->" + '\n' + 'req_key: "REQUEST_KEY"' + '\n' + "<--GALION CONNECTION SERVERS-->"
        basic_log_structure = "[" + str(datetime.datetime.now().year) + " - " + str(datetime.datetime.now().month) + " - " + str(datetime.datetime.now().day) + "|| " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second) + "] - "

        file_names = ['general.conf', 'log.txt', 'verif.ius', 'main.ius']
        with open(os.path.join(conf_path, file_names[0]), 'w') as file:
            pass
        with open(os.path.join(logs_path, file_names[1]), 'w') as log_file:
            log_file.write(basic_log_structure + "Config Folder Created!" + '\n' + basic_log_structure + "Custom Folder Created!" + '\n' + basic_log_structure + "Logs Folder Created!")
            log_file.close()
        with open(os.path.join(customs_path, file_names[2]), 'w') as verif_file:
            verif_file.write(verif_data_structure)
            verif_file.close()
        with open(os.path.join(customs_path, file_names[3]), 'w') as main_file:
            main_file.write("Author: GalionSec" + '\n' + "Version: 1.0.0" + '\n' + "Key: KEY_GOES HERE")
            main_file.close()
        os.system('cls')
        os.system('python ./src/main.py')
        
def start_process():
    while True:
        print("You wan't to gran't access to IsUsbSafe Admin Privileges?")
        admin_priv_opt = input("[YES/NO]: ")

        if(admin_priv_opt == "y"):
            os.chmod('./src/main.py', 1411)
            print('main.py upgraded the Priviledge')
            time.sleep(1)
            logger.update_log(path='./src/logs/', logger_file_name='log.txt', encode='', content="User Priviledge's were Garanted!")
            logger.update_log(path='./src/logs/', logger_file_name='log.txt', encode='', content="Started the USB Wait Proccess!")
            is_usb_connected = False
            while is_usb_connected == False:
                print("Insert a USB or External Disk to Start the Process -")
                time.sleep(0.3)
                os.system('cls')
                print("Insert a USB or External Disk to Start the Process \\")
                time.sleep(0.3)
                os.system('cls')
                print("Insert a USB or External Disk to Start the Process |")
                time.sleep(0.3)
                os.system('cls')
                print("Insert a USB or External Disk to Start the Process /")
                time.sleep(0.3)
                os.system('cls')
        elif(admin_priv_opt == "n"):
            print("Privileges are needed to use the tool!")
            print("Error Code: " + errors.error_list[1])
            print('\n')
            print("Exiting the tool...")
            time.sleep(3)
            exit()
        elif(admin_priv_opt == "restore"):
            print("Opening Recovery Tool!")
            time.sleep(0.5)
            os.system('cls')
            time.sleep(0.1)
            loaders.loading_text(name="lof", secs=5, once_complete=restore.start())
        else:
            os.system('cls')


config()