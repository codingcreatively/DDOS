import os
import sys
import time
import random
from platform import system

def clearScr():
    os.system('clear')

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝																		
Note! : I'm Not Responsible for any illegal usage.
Coded by : Alexxx
Instagram: arcane.__01


[+] 1. DDOS Tools
			                  """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)						  
        
clearScr()
logo()

luc = input("DDOS@ALEXXX:~# ")
clearScr()

class choices():
    def ddos(self):
        if system() == 'Linux':
            os.system("cd files/ddos && chmod +x ddos.py && python3 ddos.py")
        elif system() == 'Windows':
            os.system('cd files\\ddos && python ddos.py')
        else:
            print("Unsupported OS!")
    
    def exitluc(self):
        print('\033[97m\nClosing Lucille\nPlease Wait...\033[1;m')
        time.sleep(2)
        sys.exit()

ch = choices()
if luc == '1':
    ch.ddos()
elif luc.lower() in ['exit', 'quit', 'q']:
    ch.exitluc()
else:
    print("Invalid Input!")