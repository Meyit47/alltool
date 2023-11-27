import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mDosyalar ve temel komutlar")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mSüreç kontrolörlerinin komutları")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mErişim hakları ve dosyalar komutları")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mSistem Bilgisi komutları ")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mPaketler ve çalışma komutları")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mArama komutları")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mArşiv komutları")
print("  \033[1;34m[ 08 ] >> \033[1;36;40mAğ komutları")
print("  \033[1;34m[ 09 ] >> \033[1;36;40mSistemden çıkış")
print("  \033[1;34m[ 10 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("1nf0rmatI0nHe1p: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && bash Help/FilesAndBaseCommads.sh")
 os.system("cd && cd alltool && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && bash Help/ProcessControlerCommands.sh")
 os.system("cd && cd alltool && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd alltool && bash Help/SearchCommand.sh")
 os.system("cd && cd alltool && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && bash Help/AccesRightAndFilesCommands.sh")
 os.system("cd && cd alltool && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd alltool && bash Help/SystemInformationCommands.sh")
 os.system("cd && cd alltool && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd alltool && bash Help/InstallingPackagesAndWorkingCommands.sh")
 os.system("cd && cd alltool && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd alltool && bash Help/ArchiveFilesCommands.sh")
 os.system("cd && cd alltool && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd alltool && bash Help/NetworkComands.sh")
 os.system("cd && cd alltool && python3 src/Timer1.py && python2 src/aboutMenu.py")
elif(op==9):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 sys.exit()
elif(op==10):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/HelpTermuxMenu.py")

