import time
import os

directory = os.getcwd()

def option_1():
    os.mkdir(option1)
    os.chdir(option1)
    content()

def option_2():
    os.mkdir(option2a + ' - ' + opinio2b)
    os.chdir(option2a + ' - ' + opinio2b)
    content()

def content():
    os.mkdir ('Textures')
    os.mkdir ('Exports')
    os.mkdir ('Images')
    os.mkdir ('Documents')
    os.mkdir ('Alphas')
    os.mkdir ('Renders')

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

logo = """
  _____           _           _     __  __                                     ____  _____  
 |  __ \         (_)         | |   |  \/  |                                   |___ \|  __ \ 
 | |__) | __ ___  _  ___  ___| |_  | \  / | __ _ _ __   __ _  __ _  ___ _ __    __) | |  | |
 |  ___/ '__/ _ \| |/ _ \/ __| __| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|  |__ <| |  | |
 | |   | | | (_) | |  __/ (__| |_  | |  | | (_| | | | | (_| | (_| |  __/ |     ___) | |__| |
 |_|   |_|  \___/| |\___|\___|\__| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|    |____/|_____/ 
                _/ |                                          __/ |                         
               |__/                                          |___/                          
"""

while True:
    print (logo)
    print ('To whom this shall be done? Me/Someone: ')

    whom = input()

    whom = whom.lower()

    if whom == 'me':
        clearConsole()
        print ('What shall be done?: ')
        option1 = input()
        option_1()
        break

    elif whom == 'someone':
        clearConsole()
        print ('Who Poor soul has offered their soul for such service?: ')
        option2a = input()
        clearConsole()
        print ('What Shall be done?: ')
        opinio2b = input()
        option_2()
        break

    else:
        clearConsole()
        print('You mere mortal not understand these simplest rules? Try again!')
        time.sleep(2)
        clearConsole()
        continue


