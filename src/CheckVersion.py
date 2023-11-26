
R = '\033[31m'
G = '\033[32m' 
C = '\033[36m'
W = '\033[0m' 

from heconsole import console
from shutil import which
import time
import os
import sys

print(G + '[+]' + C + ' Bağımlılıkları ve Paketleri Kontrol Etme...' + W)
pkgs = ['python3', 'pip', 'php', 'ssh', 'pip2', 'wget', 'curl', 'python', 'python2', 'toilet', 'neofetch', 'figlet', 'lolcat', 'clang', 'w3m', 'jq', 'ruby', 'pv']
inst = True
for pkg in pkgs:
	present = which(pkg)
	if present == None:
		print(R + '[-] ' + W + pkg + C + ' yüklü değil!')
		inst = False
	else:
		pass
if inst == False:
	exit()
else:
	pass

console.arrowLog(0, "başarılı bir şekilde kontrol edildi")
console.arrowInfo(2, "başlıyor")
console.arrowInfo(1, "güncelleme denetleyicisi başlatılıyor")
import csv
import json
import argparse
import requests
import subprocess as subp

row = []
info = ''
result = ''
version = '2.7.4'

def ver_check():
	print(G + '[+]' + C + ' Güncellemeler için alltool u kontrol etme....', end='')
	ver_url = 'https://raw.githubusercontent.com/mishakorzik/AllHackingTools/main/Castom/version.txt'
	try:
		ver_rqst = requests.get(ver_url)
		ver_sc = ver_rqst.status_code
		if ver_sc == 200:
			github_ver = ver_rqst.text
			github_ver = github_ver.strip()

			if version == github_ver:
				print(C + '[' + G + ' Güncelleme yok ' + C +']' + '\n')
			else:
				print(C + '[' + R + ' Mevcut : {} '.format(github_ver) + C + ']' + '\n')
				print(R + '[-] ' + C + 'Lütfen sistemi güncelleyin: msdconsoleUPD')
		else:
			print(C + '[' + R + ' Durum : {} '.format(ver_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' İstisna : ' + W + str(e))

try:
	ver_check()

except KeyboardInterrupt:
	print ('\n' + R + '[!]' + C + ' Klavye Kesintisi.' + W)
	os.system("cd && bash alltool/.check/ConfigurationOptions.sh")

