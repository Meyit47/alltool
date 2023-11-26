cd
cd
cd alltool
python3 src/CheckVersion.py
python3 .check/CheckServerYesAndNo.py
sleep 3
clear
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
cd
cd
cd alltool 
cd Tool
mv MainMenu.py /data/data/com.termux/files/home/alltool
cd
cd alltool
clear
echo -e $b"[ ✔ ]"$g"başarıyla doğrulandı"$w
python2 MainMenu.py
