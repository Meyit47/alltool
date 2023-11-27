import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")
os.system("cd && bash alltool/.desing/desingpanel/desingpanel0.sh")

op=int(raw_input("TermUxPane1: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && bash Files/ViewS.sh")
elif(op==2):
 os.system("cd")
 os.system("cd alltool")
 os.system("w3m http://google.com/")
 os.system("cd && cd alltool && python2 Files/TermuxS.py")
elif(op==3):
 os.system("cd && cd alltool")
 os.system("termux-battery-status")
 os.system("python3 src/Timer.py")
 os.system("python2 src/aboutMenu.py")
elif(op==4):
 os.system("cd")
 os.system("cd alltool")
 os.system("bash src/PassGenerator.sh")
 os.system("cd && cd alltool && python2 Files/TermuxS.py")
elif(op==5):
 os.system("cd")
 os.system("cd alltool")
 os.system("termux-style")
 os.system("cd && cd alltool && python2 Files/TermuxS.py")
elif(op==7):
 os.system("cd")
 os.system("cd alltool")
 os.system("bash src/Inf.sh")
 os.system("python2 Files/HelpTermuxMenu.py")
elif(op==6):
 os.system("cd")
 os.system("cd .. && cd usr/var/log/apt && rm -r history.log && rm -r term.log && rm -r eipp.log.xz && cd .. && rm -r alternatives.log")
 time.sleep(0.5)
 print("\033[1;31;40m Termux günlükleri temizlendi...")
 time.sleep(0.6)
 os.system("cd && cd alltool && python2 Files/TermuxS.py")
elif(op==8):
 os.system("cd && cd alltool && cd TermuxBackupTools && ./rewind -b")
elif(op==9):
 os.system("cd && cd alltool && cd TermuxBackupTools && ./rewind -r")
elif(op==10):
 os.system("cd && pkg clean && apt clean && cd && cd alltool && python2 MainMenu.py")
elif(op==11):
 os.system("cd && cd alltool && bash src/Inf.sh && python2 src/BannerType.py")
elif(op==12):
 os.system("cd && cd alltool && python src/CheckPackages.py && python2 Files/TermuxS.py ")
elif(op==13):
 os.system("cd && cd alltool && cp -r Termux-os /data/data/com.termux/files/home && cd && cd Termux-os && bash TermuxNewKeys.sh && cd && cd alltool && python2 Files/TermuxS.py")
elif(op==14):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 time.sleep(0.7)
elif(op==15):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/TermuxS.py")
