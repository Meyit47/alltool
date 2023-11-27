import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mDSLeaks - Discord Sızıntısı toplu kullanıcı bilgileri")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mDSHub - Discord Kaçak Kullanıcı Adı  ")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mDSLookup - Discord Toplu Arama")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mDSHT - Discord Geçmişi Takibi")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mAna menüye dön")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mSistemden çıkış")

op=int(raw_input("D1sc0Rd: "))

if(op==1):
 print("Siteye gidin ve izlemek istediğiniz kullanıcının kimliğini girin.")
 print("website: https://discordleaks.unicornriot.ninja/discord/users")
 os.system("cd && cd alltool && python src/Timer1.py && python2 MainMenu.py")
elif(op==2):
 print("Siteye gidin ve izlemek istediğiniz kullanıcının kimliğini girin.")
 print("website: https://discordhub.com/user/search")
 os.system("cd && cd alltool && python src/Timer1.py && python2 MainMenu.py")
elif(op==3):
 print("Siteye gidin ve izlemek istediğiniz kullanıcının kimliğini girin.")
 print("website: https://discord.id/")
 os.system("cd && cd alltool && python src/Timer1.py && python2 MainMenu.py")
elif(op==4):
 print("Siteye gidin ve izlemek istediğiniz kullanıcının kimliğini girin.")
 print("website: https://dht.chylex.com/")
 os.system("cd && cd alltool && python src/Timer1.py && python2 MainMenu.py")
elif(op==5):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden Çıkış...")
 sys.exit()
elif(op==6):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/discordMenu.py")
