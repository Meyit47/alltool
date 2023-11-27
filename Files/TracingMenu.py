import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mSeeker - Akıllı Telefonların ve GPS'in Doğru Yerini Belirleyin")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mTrape - İnternet OSINT'te kişi takibi")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mSistemden çıkış - alltool dan çıkış ")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("IpTrac1Ng: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool")
 print("Termux'ta ikinci bir pencere açın ve 8080 numaralı bağlantı noktasında ngrok'u çalıştırın: ./ngrok http 8080")
 time.sleep(1.4)
 print("Uyarı alltool zaten ngrok'u indirdi")
 time.sleep(2.3)
 os.system("cd && cd alltool && cd seeker && python3 seeker.py -t manual && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd trape && python trape.py && cd &Geçersiz Giriş. Yeniden Yükleme Araçları& cd alltool && python2 MainMenu.py")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden Çıkış...")
 sys.exit()
elif(op==4):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş. Yeniden Yükleme Araçları") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/AndroidMenu.py")
