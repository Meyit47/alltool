import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mDarkDump - Deep web de Arama yap.")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mSistemden çıkış")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("DarkSearch: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && python2 Files/DarkDump.py && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 sys.exit()
elif(op==3):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/DarkSearchMenu.py")
