
# # balok
# print ("diketahui panjang balok 20cm")
# print ("diketahui lebar balok 13cm")
# print ("diketahui tinggi balok 7cm")
# panjang_balok = input("diketahui ukuran panjang balok adalah: ")
# lebar_balok = int(input("diketahui ukuran lebar balok adalah: "))
# tinggi_balok = int(input("diketahui ukuran tinggi balok adalah: "))
# hasil = int(panjang_balok*lebar_balok*tinggi_balok)
# print(f"hasil dari volume balok adalah: {hasil}")

# #tabung
# print ("menghitung volume tabung")
# print ("diketahui diameter tabung 14cm")
# print ("diketahui luas selimut tabung 440cm")
# print ("pi = 22/7")
# #menghitung jari-jari: diameter/2
# print ("14/2")
# print (input("masukkan nilai diameter tabung: "))
# print (input("masukkan nilai luas selimut tabung: "))
# #menghitung tinggi luas selimut/ pi jari-jari
# diameter_tabung = 14
# luas_selimut = 440
# pi = 22/7
# jari_jari = diameter_tabung / 2
# # Menghitung tinggi dari luas selimut
# tinggi_luas_selimut = luas_selimut / (2 * pi * jari_jari)
# # Menghitung volume
# hasil = pi * (jari_jari ** 2) * tinggi_luas_selimut
# print(f"hasil dari volume tabung adalah: {int(hasil)}")


# #no 2
# u5 = 11
# u8_ditambah_u12 = 52
# b = (u8_ditambah_u12-2*u5)/10
# a = u5-4*b
# n= 8
# jumlah_8_suku=n*(2*a+(n-1)*b)/2
# print(f"suku pertama adalah: {a}")
# print(f"beda suku adalah: {b}")
# print(f"jumlah 8 suku pertama adalah: {int(jumlah_8_suku)}")

#no 3
# print("uang kertas suraji sebanyak US35$")
# print("1$ = 15.102 Rp kurs rupiah pada tanggal 25 september")
# dollar = 35
# rupiah = 528.57
# hasil = rupiah/15.102
# #print(input("masukkan jumlah mata uang yang akan dikonferensi ke rupiah: "))
# print(f"hasil dari konferensi uang suraji adalah: {hasil} rupiah")
# #print("hasil dari konferensi uang suraji adalah: "+" rupiah")

#no 4
a = 10
b = 4
a_b = 3 #a-b
faktorial_a = 10*9*8*7*6*5*4*3*2*1
faktorial_b = 4*3*2*1
faktorial_a_b = 3*2*1 #a_b adalah a-b/selisih
kombinasi = faktorial_a/(faktorial_b*faktorial_a_b)
print(f"banyak cara untuk memilih {a} orang dari {b} orang adalah {int(kombinasi)}")
