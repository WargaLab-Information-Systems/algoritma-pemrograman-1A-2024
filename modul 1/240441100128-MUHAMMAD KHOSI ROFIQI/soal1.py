#VB
p = 20
l = 13
tb = 7

#VT
diameter = 14
luas_selimut = 440
phi = 22/7
#(phi adalah kunci rumus mencari tabung)

#RUMUS MENCARI JARI - JARI
jari_jari = diameter / 2

#RUMUS MENCARI TINGGI TABUNG
tinggi_tabung = luas_selimut / (2*phi*jari_jari)

#MENGHITUNG VOLUME BALOK
volume_balok = p * l * tb
print("jadi volume celengan balok andi adalah", volume_balok, "cm")

#MENGHITUNG VOLUME TABUNG
volume_tabung = phi * 2 * jari_jari * tinggi_tabung
print ("jadi volume celengan tabung andi ", volume_tabung, "cm")