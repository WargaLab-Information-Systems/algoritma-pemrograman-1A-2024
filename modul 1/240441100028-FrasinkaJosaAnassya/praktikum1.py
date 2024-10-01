# # # #soal 1
# # # diketahui balok:
p = 20  
l = 13    
tb = 7  
volume_balok = p* l * tb

# diketahui tabung:
diameter = 14  # cm
radius = diameter / 2
luas_selimut = 440  # cm³

# Menghitung tinggi tabung dari luas selimut
pi = 22/7
tinggi_tabung = luas_selimut / (2 * pi * radius)
# Menghitung volume tabung
volume_tabung = pi * radius ** 2 * tinggi_tabung

# Menampilkan hasil
print("Volume balok: ",volume_balok, "cm³")
print("Volume tabung: ",volume_tabung, "cm³")

# #soal 2
# u5 = 11
# u8_plus_u12 = 52

# #menghitung beda (b)
# b = (u8_plus_u12 - 2*u5) / 10

# # Mencari suku pertama (a)
# a = u5 - 4*b

# # Menghitung jumlah 8 suku pertama
# n = 8
# jumlah_8_suku = n * (2*a + (n-1)*b) / 2

# # Menampilkan hasil
# print(f"Suku pertama (a) = {a}")
# print(f"Beda (b) = {b}")
# print(f"Jumlah 8 suku pertama = {jumlah_8_suku}")

# #soal 3
# usd = 15.102
# jumlah_usd = 35
# jumlah_idr= jumlah_usd*usd
# print(f"Maka nominal yang didapatkan dengan mata uang adalah",jumlah_idr,"rupiah")

# #soal 4
# #jumlah orang
# orang = 7
# #jumlah orang yang dipilih
# orang_dipilih = 4
# #faktorial 7
# faktorial_7 = 7*6*5*4*3*2*1
# #faktorial 4
# faktorial_4 = 4*3*2*1
# #faktorial_3
# faktorial_3 = 3*2*1
# #banyak cara untuk membentuk sebuah tim darsono
# jumlah_cara= (faktorial_7)/(faktorial_4*faktorial_3)
# print(f"Banyaknya cara untuk membentuk sebuah tim darsono",jumlah_cara)

#jajar genjang
print("untuk menghitung luas jajar genjang ")
alas = int(input("Masukkan nilai alas jajar genjang : "))
tinggi = int(input("Masukkan nilai tinggi jajar genjang : "))
# Mencari luas jajar genjang, rumus ( L = a * t )
Luas = alas * tinggi
print(f"jadi luas jajar genjangnya adalah" , Luas)




