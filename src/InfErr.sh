g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
o="\033[1;33m"

echo -e $w"["$g"BİLGİ"$w"]"$b"Araç menüsünü . Bir süre bekleyin lütfen!"$w
sleep 0.06
echo -e $w"["$o"UYARI"$w"]"$b"Termux uygulamasını kapatmayın! Ve termux'tan çıkmayın!"$w
sleep 0.07
echo -e $w"["$r"HATA"$w"]"$b"Error to starting tool! Error code 25-39"$w
sleep 0.02
echo -e $w"["$g"BİLGİ"$w"]"$b"Reloading Tools. Please wait!"$w
cd
cd alltool
python2 MainMenu.py




