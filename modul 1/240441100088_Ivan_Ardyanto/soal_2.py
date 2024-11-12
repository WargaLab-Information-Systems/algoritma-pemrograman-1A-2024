#Dua variabel awal
u5 = 11
u8_plus_u12 = 52

#menghitung beda (b)
b = (u8_plus_u12 - 2*u5) / 10

# Mencari suku pertama (a)
a = u5 - 4*b

# Menghitung jumlah 8 suku pertama
n = 8
jumlah_8_suku = n * (2*a + (n-1)*b) / 2

# Menampilkan hasil
print(f"Suku pertama (a) = {a}")
print(f"Beda (b) = {b}")
print(f"Jumlah 8 suku pertama = {jumlah_8_suku}")