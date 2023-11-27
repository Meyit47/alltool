import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mTGarama - Telegram kullanıcı bilgileri")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mLyzen - Discord Leak kullanıcıları ")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mAna menüye dön")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mSistemden çıkış")

op=int(raw_input("D1sc0Rd: "))

if(op==1):
 print("Siteye gidin ve sitede listelenen her şeyi girin")
 print("website: https://lyzem.com/")
 os.system("cd && cd alltool && python src/Timer1.py && python2 MainMenu.py")
elif(op==2):
 print("Siteye gidin ve sitede listelenen her şeyi girin")
 print("website: https://search.buzz.im")
 os.system("cd && cd alltool && python src/Timer1.py && python2 MainMenu.py")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden Çıkış...")
 sys.exit()
elif(op==4):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş. Araçlar Yeniden Yüklenmeli") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/telegramMenu.py")
