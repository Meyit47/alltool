import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mZphisher - 30'dan fazla şablona sahip otomatik bir kimlik avı aracı")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mShellphish - SacialFish in değiştirilmiş versiyonu")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mSayCheese - Bağlantıyla hedefin web kamerası çekimlerini yakalayın")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mBlackPhish - Kolay bir kimlik avı aracıdır")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mUserRecon - sosyal medyadan insanları bul")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mMask Phish - Maskeleme kimlik avı URL'si")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mSeeker - Akıllı Telefonların Doğru Yerini Belirleyin")
print("  \033[1;34m[ 08 ] >> \033[1;36;40mAIOPhish - Kimlik avına yönelik bir Sosyal Araç Seti")
print("  \033[1;34m[ 09 ] >> \033[1;36;40mISeeYou - Kullanıcıların tam konumunu bulun")
print("  \033[1;34m[ 10 ] >> \033[1;36;40mBlackEye - 38 web sitesiyle en iyi kimlik avı aracı!")
print("  \033[1;34m[ 11 ] >> \033[1;36;40mNPhish - 60'tan Fazla Kimlik Avı Sitesine Sahip Kimlik Avı Aracı")
print("  \033[1;34m[ 12 ] >> \033[1;36;40mPyPhisher - 77'den fazla web sitesi şablonuyla kullanımı kolay kimlik avı aracı.")
print("  \033[1;34m[ 13 ] >> \033[1;36;40mSistemden çıkış - alltool dan çıkış")
print("  \033[1;34m[ 14 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("Phish1ng: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd zphisher && bash zphisher.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd ShellPhish && bash shellphish.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd saycheese && bash saycheese.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd alltool && cd BlackPhish && sudo python3 blackphish.py && cd && cd alltool && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd alltool && bash Castom/userrecon.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd alltool && cd Mask-Phish.Termux && bash Mask-Phish.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd alltool")
 print("Termux'ta ikinci bir pencere açın ve 8080 numaralı bağlantı noktasında ngrok'u çalıştırın: ./ngrok http 8080")
 time.sleep(1.4)
 print("Uyarı alltool zaten ngrok'u indirdi")
 time.sleep(2.3)
 os.system("cd && cd alltool && cd seeker && python3 seeker.py -t manual && cd && cd alltool && python2 MainMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd alltool && cd AIOPhish && bash aiophish.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==9):
 os.system("clear")
 os.system("cd && cd alltool && cd I-See-You && ./ISeeYou.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==10):
 os.system("clear")
 os.system("cd && cd alltool && cd blackeye && bash blackeye.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==11):
 os.system("clear")
 os.system("NPhish")
elif(op==12):
 os.system("clear")
 os.system("pyphisher")
elif(op==13):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 sys.exit()
elif(op==14):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/PhishingMenu.py")
 
