import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mXSSCon - Basit XSS Tarayıcı aracı")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mXanXSS - Basit bir XSS bulma aracı")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mXSStrike - En gelişmiş XSS tarayıcı")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mSistemden çıkış - alltool dan çıkış yap")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("XSSattACk: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd Files && bash XSScon.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd Files && bash XanXSS.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd Files && bash XSStrike.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden Çıkış...")
 sys.exit()
elif(op==5):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/AnalistickMenu.py")
