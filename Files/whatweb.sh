g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd alltool
cd WhatWeb
clear
./whatweb
echo "Programı çalıştırmak için lütfen gerekli ayarlarınızı girin, örneğin: reddit.com"
echo -e $b">>>"$w" consoller "$g"WhatWeb"$w
read opt
sleep 0.1
./whatweb $opt
cd
cd
cd alltool
