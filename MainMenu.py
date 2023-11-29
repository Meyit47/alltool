#!/usr/bin
#Copyright 2023 alltool
#Kopyalayan : MEYİTZADE
#Telegram   : http://t.me/Meyit47

import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool")
os.system("bash Logo.sh")
os.system("bash src/MenuOps.sh")

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

g="\033[1;32m"
r="\033[1;31m"
w="\033[0m"
b="\033[1;34m"
o="\033[1;33m"
bl="\033[1;36;40m"

op=int(raw_input("options:"))
if(op==1):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd alltool && python3 .check/IpMenuConfig.py")
elif(op==2):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/RouterMenu.py")
elif(op==3):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/MailMenu.py")
elif(op==4):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/WebMenu.py")
elif(op==5):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/CamHackMenu.py")
elif(op==6):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/AndroidMenu.py")
elif(op==7):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/SQLinjectionMenu.py")
elif(op==8):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/SocialMenu.py")
elif(op==9):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/SpamMenu.py")
elif(op==10):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/AnalistickMenu.py")
elif(op==11):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/DarkSearchMenu.py")
elif(op==12):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/PhishingMenu.py")
elif(op==13):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python2 Files/PassworldMenu.py")
elif(op==14):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd alltool && python2 Files/WordlistGeneratorMenu.py")
elif(op==15):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd alltool && python2 Files/XSSAttackMenu.py")
elif(op==16):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd alltool && python2 Files/discordMenu.py")
elif(op==17):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd alltool && python2 Files/telegramMenu.py")
elif(op==18):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd alltool && python3 .check/OtherToolConfig.py")
elif(op==19):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd alltool && python3 .check/TermuxPanelConfig.py")
elif(op==20):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd alltool && python2 .settings/settingsMenu.py")
elif(op==21):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("clear && cd && cd alltool && python2 MainMenu.py")
elif(op==22):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 time.sleep(1)
 os.system("cd && cd alltool && python3 .check/UpdaterConfig.py")
elif(op==23):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("bash src/About.sh")
elif(op==13324715):
 print("[Meyit47] Geliştirici modu başarıyla etkinleştirildi!")
 time.sleep(0.8)
 os.system("cd && cd alltool && cd .settings && mv DesingLogo.py /data/data/com.termux/files/home/AllHackingTools/.temp/ && mv DesingMenu.py /data/data/com.termux/files/home/AllHackingTools/.temp/")
 print("[Meyit47] Lütfen yeniden başla alltool!")
 os.system("cd && cd alltool && mv MainMenu.py /data/data/com.termux/files/home/AllHackingTools/.temp/temp && cd .settings && cd debug && cp MainMenu.py /data/data/com.termux/files/home/AllHackingTools/")
 print("[Meyit47] Uyarı! Özelleştirme devre dışı bırakıldı.")
elif(op==24):
 os.system("clear && cd && cd alltool && bash Logo.sh")
 print("\033[1;31;40mSistemden Çıkış...")
 time.sleep(0.7)
else:
 print("\033[1;31;40mGeçersiz Giriş. Araçlar Yeniden Yükleniyor") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
