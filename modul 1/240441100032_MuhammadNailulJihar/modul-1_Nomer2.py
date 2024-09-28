# Informasi yang diketahui
suku_ke_5 = 11
Suku_8_12 = 52

# Langkah 1: Menghitung beda (d) dari deret aritmatika
d = (Suku_8_12 - 2 * suku_ke_5) / 4

# Langkah 2: Menghitung suku pertama (a)
a = suku_ke_5 - 4 * d

# Langkah 3: Menghitung jumlah 8 suku pertama
n = 8
Sn = (n / 2) * (2 * a + (n - 1) * d)

# Menampilkan hasil
print("Suku pertama (a):", a)
print("Beda (d):", d )
print("Jumlah 8 suku pertama:", Sn)