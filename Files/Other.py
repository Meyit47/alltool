import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mFree-Proxy  - daha fazla ücretsiz proxy sunucusu")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mIntersect-2.5 - Komut Dosyası Oluşturma Programı")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mExit System  -  alltool dan çıkış")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mBack to menu  -  Ana menüye dön")

op=int(raw_input("OthErTo01s: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && bash Files/Proxy/Logo.sh && python2 Files/Proxy/menu.py && cd")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd Intersect-2.5 && python2 Create.py")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış..")
 sys.exit()
elif(op==4):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/Other.py")



