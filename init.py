import imp
import os
import time
from src.extras import restore
from src.extras import updater
from src.extras.test import testing_menu

os.system('cls')

while True:
    print("Init Tool for: IsUsbSafe")
    print('\n')
    print("===============================")
    print("| Select an Option to Execute |")
    print("===============================")
    print("| 1. Init IsUsbSafe Tool      |")
    print("| 2. Init Restore Tool        |")
    print("| 3. Init Testing/Error.py    |")
    print("| 4. Update the Tool          |")
    print("| 5. Exit                     |")
    print("| 6. Testing (Dev's Only      |")
    print("===============================")
    print("|  Tool Created by GalionSec  |")
    print("===============================")

    menu_opt = int(input("Select an Option: "))

    if(menu_opt == 1):
        os.system('python ./src/main.py')
        break
    elif(menu_opt == 2):
        restore.start()
        break
    elif(menu_opt == 3):
        os.system('python ./testing/error_gen.py')
        break
    elif(menu_opt == 4):
        updater.init();
    elif(menu_opt == 5):
        print('\n')
        print("Exiting IsUsbSafe...")
        time.sleep(2)
        os.system('cls')
        exit()
    elif(menu_opt == 6):
        print('\n')
        print("Opening Testing Field...")
        time.sleep(1)
        testing_menu.start_menu()
    else:
        print('\n')
        print("The selected option is Unexistant!")
        time.sleep(1)
        os.system('cls')
