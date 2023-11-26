import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool")
os.system("bash Logo.sh")
os.system("bash src/MenuA.sh")

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

op=int(raw_input("Seçenekler: "))

if(op==1):
 os.system("cd")
 os.system("cd alltool && bash src/Inf.sh")
 os.system("python2 MainMenu.py")
elif(op==2):
 print("\033[1;31;40m-Sistem yeniden başlatılıyor...")
 time.sleep(0.7)
 os.system("cd")
 os.system("cd alltool")
 os.system("bash src/alltool.sh")
elif(op==3):
 print("\033[1;31;40m-Sistemden çıkış...")
 time.sleep(1)
 sys.exit()
else:
 print("\033[1;31;40mGeçersiz Giriş. Ana menüye dön...")
 time.sleep(1)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
 
