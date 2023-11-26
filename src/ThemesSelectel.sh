RED="$(printf '\033[31m')"  GREEN="$(printf '\033[32m')"  ORANGE="$(printf '\033[33m')"  BLUE="$(printf '\033[34m')"
MAGENTA="$(printf '\033[35m')"  CYAN="$(printf '\033[36m')"  WHITE="$(printf '\033[37m')" BLACK="$(printf '\033[30m')"
REDBG="$(printf '\033[41m')"  GREENBG="$(printf '\033[42m')"  ORANGEBG="$(printf '\033[43m')"  BLUEBG="$(printf '\033[44m')"
MAGENTABG="$(printf '\033[45m')"  CYANBG="$(printf '\033[46m')"  WHITEBG="$(printf '\033[47m')" BLACKBG="$(printf '\033[40m')"
DEFAULT_FG="$(printf '\033[39m')"  DEFAULT_BG="$(printf '\033[49m')"

clear
echo "${BLUE}-----------------------------"
echo "| ${RED}Bir tema seç${BLUE}  "
echo "|------- ----  --------- ---|"
echo "| ${CYAN}1. KoyuMavi ${BLUE}                "
echo "| ${CYAN}2. Neon ${BLUE}                   "
echo "| ${CYAN}3. GoogleDark ${BLUE}            |"
echo "| ${CYAN}4. Materia ${BLUE}               |"
echo "| ${CYAN}5. Material ${BLUE}               "
echo "| ${CYAN}6. Smyck ${BLUE}                  "
echo "| ${CYAN}7. Dracula ${BLUE}                "
echo "  ${CYAN}8. Twilight ${BLUE}              |"
echo "|                           |"
echo "| ${RED}Sırasına göre - 1/2/3/4/5/6/7/8: ${BLUE} |"
echo "----  ----------       ------"
read numb
clear
echo "${BLUE}-----------------------------"
echo "| ${RED}Bir süre bekleyin lütfen${BLUE}  "
echo "|------- ----  --------- ---|"
echo "| ${CYAN}1. KoyuMavi ${BLUE}                "
echo "| ${CYAN}2. Neon ${BLUE}                   "
echo "| ${CYAN}3. GoogleDark ${BLUE}            |"
echo "| ${CYAN}4. Materia ${BLUE}               |"
echo "| ${CYAN}5. Material ${BLUE}               "
echo "| ${CYAN}6. Smyck ${BLUE}                  "
echo "| ${CYAN}7. Dracula ${BLUE}                "
echo "  ${CYAN}8. Twilight ${BLUE}              |"
echo "|                           |"
echo "| ${RED}Sırasına göre  1/2/3/4/5/6/7/8: ${BLUE} |"
echo "----  ----------       ------"
if [ $numb = "1" ]
then
        echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Ayarlar Yeniden Yükleniyor..."
        sleep 0.3
        echo ""
        cd
        cd alltool
        bash Themes/Default.sh
        echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Başvuru Başarılı..!"
else
        if [ $numb = "2" ]
        then
                echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Ayarlar Yeniden Yükleniyor..."
                sleep 0.3
                echo ""
                cd
                cd alltool
                bash Themes/Neon.sh
                echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Başvuru Başarılı..!"
        else
                if [ $numb = "3" ]
                then
                        echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Ayarlar Yeniden Yükleniyor..."
                        sleep 0.3
                        echo ""
                        cd
                        cd alltool
                        bash Themes/GoogleDark.sh
                        echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Başvuru Başarılı..!"
                else
                        if [ $numb = "4" ]
                        then
                                echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Ayarlar Yeniden Yükleniyor..."
                                sleep 0.3
                                echo ""
                                cd
                                cd alltool
                                bash Themes/Materia.sh
                                echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Başvuru Başarılı..!"
                        else
                                if [ $numb = "5" ]
                                then
                                        echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Ayarlar Yeniden Yükleniyor..."
                                        sleep 0.3
                                        echo ""
                                        cd
                                        cd alltool
                                        bash Themes/Material.sh
                                        echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Başvuru Başarılı..!"
                                else
                                        if [ $numb = "6" ]
                                        then
                                                echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Ayarlar Yeniden Yükleniyor..."
                                                sleep 0.3
                                                echo ""
                                                cd
                                                cd alltool
                                                bash Themes/Smyck.sh
                                                echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Başvuru Başarılı..!"
                                        else
                                                if [ $numb = "7" ]
                                                then
                                                        echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Ayarlar Yeniden Yükleniyor..."
                                                        sleep 0.3
                                                        echo ""
                                                        cd
                                                        cd alltool
                                                        bash Themes/Dracula.sh
                                                        echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Başvuru Başarılı..!"
                                                else
                                                        if [ $numb = "8" ]
                                                        then
                                                                echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Ayarlar Yeniden Yükleniyor..."
                                                                sleep 0.3
                                                                echo ""
                                                                cd
                                                                cd alltool
                                                                bash Themes/Twilight.sh
                                                                echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Başvuru Başarılı..!"
                                                        else
                                                                echo -n "${BLUE}[${RED}!${BLUE}] ${GREEN}Geçersiz Giriş! Yeniden Yüklemeli"
                                                                sleep 1.5
                                                                cd && cd alltool && bash src/ThemesSelectel.sh
                                                        fi
                                                fi
                                        fi
                                fi
                        fi
                fi
        fi
fi




