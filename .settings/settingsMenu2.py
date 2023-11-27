import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")
os.system("cd && bash alltool/.desing/SettingMenu2.sh")

op=int(raw_input("Sett1Ngs: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd .settings && python2 DesingLogo.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd .settings && python2 DesingMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd src && mv AnimationLoad1.sh /data/data/com.termux/files/home/alltool/.temp/ && cd && cd alltool && cd .settings && mv AnimationLoad1.sh /data/data/com.termux/files/home/alltool/src/ && cd && cd alltool && cd .temp && mv AnimationLoad1.sh /data/data/com.termux/files/home/alltool/.settings/ && cd && cd alltool && bash .settings/Applined.sh")
elif(op==4):
 os.system("cd && cd alltool && cd src && mv AnimationLoad1.sh /data/data/com.termux/files/home/alltool/.temp/DesingTemp4/ && mv AnimationLoad2.sh AnimationLoad1.sh && cd && cd alltool && cd .temp && cd DesingTemp4 && mv AnimationLoad1.sh AnimationLoad2.sh && mv AnimationLoad2.sh /data/data/com.termux/files/home/alltool/src/")
elif(op==5):
 os.system("clear")
 os.system("cd && cd alltool && cd .settings && python2 SpecialOpportunities.py")
elif(op==6):
 os.system("clear")
 os.system("cd && nano .zsh_history")
elif(op==7):
 os.system("clear")
 os.system("cd && rm -rf alltool/.settings/deletedfiles/.zsh_history && cd && mv .zsh_history alltool/.settings/deletedfiles/ && cd && cd alltool && python2 MainMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd alltool && bash Logo.sh")
 time.sleep(0.2)
 print("\033[1;31;40mAlltool yedeklemesini geri yükleme...")
 os.system("cd /sdcard/ && cp -r alltool /data/data/com.termux/files/home/")
 os.system("cd && bash alltool/.settings/RestorealltoolBackup.sh")
 print("yedekleme başarıyla geri yüklendi: sdcard...")
elif(op==9):
 os.system("clear")
 os.system("cd && cd alltool && bash Logo.sh")
 time.sleep(0.2)
 print("\033[1;31;40mYedeklemenin Oluşturulması İçin Biraz Bekleyin...")
 os.system("cd && cd && cp -r alltool /sdcard/")
 print("başarıyla şu konumda bir yedekleme oluşturuldu: sdcard...")
elif(op==10):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 sys.exit()
elif(op==11):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
