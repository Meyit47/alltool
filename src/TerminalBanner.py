import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print(" \033[1;34mBu başlığı şu bölümden değiştirebilirsiniz: Terminal Ayarları aracılığıyla")
print("  \033[1;34m[ 01 ] >> \033[1;36;40mZehir")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mKabarık")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mAvatar")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mKanlı")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mModüler")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mRusto")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mVarsayılan")
print("  \033[1;34m[ 08 ] >> \033[1;36;40mÇıkış")

op=int(raw_input("TeRMuxBannER: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && bash src/CreateTermuxBannerPoison.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && bash src/CreateTermuxBannerPuffy.sh")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && bash src/CreateTermuxBannerAvatar.sh")
elif(op==4):
 os.system("clear")
 os.system("cd && cd alltool && bash src/CreateTermuxBannerBloody.sh")
elif(op==5):
 os.system("clear")
 os.system("cd && cd alltool && bash src/CreateTermuxBannerModular.sh")
elif(op==6):
 os.system("clear")
 os.system("cd && cd alltool && bash src/CreateTermuxBannerRusto.sh")
elif(op==7):
 os.system("clear")
 os.system("cd && cd alltool && bash src/CreateTermuxBanner.sh")
elif(op==8):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden Çıkış...")
else:
 print("\033[1;31;40mGeçersiz Giriş. Araçlar Yeniden Yükleniyor...") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/TermuxS.py")
