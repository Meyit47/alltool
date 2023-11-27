g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd alltool
bash Logo.sh
cd XSSCon
echo ""
echo -e $b">>>"$w" Site adresini yazın: "$g"XSScon"$w
read siteURL1
sleep 0.1
echo -e $b">>>"$w" Bir süre bekleyin lütfen: "$g"XSScon"$w
sleep 0.6
python3 xsscon.py -u $siteURL1 
cd
cd
cd alltool
