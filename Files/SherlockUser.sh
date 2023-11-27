g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd alltool
bash Logo.sh
cd sherlock
echo ""
echo -e $b">>>"$w" Kullanıcı Adını Yazın: "$g"Sherlock"$w
read NameOrUser
sleep 0.1
echo -e $b">>>"$w" Bir süre bekleyin lütfen: "$g"Sherlock"$w
sleep 0.8
clear
python3 sherlock.py $NameOrUser
cd
cd
cd alltool
python3 src/Timer3.py
