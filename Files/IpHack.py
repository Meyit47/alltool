from iphack import *

print("01: IP adresi")
print("02: Proxy Denetleyicisi")
print("03: Proxy Oluşturucu")

op = input("Seçeneği Seçin: ")

if op == "1" or op == "01":
    ip_adr = input("IP iken: ")
    ip.address(ip_adr)
if op == "2" or op == "02":
    ip_p = input("Proxy ip iken: ")
    port_p = input("Proxy bağlantı noktası iken: ")
    check.proxy(ip_p, port_p)
if op == "3" or op == "03":
    ip.proxy(False)
