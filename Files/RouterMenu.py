import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mRouterSploit - Yönlendiricileri hacklemek için evrensellik aracı")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mWebSploit - Gelişmiş bir MiTM Çerçevesi")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mCommix - İşletim Sistemi Komut Enjeksiyonu Kullanım Aracı")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mTxtool - Kolay bir pentest aracı")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mFim - Facebook Kaba Kuvvet")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mSistemden çıkış")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("Expl0Tat10nTool: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd routersploit && python3 rsf.py && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd websploit && sudo websploit && cd && cd alltool && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd commix && python commix.py --wizard && cd && cd alltool && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd alltool && cd txtool && txtool && cd && cd alltool && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd alltool && cd fim && python fim.py && cd && cd alltool && python2 MainMenu.py")
elif(op==6):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 sys.exit()
elif(op==7):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/RouterMenu.py")
 
