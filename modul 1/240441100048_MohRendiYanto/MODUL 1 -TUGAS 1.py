# Volume Balok
panjang = 20 
lebar = 13 
tinggi_Balok = 7

# Volume Tabung 
diameter = 14
luas_selimut = 440
phi = 22/7

#rumus mencari jari - jari
jari_jari = diameter / 2

# rumus mencari tinggi tabung
tinggi_Tabung = luas_selimut / (2*phi*jari_jari)

# Menghitung Volume Balok 
volume_balok = int (panjang * lebar * tinggi_Balok)
print("Volume celengan balok Andi adalah", volume_balok, "cm")

# Menghitung Volume Tabung
volume_tabung = int (phi * jari_jari**2 * tinggi_Tabung)
print ("Volume celengen tabung Andi adalah", volume_tabung, "cm")
