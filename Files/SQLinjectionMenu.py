import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mVirusInjection - /sdcard/ a virüs oluştur.")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mDebinject - Kötü amaçlı kodu enjekte edin *.debs")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mInfect - Windows, android için virüs oluşturma")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mSistemden çıkış")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("Iject1onTo0l: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd Vitus2.0 && cp VirtualXposed.apk /sdcard/")
 print("Virüsünüz oluşturuldu!")
 time.sleep(1)
 print("Virüsünüzü /sdcard/'da bulun")
 time.sleep(2)
 os.system("cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd Debinject && python2 debinject.py && cd && cd alltool && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd Infect && Infect && cd && cd alltool && python2 MainMenu.py")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
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
 os.system("python2 Files/SQLinjectionMenu.py")
