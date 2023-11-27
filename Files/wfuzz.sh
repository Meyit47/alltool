g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd alltool
clear
wfuzz
echo "Programı çalıştırmak için lütfen gerekli ayarlarınızı girin, örneğin: -h https://www.example.com"
echo -e $b">>>"$w" Consoler "$g"Wfuzz"$w
read opt
sleep 0.1
wfuzz $opt
cd
cd
cd alltool
