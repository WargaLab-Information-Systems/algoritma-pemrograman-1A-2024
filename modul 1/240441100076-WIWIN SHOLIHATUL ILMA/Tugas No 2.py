# Rumus untuk suku ke-n: an = a + (n-1)d
# Rumus untuk jumlah n suku pertama: Sn = (n/2) * (2a + (n-1)d)

# Informasi yang diberikan
a5 = 11
a8_plus_a12 = 52

# Langkah 1: Cari beda umum (d)
# a8 + a12 = 2a5 + 10d
# 52 = 2(11) + 10d
d = (52 - 2*11) / 10
print("Beda umum (d) =", d)

# Langkah 2: Cari suku pertama (a)
# a5 = a + 4d
# 11 = a + 4d
a = 11 - 4*d
print("Suku pertama (a) =", a)

# Langkah 3: Cari jumlah 8 suku pertama
# Sn = (n/2) * (2a + (n-1)d)
S8 = (8/2) * (2*a + (8-1)*d)
print("Jumlah 8 suku pertama =", S8)
