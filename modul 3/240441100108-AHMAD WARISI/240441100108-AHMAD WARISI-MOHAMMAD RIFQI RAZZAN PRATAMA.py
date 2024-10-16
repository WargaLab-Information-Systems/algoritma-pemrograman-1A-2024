

# Program 3 angka terakhir NIM
t = 5

# Mencetak angka 1
for i in range(1, t + 1):
    for j in range(1, t + 1):
        if (j == t or (i == t//1 + 1 and j == t/1 + 1)):
            print("1", end="")
        else:
            print(" ", end="")
    print()
print ()

# Mencetak angka 0
for i in range(1, t + 1):
    for j in range(1, t + 1):
        if (i == 1 or i == t or
            (j == 1 and i != 1 and i != t) or
            (j == t and i != 1 and i != t)):
            print("0", end="")
        else:
            print(" ", end="")
    print()
print ()

# Mencetak angka 8
for i in range(1,t + 1):
    for j in range(1,t+ 1):
        if (i == 1 or i == t or i == t/5 + 2 or 
            (j == 1 and i <= t// 5 + 3) or 
            (j == t and i > t // 5)):
            print("8", end="")
        else:
            print(" ", end="")
    print()

# Program untuk membalikkan urutan angka bulat
angka = int(input("Masukkan angka bulat positif : "))

angka_terbalik = 0

# Proses membalikkan angka
while angka > 0:
        digit = angka % 10
        angka_terbalik = (angka_terbalik * 10) + digit
        angka = angka // 10




# Menampilkan hasil
        print("Angka yang sudah dibalik:", angka_terbalik)

# Program denda toko penyewaan DVD
while True:
    # Input lama peminjaman
    lama_pinjam_input = int(input("Masukkan lama peminjaman DVD (dalam hari): "))

    if lama_pinjam_input <0 :
        print("Mohon masukkan angka yang valid.")
        continue
    
    lama_pinjam = int(lama_pinjam_input)
    if lama_pinjam < 0:
        print("Mohon masukkan angka positif.")
        continue

    # Variabel untuk menghtung 
    batas_pinjam = 5
    denda_per_hari = 2500
    denda_tambahan = 5500
    denda_tambahan2 = 5

    # menghitung denda
    if lama_pinjam <= batas_pinjam:
        total_denda = 0
    else:
        keterlambatan = lama_pinjam - batas_pinjam
        denda_normal = keterlambatan * denda_per_hari
        
        if keterlambatan > 10:
            lewat_10_hari = (keterlambatan - 10) /denda_tambahan2
            denda_tambahan_total = lewat_10_hari * denda_tambahan
            total_denda = denda_normal + denda_tambahan_total
        else:
            total_denda = denda_normal

    # Menampilkan hasil
    print("Total denda yang harus dibayar Rp:",total_denda)
    
    # Menanyakan apakah ingin menghitung lagi
    lanjut = input("Apakah Anda ingin menghitung denda lagi? (ya/tidak): ")
    if lanjut != 'ya':
        print("Program Selesai.")
        break