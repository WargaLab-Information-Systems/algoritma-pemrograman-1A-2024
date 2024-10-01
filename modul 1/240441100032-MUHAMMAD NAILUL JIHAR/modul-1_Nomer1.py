# Volume Balok
panjang = 20
lebar = 13
tinggi_Balok = 7

# Volume Tabung
diameter = 14
luas_Selimut = 440
phi = 22/7

#rumus mencari jari - jari
jari_Jari = diameter / 2

# rumus mencari tinggi tabung
tinggi_Tabung = luas_Selimut / (2*phi*jari_Jari)

# Menghitung Volume Balok
volume_balok = int (panjang * lebar * tinggi_Balok)
print("Volume celengan balok Andi adalah", volume_balok, "cm")

# Menghitung Volume Tabung
volume_tabung = int(phi * jari_Jari**2 * tinggi_Tabung)
print ("Volume celengan tabung Andi adalah", volume_tabung, "cm")