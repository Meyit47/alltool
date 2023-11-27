g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd alltool
clear
python2 ismtp.py
echo "Programı çalıştırmak için lütfen gerekli tüm ayarlarınızı girin."
echo -e $b">>>"$w" Consoler "$g"iSMTP"$w
read opt
sleep 0.1
python2 ismtp.py $opt
cd
cd
cd alltool
