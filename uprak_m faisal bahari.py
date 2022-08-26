print("1.balok")

panjang =int(input("masukan nilai panjang: "))
lebar = int(input("masukan nilai lebar: "))
tinggi = int(input("masukan nilai tinggi: "))

volume_balok = panjang * lebar * tinggi
print("nilai volum balok adalah", volume_balok)

print("2.limas")

alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))
volume_l= alas * tinggi
print("volume limas adalah: ", volume_l)



print("3.tabung")

import math
r =float(input("masukan jari jari : "))
t =float(input("masukan tinggi :"))
pi =math. pi
v =round(pi*(r*r)*t,2)
print("volume tabung adalalah : ",v)

print("4.1dolarr")

kursdolar = 14000
rupiah = float(input("masukan uang rupiah= "))
rupTodol = rupiah / kursdolar
doldecimal = round(rupTodol, 2)
print("Rp.",rupiah, "==> US$", doldecimal)


