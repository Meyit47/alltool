import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mMailHack - Email hacker")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mPwnedOrnot - Tool for find passworld email")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mExit Utility")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Ma1lHacK: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd hack-gmail && python3 hack-gmail.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd pwnedOrNot && python3 pwnedornot.py")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
elif(op==4):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/MailMenu.py")