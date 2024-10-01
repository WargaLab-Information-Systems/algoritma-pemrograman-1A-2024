# Input
a5 = 11
a8_plus_a12 = 52

# Tentukan nilai d (beda antara suku-suku)
d = (a8_plus_a12 - 2 * a5) / 4

# Tentukan nilai a1 (suku pertama)
a1 = a5 - 4 * d

# Hitung jumlah nilai 8 suku pertama
jumlah_suku = 0
for n in range(1, 9):
    an = a1 + (n - 1) * d
    jumlah_suku += an

print("Jumlah nilai 8 suku pertama:", jumlah_suku)