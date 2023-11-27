import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mInstaHack - İnstagram bruteforce hackleme Aracı için En İyi Araç")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mFacebook - Python kullanarak Facebook hesabına Bruteforce saldırısı")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mSherlock - Sosyal ağlarda kullanıcı adına göre sosyal medya hesaplarını avlayın")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mFindUser - Finderda 75'ten fazla kişinin kullanıcı adları")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mUserFinder - Finder Sosyal medyada KullanıcıAdı")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mSistemden çıkış - alltool dan çıkış")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("Soc1alF1sh: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd instahack && bash instahack.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd Facebook-BruteForce && python3 fb.py or python fb2.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd Files && bash SherlockUser.sh")
elif(op==4):
 os.system("clear")
 os.system("cd && cd alltool && cd finduser && bash finduser.sh && cd && cd alltool && python3 src/Timer3.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd alltool && cd UserFinder && bash UserFinder.sh && cd && cd alltool && python3 src/Timer3.py")
elif(op==6):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış..")
elif(op==7):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/SocialMenu.py")
