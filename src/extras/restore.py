#Restore File by (GalionSec[usr:GXFAnFg])
import os
import sys
import random
import time
from urllib import request
import wget

#Relases URL
rel_url = "https://galionsec.github.io/is-usb-safe/download/releases/?v=latest"

def start():

    os.system('cls')

    print("Welcome to IsUsbSafe Restore Tool!")
    print("==================================")
    time.sleep(0.3)
    print("1. Check all the Program Files")
    print("2. Update the tool!")
    print("3. Clear Cache")
    print("4. Exit")
    while True:
        option = int(input('What You Want To Do?: '))
        
        if(option == 1):
            print("Option " + str(option) + " was Selected")
            time.sleep(0.5)
            for f in os.listdir('./src/config/'):
                os.remove(os.path.join('./src/config/', f))
            os.rmdir('./src/config/')
            for f in os.listdir('./src/logs/'):
                os.remove(os.path.join('./src/logs/', f))
            os.rmdir('./src/logs/')
            for f in os.listdir('./src/custom/'):
                os.remove(os.path.join('./src/custom/', f))
            os.rmdir('./src/custom/')
            time.sleep(0.5)
            print("Config Files Restored!")
            print("Logs Restored!")
            print("Custom Files Restored!")
            time.sleep(2)
            print('Re-Executing IsUsbSafe! (This will create all important files again)')
            print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
            time.sleep(2)
            os.system('python ./src/main.py')
            break
        elif(option == 2):
            print("Option " + str(option) + " was Selected!")
            time.sleep(0.5)
            print("Starting Update Tool...")
            time.sleep(0.5)
            print('Connection to GalionSec Servers [PENDING VERIFICATION]')
            time.sleep(1)
            print('Checking if verif.ius coincides with SERVER_CONNECTION_TOKENS')
            time.sleep(1)
            print("Connecting to: " + rel_url)
        elif(option == 3):
            if(os.path.exists('./src/chache/')):
                print("Clear Cache")
                break
            else:
                print("Cache Folder and Files are Unexistant!")
                print("Returning to the tool!")
                time.sleep(1)
                os.system('cls')
                os.system('python ./src/main.py')
                break
        elif(option == 4):
            os.system('cls')
            print("=========================")
            print("Select a whay of exiting!")
            print("=========================")
            print("| 1. Exit to App        |")
            print("| 2. Exit the App       |")
            print("=========================")
            print('\n')
            while True:
                exit_opt = int(input("Select an Option: "))
                if(exit_opt == 1):
                    print("ReBooting App...")
                    time.sleep(2)
                    os.system('python ./init.py')
                    break
                elif(exit_opt == 2):
                    print("Exiting the App...")
                    time.sleep(2)
                    os.system('cls')
                    exit() 