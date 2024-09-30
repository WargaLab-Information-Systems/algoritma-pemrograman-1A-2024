# SOAL NOMOR 1

# BALOK
# diketahui
p_balok = 20
l_balok = 13
t_balok= 7

print("Diketahui :")
print("panjang balok : 20 cm")
print("lebar balok   : 13 cm")
print("tinggi balok  : 7 cm")

# Operasi Aritmatika
hasil1 = p_balok * l_balok * t_balok

# Hasil Ouput
print(f"Maka hasil dari volume balok tersebut adalah : {hasil1}cm3")

# TABUNG
# diketahui
ls = 440
d = 14
r = 7
phi = 22/7
print("Diketahui :")
print("luas selimut tabung : 440 cm")
print("diameter tabung     : 14 cm")
print("jari-jari tabung    : 7 cm")
print("phi tabung          : 7 cm")

# menentukan tinggi tabung/luas selimut
t_tabung = ls / (2 * phi * r)

# operasi aritmatika
hasil2 = phi * (r ** 2) * t_tabung

# hasil output
print(f"Maka volume dari tabung tersebut adalah : {hasil2}cm3")



# SOAL NOMOR 2

# diketahui
U5 = 11
U8_gab_U12 = 52
n = 8

print("diketahui :")
print("U5              = 11")
print("U8 gabungan U12 = 52")
print("beda (b)        = -1")
print("suku pertama (a)= 3")
print("n               = 8")
print("persamaan 1     : a + 4 = 11")
print("persamaan 2     : (a + 7b) + (a +11b) = 52")

# mencari beda (b)
# mensubtitusikan persamaan 1 ke persamaan 2
# a + 4b = 11
# a = 11 - 4b
# (11 - 4b + 7b) + (11 - 4b + 11b) = 52
# 11 + 3b + 11 + 7b                = 52
# 22 + 10b                         = 52
# 10b                              = 30
# b                                = 3

b = 3
a = 11 - 4 * b

# operasi aritmatika
jumlah_suku = (n / 2) * (2 * a + (n - 1) * b)

# hasi output
print(f"maka hasil dari jumlah suku ke-8 adalah : {jumlah_suku}")



# SOAL NOMOR 3

# diketahui
uang_suraji = 35
dollar_indo = 15.102 #kurs dollar to rupiah pada tgl 25/09/2024

print("diketahui :")
print("uang suraji =  USD35$")
print("USD1$       =  15.102")

# operasi aritmatika
hasil_kurs = uang_suraji * dollar_indo

# hasil ouput
print(f"maka hasil nilai tukar uang yang dimiliki suraji adalah : {hasil_kurs}")



# SOAL NOMOR 4

# diketahui
x = 7
y = 4
z = 3 #(hasil dari x-y)

print("diketahui:")
print("x       = 7")
print("y       = 4")
print("z (x-y) = 3")
print("c(7,4) = 7! / 4! * (7 - 4)!")
print("       = 7! / 4! * 3!")

faktorial_7 = 7 * 6 * 5
faktorial_3 = 3 * 2

# operasi aritmatika
combinasi = faktorial_7 / faktorial_3

# hasil output
print(f"maka banyak cara untuk memilih 4 orang dari 7 orang adalah : {combinasi} ")

