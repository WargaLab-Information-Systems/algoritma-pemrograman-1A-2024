# Tugas nomer 1
panjang_balok = 20
lebar_balok = 13
tinggi_balok = 7
diameter_tabung = 14
luas_selimut_tabung = 440
jari_jari_tabung = 7

volume_balok = panjang_balok*lebar_balok*tinggi_balok
tinggi_tabung = luas_selimut_tabung / (2 * 22/7 * (diameter_tabung/2))
volume_tabung = 22/7 * (diameter_tabung / 2)**2 * tinggi_tabung

print("volume balok:", volume_balok, "cm3")
print("volume tabung:", volume_tabung, "cm3")

# Tugas nomer 2
 
# Program untuk menghitung jumlah 8 suku pertama dari deret aritmatika tanpa pengulangan

# Diketahui
# suku_5 = 11  # Suku ke-5 adalah 11
# jumlah_8_12 = 52  # Jumlah suku ke-8 dan suku ke-12 adalah 52

# Menghitung nilai suku pertama (a) dan beda (d) berdasarkan informasi
# Persamaan 1: a + 4d = 11
# Persamaan 2: (a + 7d) + (a + 11d) = 52
# Dari persamaan 1: a = 11 - 4d
# Substitusi ke persamaan 2:
# (11 - 4d + 7d) + (11 - 4d + 11d) = 52
# 11 + 3d + 11 + 7d = 52
# 22 + 10d = 52
# 10d = 30
# # d = 3

d = 3
a = 11 - 4 * d  # Suku pertama

# Menghitung jumlah 8 suku pertama dengan rumus Sn = n/2 * (2a + (n - 1)d)
n = 8
jumlah_suku_pertama = (n / 2) * (2 * a + (n - 1) * d)

# Output hasil
print(f"Jumlah nilai dari 8 suku pertama deret aritmatika tersebut adalah: {jumlah_suku_pertama}")

# tugas nomer 3

kurs_dollar = 15102 #kurs 1 dollar pada tanggal 25 september 2024
dollar_suraji= 35

total_rupiah_sanji = kurs_dollar*dollar_suraji

print("jadi, total uang sanji jika di konversi dari dollar ke rupiah adalah", total_rupiah_sanji, "rupiah")

# tugas nomer 4
# c(7,4) = 7! / 4! (7-4) !
    #    = 7! / 4! * 3!

# 7! = 7*6*5*4
# 4! = 4*3*2
# 3! = 3*2
# C(7,4) =

faktorial_7 = 7*6*5
faktorial_3 = 3*2

hasil_faktorial = faktorial_7 / faktorial_3

print("jadi hasil", hasil_faktorial, "cara untuk memilih 4 orang dari 7 orang")