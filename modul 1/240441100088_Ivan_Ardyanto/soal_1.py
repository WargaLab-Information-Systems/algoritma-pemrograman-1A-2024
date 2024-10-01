#volume balok
panjang = 20
lebar = 13
tinggi = 7

#volume tabung
diameter = 14
luas_selimut = 440

#phi adalah rumus untuk mencari volume tabung dan tinggi tabung
phi = 22/7

#rumus mencari jari jari
jari_jari = diameter / 2

#rumus mencari tinggi tabung
tinggi_tabung = luas_selimut / (2*phi*jari_jari)


#menghitung volume balok
volume_balok = panjang * lebar * tinggi
print("vollume celengan balik andi adalah", volume_balok, "cm")

#menghitung volume tabung
volume_tabung = phi * 2 * jari_jari * tinggi_tabung
print ("volume celengan andi adalah", volume_tabung, "cm")
