print("\1. segitiga")

alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))
luas_s = alas * tinggi / 2
print("luas segitiga adalah: ", luas_s)

print("\2.persegi panajang")

panjang =int(input("masukan nilai panjang: "))
lebar = int(input("masukan nilai lebar: "))
luas_pp = panjang * lebar
print("luas perseegi panjang adalah:", luas_pp)

print("\n3.lingkaran")

r = int (input("masukan jari jari: "))
keliling = 2 * 3.14 * r
luas = 3.14 * r * r
print ("keeliling =",keliling)
print ("luas =",luas)

print("\n4.jajar genjang")

alas = float(input("masukan nilai alas: "))
tinggi = float(input("masukan nilai tinggi: "))
luas_jg = alas * tinggi

print("luas jajargenjang adalah", luas_jg)