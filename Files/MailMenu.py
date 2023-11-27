import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mMailHack - E-posta korsanı")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mPwnedOrnot - Password ve e-postayı bulma aracı")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mEmailPySpam - Spam e-postalara ve daha fazla seçeneğe yönelik bir python 3+ programı!")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mGmailHack - Bir python kolay e-posta korsanı")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mEmailSpammer - Spam e-postalar için Ultimate komut dosyası!")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mExit System - alltool dan çıkış")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("Ma1lHacK: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd hack-gmail && python3 hack-gmail.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd pwnedOrNot && python3 pwnedornot.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd emailpyspam && cd main && python3 emailspam.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd alltool && cd Gmail-Hack && python3 Mail-Hack.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd alltool && cd Email-Spammer && python custom_spam.py && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==6):
 time.sleep(0.2)
 print("\033[1;31;40mSistwmden çıkış...")
elif(op==7):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/MailMenu.py")
