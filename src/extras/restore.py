#Restore File by (GalionSec[usr:GXFAnFg])
import os
import sys
import random
import time
from urllib import request
import wget

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
            print('Checking if verif.ius coincides with ')