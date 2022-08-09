#Restore File by (GalionSec[usr:GXFAnFg])
import os
import sys
import random
import time


def start():
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
            os.rmdir('./config/')
            os.remove('./logs/log.txt')
            os.rmdir('./logs/')
            time.sleep(0.5)
            print("Files Restoring Successful!")
            print("Logs Restored!")
            time.sleep(1)
            print('To continue restoring process execute again the .exe or .py')
            print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
            time.sleep(2)
            os.system('python main.py')
            break
        elif(option == 2):
            print("Option " + option + " was Selected")
            break
        elif(option == 3):
            print("Option " + option + " was Selected")
            break
        elif(option == 4):
            print("Option " + option + " was Selected")
            exit()