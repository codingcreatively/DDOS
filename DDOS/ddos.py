import os,sys
import time
import random
from platform import system
import time
VER = 2

try:
    if sys.version_info >= (3,0):
        VER = 3
        from urllib.request import urlopen
        from urllib.error import URLError
    else:
        input = raw_input
        from urllib2 import urlopen
        from urllib2 import URLError
except:
        pass

def clearScr():
    os.system('clear')

def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

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

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
luc = input("DDOS@ALEXXX:~# ")
clearScr()
class choices():

	def ddos(self):
		if system() == 'Linux':
			os.system("cd files/ddos && chmod +x ddos.py && python3 ddos.py")
		if system() == 'Windows':
			os.system('cd files/ddos && ddos.py')
		

	def exitluc(self):
		print('\033[97m\nClosing Lucille\nPlease Wait...\033[1;m')
		time.sleep(2)
		sys.exit()

ch = choices()
if luc == '1':
	ch.ddos()
else:
	print("Invalid Input!")
	

    


    
 

