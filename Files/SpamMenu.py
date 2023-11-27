import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd alltool && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mSMS-Bomber-300 - bombardıman SMS hizmeti 300 e kadar")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mAnon-SMS - Anonim Olarak Mesaj Gönder")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mSpymer - daha fazla seçenek sms ve çağrı bombacısı")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mAres-Bomb - orta Ares-bombardıman sms")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mTBomb - Is SMS ve Çağrı Bombacısı")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mDuploBomber - Özel SMS Bombacısı")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mEmailPySpam - E-postaları spamlamak için bir python 3+ programı")
print("  \033[1;34m[ 08 ] >> \033[1;36;40mSistemden çıkış - alltool dan çıkış.")
print("  \033[1;34m[ 09 ] >> \033[1;36;40mAna menüye dön")

op=int(raw_input("SpymER: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd alltool && cd SMS-Bomber-300-Free && python SMS-Bomber.py && cd && cd alltool && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd alltool && cd Anon-SMS && bash Run.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd alltool && cd spymer && python spammer.py && cd && cd alltool && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd alltool && cd AresBomb && python boom.py && cd && cd alltool && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd alltool && cd TBomb && ./TBomb.sh && cd && cd alltool && python2 MainMenu.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd alltool && cd duplo-bomber && python3 duplo_spam.py && cd && cd alltool && python2 MainMenu.py")
elif(op==7):
 os.system("clear")
 os.system("cd && cd alltool && cd emailpyspam && cd main && python3 emailspam.py && cd && cd alltool && python2 MainMenu.py")
elif(op==8):
 time.sleep(0.2)
 print("\033[1;31;40mSistemden çıkış...")
 sys.exit()
elif(op==9):
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mGeçersiz Giriş.Araçlar Yeniden Yüklenmeli.") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd alltool")
 os.system("python2 Files/SpamMenu.py")
 
