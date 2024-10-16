#Dua variabel awal
suku_5 = 11  # Suku ke-5 adalah 11
jumlah_8_12 = 52  # Jumlah suku ke-8 dan suku ke-12 adalah 52

#menghitung beda (b)
b = (jumlah_8_12 - 2*suku_5) / 10

# Mencari suku pertama (a)
a = suku_5 - 4*b

# Menghitung jumlah 8 suku pertama
n = 8
jumlah_8_suku = n * (2*a + (n-1)*b) / 2

# Menampilkan hasil
print(f"Suku pertama (a) = {a}")
print(f"Beda (b) = {b}")
print(f"Jumlah 8 suku pertama = {jumlah_8_suku}")

