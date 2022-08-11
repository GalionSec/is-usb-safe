import time
import os
import hashlib


def loading_text(name, secs, once_complete):
    hashlib.md5(name).digest()
    for i in range(secs):
                print("L")
                time.sleep(0.5)
                os.system('cls')
                print("LO")
                time.sleep(0.5)
                os.system('cls')
                print("LOA")
                time.sleep(0.5)
                os.system('cls')
                print("LOAD")
                time.sleep(0.5)
                os.system('cls')
                print("LOADI")
                time.sleep(0.5)
                os.system('cls')
                print("LOADIN")
                time.sleep(0.5)
                os.system('cls')
                print("LOADING")
                time.sleep(0.3)
                os.system('cls')
                print("LOADING.")
                time.sleep(0.3)
                os.system('cls')
                print("LOADING..")
                time.sleep(0.5)
                os.system('cls')
                print("LOADING...")
                i = i + 1
                time.sleep(0.5)
                os.system('cls')
                if(i == 5):
                    once_complete
                    break