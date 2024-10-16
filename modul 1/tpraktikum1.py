import math

# input menghitung volume balok
panjang = 20
lebar = 13
tinggi_balok = 7

# proses menghitung volume balok
volume_balok = panjang * lebar * tinggi_balok

# input menghitung volume tabung
diameter = 14 
r = diameter / 2
luas_selimut = 440 
tinggi_tabung = luas_selimut / 2 * math.pi * r 

# proses menghitung volume tabung
volume_tabung = math.pi * r**2 * tinggi_tabung

# output menghitung volume balok
print(f"Volume celengan Andi yang berbentuk balok adalah {volume_balok} ")

# output menghitung volume tabung
print(f"Volume celengan Andi yang berbentuk tabung adalah {volume_tabung} ")