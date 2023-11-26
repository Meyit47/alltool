import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && bash src/LiteLogo.sh")

print("")
print("  \033[1;34m[01] \033[1;36;40mVarsayılan -  Standart kurulum ve varsayılan")
print("  \033[1;34m[02] \033[1;36;40mKodlanmış  -  Kodlanmış kodla yükleme ÖNERİLMEZ")
print("  \033[1;34m[02] \033[1;36;40mÇıkış -  Çık ve indirme alltool")

op=int(raw_input("1nStall: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && bash Files/Modules.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && bash Files/CodedModules.sh")
elif(op==2):
 time.sleep(0.2)
 print("\033[1;31;40malltool Kurulumcudan Çıkıyor...")
 sys.exit()
else:
 print("\033[1;31;40mGeçersiz Giriş. alltool  Kurulumcudan çıkıyor") 
 time.sleep(0.8)
