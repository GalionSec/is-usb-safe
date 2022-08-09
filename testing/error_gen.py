#This programm ereases files within the code! [Use under own risk (And is for debugin)]
import os
import time
import sys

os.system('cls')

while True:

    print("========================")
    print("|Select a Error to send|")
    print("========================")
    print("| 1. Config Files      |")
    print("| 2. Custom Files      |")
    print("| 3. Inyect Custom Code|")
    print("| 4. Exit              |")
    print("========================")

    sel_error = int(input('Insert the Error Number: '))

    if(sel_error == 1):
        print("Error Selected: Config")
        time.sleep(1)
        for f in os.listdir('./src/config/'):
            os.remove(os.path.join('./src/config/', f))
        print('Error Sended! Restarting the program!')
        os.system('python ./src/main.py')
        break
    elif(sel_error == 2):
        print("Error Selected: Custom")
        break
    elif(sel_error == 3):
        print("Error Selected: Inyect")
        break
    elif(sel_error == 4):
        print('\n' + "Exiting Error Generator...")
        time.sleep(2)
        os.system('cls')
        exit()
    else:
        print('Non Existant Option!')
        time.sleep(2)
        os.system('cls')