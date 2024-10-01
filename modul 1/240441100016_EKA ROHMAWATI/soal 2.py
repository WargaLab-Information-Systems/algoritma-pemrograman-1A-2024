# Input nilai suku ke-5 dan jumlah suku ke-8 dan ke-12
suku_ke_5 = int(input("Masukkan nilai suku ke-5: "))
jumlah_suku_8_dan_12 = int(input("Masukkan jumlah suku ke-8 dan ke-12: "))

# Menggunakan brute force untuk mencari nilai beda (d)
for d in range(-100, 100):  # Mencoba nilai d dari -100 sampai 100
    a = suku_ke_5 - 4 * d  # Menghitung nilai suku pertama (a)
    if 2 * a + 18 * d == jumlah_suku_8_dan_12:  # Mengecek kesesuaian persamaan
        break

# Menghitung jumlah 8 suku pertama
n = 8
jumlah_suku_8 = (n / 2) * (2 * a + (n - 1) * d)

# Menampilkan hasil
print(f"Nilai suku pertama (a): {a}")
print(f"Nilai beda (d): {d}")
print(f"Jumlah 8 suku pertama dari deret aritmatika: {jumlah_suku_8}")