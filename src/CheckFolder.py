import time
import os 

R = '\033[31m'
G = '\033[32m' 
C = '\033[36m'
W = '\033[0m' 

# Secret folders
path1 = "/data/data/com.termux/files/home/alltool/.logs/"
path2 = "/data/data/com.termux/files/home/alltool/.settings/"
path3 = "/data/data/com.termux/files/home/alltool/.temp/"
path4 = "/data/data/com.termux/files/home/alltool/.check/"

# No secret folders
path5 = "/data/data/com.termux/files/home/alltool/Files/"
path6 = "/data/data/com.termux/files/home/alltool/src/"
path7 = "/data/data/com.termux/files/home/alltool/Tool/"
path8 = "/data/data/com.termux/files/home/alltool/Themes/"
path9 = "/data/data/com.termux/files/home/alltool/Castom/"

# check folders
if os.path.exists(path1):
    if os.path.exists(path2):
        if os.path.exists(path3):
            if os.path.exists(path4):
                if os.path.exists(path5):
                    if os.path.exists(path6):
                        if os.path.exists(path7):
                            if os.path.exists(path8):
                                if os.path.exists(path9):
                                    os.system("cd && cd alltool && cd src && bash starterUp.sh")
                                else:
                                    print(R + '[-] ' + C + 'Hata kodu: 106 DNS sunucusu bağlanmayı reddetti')
                                    print(R + '[-] ' + C + 'Hata kodu: 404 Bulunamadı! Sistem klasörü yok')
                                    print(R + '[-] ' + C + 'Hata kodu: 500 Klasör bulunamadığı için istek işlenemiyor!')
                                    print("")
                                    print(R + '[-] ' + C + 'Sistemi yeniden yüklemeyi veya bir yedekten geri yüklemeyi deneyin!')
                                    print(R + '[-] ' + C + 'Sistem başlatılamıyor! Sistem dosyaları zarar görmüş olabilir!')
                                    exit(0)

                            else:
                                print(R + '[-] ' + C + 'Hata kodu: 106 DNS sunucusu bağlanmayı reddetti')
                                print(R + '[-] ' + C + 'Hata kodu: 404 Bulunamadı! Sistem klasörü yok')
                                print(R + '[-] ' + C + 'Hata kodu: 500 Klasör bulunamadığı için istek işlenemiyor!')
                                print("")
                                print(R + '[-] ' + C + 'Sistemi yeniden yüklemeyi veya bir yedekten geri yüklemeyi deneyin!')
                                print(R + '[-] ' + C + 'Sistem başlatılamıyor! Sistem dosyaları zarar görmüş olabilir!')
                                exit(0)
                        else:
                            print(R + '[-] ' + C + 'Hata kodu: 106 DNS sunucusu bağlanmayı reddetti')
                            print(R + '[-] ' + C + 'Hata kodu: 404 Bulunamadı! Sistem klasörü yok')
                            print(R + '[-] ' + C + 'Hata kodu: 500 Klasör bulunamadığı için istek işlenemiyor!')
                            print("")
                            print(R + '[-] ' + C + 'Sistemi yeniden yüklemeyi veya bir yedekten geri yüklemeyi deneyin!')
                            print(R + '[-] ' + C + 'Sistem başlatılamıyor! Sistem dosyaları zarar görmüş olabilir!')
                            exit(0)
                    else:
                        print(R + '[-] ' + C + 'Hata kodu: 106 DNS sunucusu bağlanmayı reddetti')
                        print(R + '[-] ' + C + 'Hata kodu: 404 Bulunamadı! Sistem klasörü yok')
                        print(R + '[-] ' + C + 'Hata kodu: 500 Klasör bulunamadığı için istek işlenemiyor!')
                        print("")
                        print(R + '[-] ' + C + 'Sistemi yeniden yüklemeyi veya bir yedekten geri yüklemeyi deneyin!')
                        print(R + '[-] ' + C + 'Sistem başlatılamıyor! Sistem dosyaları zarar görmüş olabilir!')
                        exit(0)
                else:
                    print(R + '[-] ' + C + 'Hata kodu: 106 DNS sunucusu bağlanmayı reddetti')
                    print(R + '[-] ' + C + 'Hata kodu: 404 Bulunamadı! Sistem klasörü yok')
                    print(R + '[-] ' + C + 'Hata kodu: 500 Klasör bulunamadığı için istek işlenemiyor!')
                    print("")
                    print(R + '[-] ' + C + 'Sistemi yeniden yüklemeyi veya bir yedekten geri yüklemeyi deneyin!')
                    print(R + '[-] ' + C + 'Sistem başlatılamıyor! Sistem dosyaları zarar görmüş olabilir!')
                    exit(0)
            else:
                print(R + '[-] ' + C + 'Hata kodu: 106 DNS sunucusu bağlanmayı reddetti')
                print(R + '[-] ' + C + 'Hata kodu: 404 Bulunamadı! Sistem klasörü yok')
                print(R + '[-] ' + C + 'Hata kodu: 500 Klasör bulunamadığı için istek işlenemiyor!')
                print("")
                print(R + '[-] ' + C + 'Sistemi yeniden yüklemeyi veya bir yedekten geri yüklemeyi deneyin!')
                print(R + '[-] ' + C + 'Sistem başlatılamıyor! Sistem dosyaları zarar görmüş olabilir!')
                exit(0)
        else:
            print(R + '[-] ' + C + 'Hata kodu: 106 DNS sunucusu bağlanmayı reddetti')
            print(R + '[-] ' + C + 'Hata kodu: 404 Bulunamadı! Sistem klasörü yok')
            print(R + '[-] ' + C + 'Hata kodu: 500 Klasör bulunamadığı için istek işlenemiyor!')
            print("")
            print(R + '[-] ' + C + 'Sistemi yeniden yüklemeyi veya bir yedekten geri yüklemeyi deneyin!')
            print(R + '[-] ' + C + 'Sistem başlatılamıyor! Sistem dosyaları zarar görmüş olabilir!')
            exit(0)

    else:
        print(R + '[-] ' + C + 'Hata kodu: 106 DNS sunucusu bağlanmayı reddetti')
        print(R + '[-] ' + C + 'Hata kodu: 404 Bulunamadı! Sistem klasörü yok')
        print(R + '[-] ' + C + 'Hata kodu: 500 Klasör bulunamadığı için istek işlenemiyor!')
        print("")
        print(R + '[-] ' + C + 'Sistemi yeniden yüklemeyi veya bir yedekten geri yüklemeyi deneyin!')
        print(R + '[-] ' + C + 'Sistem başlatılamıyor! Sistem dosyaları zarar görmüş olabilir!')
        exit(0)
else:
    print(".logs klasörü mevcut değil!")
    print(R + '[-] ' + C + 'Hata kodu: 106 DNS sunucusu bağlanmayı reddetti')
    print(R + '[-] ' + C + 'Hata kodu: 404 Bulunamadı! Sistem klasörü yok')
    print(R + '[-] ' + C + 'Hata kodu: 500 Klasör bulunamadığı için istek işlenemiyor!')
    print("")
    print(R + '[-] ' + C + 'Sistemi yeniden yüklemeyi veya bir yedekten geri yüklemeyi deneyin!')
    print(R + '[-] ' + C + 'Sistem başlatılamıyor! Sistem dosyaları zarar görmüş olabilir!')
    exit(0)
