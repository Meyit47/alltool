import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mHasher - Otomatik karma algılamalı karma kırıcı")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mHasherDoid - Şifrelenmiş bir metni bulmak için bir araç")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mHash Generator - Güzel Hash Jeneratörü")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mHash Buster - Karmaları saniyeler içinde kırın")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mSistemden çıkış")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mAna Menüye dön")

op=int(raw_input("PAssW0r1dHack: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd hasher && python2 hash.py && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd hasherdoid && python2 hasherdotid.py && cd && cd alltool && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd hash-generator && python2 hashgen.py && cd && cd alltool && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd alltool && cd Hash-Buster && python3 hash.py && cd && cd alltool && python2 MainMenu.py")
elif(op==5):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 sys.exit()
elif(op==6):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/PassworldMenu.py")
