#celengan balok
# panjang = 20
# lebar = 13
# tinggi = 7
panjang = int(input("masukkan panjang balok :"))
lebar = int(input("masukkan lebar balok :"))
tinggi = int(input("masukkan tinggi balok :"))
volume = panjang*lebar*tinggi
print(f"volume celengan balok milik Andi adalah {volume} cm3")

#celengan tabung
diameter = int(input("masukkan diameter tabung :"))
luasselimut = int(input("masukkan luas selimut :"))
jarijari = diameter/2
phi = 22/7
tinggi = luasselimut/(2*phi*jarijari)
volume = phi*jarijari**2*tinggi

print(f"volume celengan tabung milik Andi adalah {volume} cm3")