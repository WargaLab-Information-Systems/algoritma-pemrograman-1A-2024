# Tugas nomer 2
 
# Program untuk menghitung jumlah 8 suku pertama dari deret aritmatika tanpa pengulangan

# Diketahui
suku_5 = 11  # Suku ke-5 adalah 11
jumlah_8_12 = 52  # Jumlah suku ke-8 dan suku ke-12 adalah 52

# Menghitung nilai suku pertama (a) dan beda (d) berdasarkan informasi
# Persamaan 1: a + 4d = 11
# Persamaan 2: (a + 7d) + (a + 11d) = 52
# Dari persamaan 1: a = 11 - 4d
# Substitusi ke persamaan 2:
# (11 - 4d + 7d) + (11 - 4d + 11d) = 52
# 11 + 3d + 11 + 7d = 52
# 22 + 10d = 52
# 10d = 30
# d = 3

d = 3
a = 11 - 4 * d  # Suku pertama

# Menghitung jumlah 8 suku pertama dengan rumus Sn = n/2 * (2a + (n - 1)d)
n = 8
jumlah_suku_pertama = (n / 2) * (2 * a + (n - 1) * d)

# Output hasil
print(f"Jumlah nilai dari 8 suku pertama deret aritmatika tersebut adalah: {jumlah_suku_pertama}")
