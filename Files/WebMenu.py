import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mAdminHack - Yönetici panelini hackle")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mSubDom - cname bulma aracı")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mBlazy - modern giriş bruteforcer")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mSqlMap - SQL enjeksiyon ve veritabanı devralma aracı")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mWebSploit - Gelişmiş bir MiTM Çerçevesi")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mSqlmate - SQLmap'ten her zaman beklediğinizi yapacak bir SQLmap dostu")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mSH33LL - Kolay Shell tarayıcı")
print("  \033[1;34m[ 09 ] >> \033[1;36;40mUltraDDos - Ddos web siteleri için araç")
print("  \033[1;34m[ 10 ] >> \033[1;36;40mWhatWeb - Yeni nesil web tarayıcısı")
print("  \033[1;34m[ 11 ] >> \033[1;36;40mWfuzz - Web uygulaması fuzzer'ı")
print("  \033[1;34m[ 12 ] >> \033[1;36;40mSistemden çıkış - alltool dan çıkış.")
print("  \033[1;34m[ 13 ] >> \033[1;36;40mAna menüye dön")


op=int(raw_input("Web-Hack1Ng: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd AdminHack && bash AdminHack.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd Files && bash SubDom.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd Blazy && python2 blazy.py && cd && cd alltool && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd alltool && cd sqlmap-dev && python sqlmap.py -wizard && cd && cd alltool && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd alltool && cd websploit && websploit && cd && cd alltool && python2 MainMenu.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd alltool && cd sqlmate && python2 sqlmate && cd && cd alltool && python2 MainMenu.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd alltool && cd SH33LL && python2 sh33l.py && cd && cd alltool && python2 MainMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd alltool && cd py-ddoser && python ddos.py && cd && cd alltool && python2 MainMenu.py")
elif(op==9):
 os.system("clear")
 os.system("cd && cd alltool && cd Ultra-DDos && python2 main.py && cd && cd alltool && python2 MainMenu.py")
elif(op==10):
 os.system("clear")
 os.system("cd && cd alltool && cd Files && bash whatweb.sh && echo done! && sleep 4 && cd && cd alltool && python2 MainMenu.py")
elif(op==11):
 os.system("clear")
 os.system("cd && cd alltool && cd Files && bash wfuzz.sh && echo done! && sleep 4 && cd && cd alltool && python2 MainMenu.py")
elif(op==12):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 sys.exit()
elif(op==13):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/WebMenu.py")
