g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd alltool
bash Logo.sh
cd HatCloud
echo ""
echo -e $b">>>"$w" Sitenin adını http olmadan yazın Sitenin adını httpi olmadan yazın & https: "$g"HatCloud"$w
read siteURL3
sleep 0.1
echo -e $b">>>"$w" Bir süre bekleyin lütfen: "$g"HatCloud"$w
sleep 0.6
ruby hatcloud.rb -b $siteURL3
cd
cd
cd alltool
