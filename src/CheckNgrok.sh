red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

arch=`arch`
if [ -f "ngrok" ]; then
echo -e "$green[+]-[Ngrok]..........................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Ngrok]........................[ BULUNAMADI ]"
sleep 0.2
echo -e "$yellow[!]-[İndiriliyor:Ngrok.............[ KURULUM ]"
sleep 1.2
cd 
cd
cd alltool
cd Castom
cp ngrok /data/data/com.termux/files/home/
cd
cd
chmod +x ngrok
sleep 2
echo -e "$yellow[+]-[Ngrok İNDİRİLMİŞ!..............[ KURULMUŞ ]"
sleep 1.5
fi

