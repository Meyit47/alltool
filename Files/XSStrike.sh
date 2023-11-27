g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd alltool
bash Logo.sh
cd XSStrike
echo ""
echo -e $b">>>"$w" Site adresini yazın: "$g"XSStrike"$w
read siteURL3
sleep 0.1
echo -e $b">>>"$w" Bir süre bekleyin lütfen: "$g"XSStrikr"$w
sleep 0.6
python3 xsstrike.py -u $siteURL3 
cd
cd
cd alltool
