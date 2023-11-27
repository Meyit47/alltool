import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mCam-Hacker - Hack Kameralar CCTV ÜCRETSİZ")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mGrabCam - Termux'tan kamera hacklemek için bir araç")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mCamHack - Bir BAĞLANTI göndererek Ön Kamerayı hackleyin")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mExit System - alltool dan çıkış")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("CamPh1sh: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd Cam-Hackers && python3 cam-hackers.py && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd grabcam && bash grabcam.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd CamHack && bash CamHack.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 sys.exit()
elif(op==5):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/CamHackMenu.py")
