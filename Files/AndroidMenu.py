import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mPyshell - Uzaktan Erişim Truva Atı - RAT")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mWishfish - Bir Bağlantı Kullanarak Ön Kamera Fotoğrafını Yakalamak İçin Güçlü Araç")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mLockPhish - Kilit ekranında kimlik avı saldırılarına yönelik araç")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mLockPhish - Kilit ekranında kimlik avı saldırılarına yönelik araç")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mExit System - alltool dan çıkış")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("R6moteTRo1anR8t: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd pyshell && ./Pyshell && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd wishfish && ./wishfish.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd lockphish && bash lockphish.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd alltool && cd Files && bash HatCloud.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==5):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 sys.exit()
elif(op==6):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/AndroidMenu.py")
