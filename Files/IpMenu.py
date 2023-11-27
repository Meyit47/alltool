import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mAstraNmap - Bir bilgisayar ağındaki ana bilgisayarları ve hizmetleri bulmak için kullanılan güvenlik tarayıcısı")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mEvilURL - IDN Homograf Saldırısı için unicode kötü etki alanları oluşturun ve bunları tespit edin")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mOSIF - Açık Kaynak Bilgisi Facebook")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mWeeman - Python'da kimlik avı için HTTP sunucusu")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mMaxSubdoFinder - Alt Alan Adını Keşfetme Aracı")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mEasymap - Nmap Kısayolu")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mTrape - İnternet OSINT'te kişi takibi")
print("  \033[1;34m[ 08 ] >> \033[1;36;40mRed Hawk - Bilgi Toplama, Güvenlik Açığı Taraması ve Tarama")
print("  \033[1;34m[ 09 ] >> \033[1;36;40mLittleBrother - Bir kişi (AB) hakkında bilgi toplama (OSINT)")
print("  \033[1;34m[ 10 ] >> \033[1;36;40mSeeker - Akıllı Telefonların ve GPS'in Doğru Yerini Belirleyin")
print("  \033[1;34m[ 11 ] >> \033[1;36;40mReconDog - İsviçre Keşif Çakısı")
print("  \033[1;34m[ 12 ] >> \033[1;36;40mD-Tech - Modern Web'e Sızma Testi")
print("  \033[1;34m[ 13 ] >> \033[1;36;40mWebKiller - Python ile Araç Bilgisi Toplama Yazma")
print("  \033[1;34m[ 14 ] >> \033[1;36;40mIpHack - Termux'ta Canlı Adres ve Şehir ile Konumu Takip Edin")
print("  \033[1;34m[ 15 ] >> \033[1;36;40mNikto - Nikto web sunucusu tarayıcısı")
print("  \033[1;34m[ 16 ] >> \033[1;36;40miSMTP - SMTP Sunucu Test Cihazı")
print("  \033[1;34m[ 17 ] >> \033[1;36;40mMailFinder - Ad ve soyadına göre e-posta bulmak için OSINT aracı")
print("  \033[1;34m[ 18 ] >> \033[1;36;40mExit System - alltool dan çıkış")
print("  \033[1;34m[ 19 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("1nf0RmatI0n: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd AstraNmap && bash astranmap.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd EvilURL && python3 evilurl.py && cd && cd alltool && python2 MainMenu.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd alltool && cd Easymap && php easymap.php && cd && cd alltool && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd OSIF && python2 osif.py && cd && cd alltool && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd alltool && cd weeman && python2 weeman.py && cd && cd alltool && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd alltool && cd MaxSubdoFinder && python2 maxteroit.py && cd && cd alltool && python2 MainMenu.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd alltool && cd trape && python trape.py && cd && cd alltool && python2 MainMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd alltool && cd RED_HAWK && php rhawk.php && cd && cd alltool && python2 MainMenu.py")
elif(op==9):
 os.system("clear")
 os.system("cd && cd alltool && cd LittleBrother && python3 LittleBrother.py && cd && cd alltool && python2 MainMenu.py")
elif(op==10):
 os.system("clear")
 os.system("cd && cd alltool")
 print("Termux'ta ikinci bir pencere açın ve 8080 numaralı bağlantı noktasında ngrok'u çalıştırın: ./ngrok http 8080")
 time.sleep(1.4)
 print("Warning alltool zaten ngrok'u indirdi")
 time.sleep(2.3)
 os.system("cd seeker && python3 seeker.py -t manual && cd && cd alltool && python2 MainMenu.py")
elif(op==11):
 os.system("clear")
 os.system("cd && cd alltool && cd ReconDog && ./dog && cd && cd alltool && python2 MainMenu.py")
elif(op==12):
 os.system("clear")
 os.system("cd && cd alltool && cd D-Tech && python2 d-tect.py && cd && cd alltool && python2 MainMenu.py")
elif(op==13):
 os.system("clear")
 os.system("cd && cd alltool && cd webkiller && python3 webkiller.py && cd && cd alltool && python2 MainMenu.py")
elif(op==14):
 os.system("clear")
 os.system("cd && cd alltool && cd Files && bash IpHack.sh && python2 MainMenu.py")
elif(op==15):
 os.system("clear")
 os.system("cd && cd alltool && cd Files && bash Nikto.sh && echo done! && sleep 3 && cd && cd alltool && python2 MainMenu.py")
elif(op==16):
 os.system("clear")
 os.system("cd && cd alltool && cd Files && bash iSMTP.sh && echo done! && sleep 3 && cd && cd alltool && python2 MainMenu.py")
elif(op==17):
 os.system("clear")
 os.system("cd && cd alltool && cd MailFinder && python MailFinder.py && echo done! && sleep 3 && cd && cd alltool && python2 MainMenu.py")
elif(op==18):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 sys.exit()
elif(op==19):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/IpMenu.py")
