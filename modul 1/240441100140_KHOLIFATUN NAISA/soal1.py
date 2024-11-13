# balok
print ("diketahui panjang balok 20cm")
print ("diketahui lebar balok 13cm")
print ("diketahui tinggi balok 7cm")
panjang_balok = input("diketahui ukuran panjang balok adalah: ")
lebar_balok = int(input("diketahui ukuran lebar balok adalah: "))
tinggi_balok = int(input("diketahui ukuran tinggi balok adalah: "))
hasil = int(panjang_balok*lebar_balok*tinggi_balok)
print(f"hasil dari volume balok adalah: {hasil}")

#tabung
print ("menghitung volume tabung")
print ("diketahui diameter tabung 14cm")
print ("diketahui luas selimut tabung 440cm")
print ("pi = 22/7")
#menghitung jari-jari: diameter/2
print ("14/2")
print (input("masukkan nilai diameter tabung: "))
print (input("masukkan nilai luas selimut tabung: "))
#menghitung tinggi luas selimut/ pi jari-jari
diameter_tabung = 14
luas_selimut = 440
pi = 22/7
jari_jari = diameter_tabung / 2
# Menghitung tinggi dari luas selimut
tinggi_luas_selimut = luas_selimut / (2 * pi * jari_jari)
# Menghitung volume
hasil = pi * (jari_jari ** 2) * tinggi_luas_selimut
print(f"hasil dari volume tabung adalah: {int(hasil)}")
