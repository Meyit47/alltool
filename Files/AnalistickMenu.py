import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mAstraNmap - Bir bilgisayar ağındaki ana bilgisayarları ve hizmetleri bulmak için kullanılan güvenlik tarayıcısı")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mRed Hawk - Bilgi Toplama, Güvenlik Açığı Taraması ve Tarama")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mWeeman - Python'da kimlik avı için HTTP sunucusu")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mTM-scanner - termux için web siteleri güvenlik açığı tarayıcısı")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mRang3r - Çok Konulu IP + Bağlantı Noktası Tarayıcı")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mSqlmap - Otomatik SQL enjeksiyonu ve veritabanı devralma aracı")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mMaxSubdoFinder - Alt Alan Adını Keşfetme Aracı")
print("  \033[1;34m[ 08 ] >> \033[1;36;40mEasymap - Nmap Kısayolu")
print("  \033[1;34m[ 09 ] >> \033[1;36;40mSistemden çıkış")
print("  \033[1;34m[ 10 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("1nf0rmatI0n: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd AstraNmap && bash astranmap.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd alltool && cd Easymap && php easymap.php && cd && cd alltool && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd weeman && python2 weeman.py && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd RED_HAWK && php rhawk.php && cd && cd alltool && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd alltool && cd TM-scanner && python2 tmscanner.py && cd && cd alltool && python2 MainMenu.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd alltool && cd MaxSubdoFinder && python2 maxteroit.py && cd && cd alltool && python2 MainMenu.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd alltool && cd sqlmap-dev && python sqlmap.py -wizard && cd && cd alltool && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd alltool && cd rang3r && python2 rang3r.py --ip 192.168.0.1 && cd && cd alltool && python2 MainMenu.py")
elif(op==9):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 sys.exit()
elif(op==10):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/AnalistickMenu.py")
