import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mWlcreator - Kelime listesi yaratıcısı yazılı C")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mGoblinWordGenerator - Python'da kullanışlı kelime listesi oluşturur")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mSMWYG - araç OSINT ve keşif yapmanızı sağlar")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mSistemden Çıkış - alltool dan çıkış")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("Ma1lHacK: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd wlcreator && ./wlcreator 5 && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd GoblinWordGenerator && python3 goblin.py && cd && cd alltool && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd SMWYG-Show-Me-What-You-Got && python3 SMWYG.py && cd && cd alltool && python2 MainMenu.py")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mSistemdem çıkış...")
 sys.exit()
elif(op==5):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/AndroidMenu.py")
