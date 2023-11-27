red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

clear
sleep 1
echo -e "$yellow  ___                 __         .__  .__                 "
echo -e "$yellow |   | ____   _______/  |______  |  | |  |   ___________  "    
echo -e "$yellow |   |/    \ /  ___/\   __\__  \ |  | |  | _/ __ \_  __ \ "    
echo -e "$yellow |   |   |  \___  \  |  |  / __ \|  |_|  |_\  ___/|  | \/ "    
echo -e "$yellow |___|___|  /____  > |__| (____  /____/____/\___  >__|    "
echo -e "$yellow          \/     \/            \/               \/        "
echo ""
echo -e "$orange [>] $yellow Tool Adı: alltool "
echo -e "$orange [>] $yellow Geliştirici: MEYITZADE " 

which git > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Git].............................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Git]..........................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][Git Modülü Yükleniyor...]"
apt install git 
fi

which python > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Python]..........................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Python].......................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][Python Modülü Yükleniyor...]"
apt install python > /dev/null
apt install python
apt install python2
apt install python3
pkg install pip
pkg install pip2
pip2 install --upgrade pip
fi

which cowsay > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Cowsay]..........................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Cowsay].......................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][Cowsay Modülü Yükleniyor...]"
apt install cowsay
fi

which wget > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Wget]............................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Wget].........................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][Wget Modül Yükleniyor...]"
apt install wget
fi

which ruby > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Ruby]............................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Ruby].........................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][Ruby Modülü Yükleniyor...]"
apt install ruby 
fi

which toilet > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Toilet]..........................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Toilet].......................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][Toilet Modülü Yükleniyor...]"
apt install toilet 
fi

which figlet > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Figlet]..........................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Figlet].......................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][Figlet Modülü Yükleniyor...]"
apt install figlet 
fi

which lolcat > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Lolcat]..........................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Lolcat].......................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][Lolcat Modülü Yükleniyor...]"
gem install lolcat
fi

which neofetch > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Neofetch]........................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Neofetch].....................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][Neofetch Modülü Yükleniyor...]"
apt install neofetch
fi

which php > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[PHP].............................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[PHP]..........................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][PHP Modülü Yükleniyor...]"
apt install php
fi

which ruby > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Clang]...........................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Clang]........................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][Clang Modülü Yükleniyor...]"
apt install clang
fi

which zip > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Zip].............................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Zip]..........................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][Zip Modülü Yükleniyor...]"
apt install zip
fi

which pip > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[PIP].............................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[PIP]..........................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][pip Modülü Yükleniyor...]"
apt install pip
pkg install pip
pkg install pip2
apt install pip
apt install pip2
pip2 install --upgrade pip
fi

which zsh > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[zsh].............................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[zsh]..........................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][zsh Modülü Yükleniyor...]"
apt install zsh 
fi

which pv > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[pv]..............................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[pv]...........................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!][pv Modülü Yükleniyor...]"
apt install pv
fi

which curl > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Curl]............................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[Curl].........................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!]-[Curl Modülü Yükleniyor...]"
apt install curl 
fi

which w3m > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[w3m].............................[ BAŞARILI ]"
sleep 1.5
else
echo -e "$red[-]-[w3m]..........................[ ARIZALI ]"
sleep 1.5
echo -e "$yellow[!]-[w3m Modülü Yükleniyor...]"
apt install w3m 
fi

red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

cd 
cd
cd alltool
cd Castom
cp ngrok /data/data/com.termux/files/home/
cd
cd
chmod +x ngrok
sleep 2
echo -e "$yellow[+]-[Ngrok Yüklendi!..............[ KURULDU ]"
sleep 1.5
fi

echo -e $yellow
echo -n [!] Bağımlılıklar Yükleniyor...= ;
sleep 3 & while [ "$(ps a | awk '{print $1}' | grep $!)" ] ; do for X in '-' '\' '|' '/'; do echo -en "\b$X"; sleep 0.1; done; done 
echo ""

apt-get install nodejs
npm install --global speed-test
apt install apache2
apt install openssl -y
python3 -m pip install rich
apt install python-dev -y
apt install python3 -y
apt-get install pip2
pip install --upgrade pip2
apt-get install termux-api
pkg install termux-api
pip2 install --upgrade pip
pip2 install passlib
pip install passlib
pip2 install progressbar
pip install progressbar
pip2 install future
pip install future
pip2 install colorama
python3 -m pip install smtp
pip install smtp
pip install flask
pip2 install flask_socketio
pip install flask_socketio
python3 -m pip install flask_socketio
python3 -m pip install flask_cors
pip2 install flask_cors
pip2 install mechanize
pip3 install rich
