# soal 1 
# Program untuk mencetak bentuk angka berdasarkan NIM yang dimasukkan

# Pola x untuk setiap digit
patterns = {
    '0': [
        " xxx ",
        "x   x",
        "x   x",
        "x   x",
        " xxx "
    ],
    '1': [
        "  x  ",
        " xx  ",
        "  x  ",
        "  x  ",
        " xxxx"
    ],
    '2': [
        " xxx ",
        "    x",
        " xxx ",
        "x    ",
        " xxx "
    ],
    '3': [
        " xxx ",
        "    x",
        " xxx ",
        "    x",
        " xxx "
    ],
    '4': [
        "x   x",
        "x   x",
        " xxxx",
        "    x",
        "    x"
    ],
    '5': [
        " xxx ",
        "x    ",
        " xxx ",
        "    x",
        " xxx "
    ],
    '6': [
        " xxx ",
        "x    ",
        " xxx ",
        "x   x",
        " xxx "
    ],
    '7': [
        " xxx ",
        "    x",
        "   x ",
        "  x  ",
        " x   "
    ],
    '8': [
        " xxx ",
        "x   x",
        " xxx ",
        "x   x",
        " xxx "
    ],
    '9': [
        " xxx ",
        "x   x",
        " xxx ",
        "    x",
        " xxx "
    ]
}

# Meminta input NIM dari pengguna 
nim_terakhir = input(" Silakan Masukkan NIM terakhir anda : ")

# Menggunakan loop untuk mencetak pola
for i in range(5):
    for digit in nim_terakhir:
        print(patterns[digit][i], end="  ")  # Spasi antara angka
    print()  # Pindah ke baris berikutnya



# soal 2
# Input angka bulat dari pengguna
angka = int(input("silakan Masukkan angka bulat: "))

# Inisialisasi variabel untuk menyimpan hasil
hasil = 0

# while loop untuk membalikkan urutan angka
while angka > 0:
    # Ambil digit terakhir dari angka
    digit = angka % 10
    # Tambahkan digit ke hasil
    hasil = hasil * 10 + digit
    # Hapus digit terakhir dari angka
    angka = angka // 10

# Cetak hasil
print("Angka yang dibalik: ", hasil)


# soal 3
# Inisialisasi variabel untuk melacak apakah pengguna ingin melanjutkan
continue_perhitungan = 'iya'

while continue_perhitungan:
    # Masukkan variabel
    rental_hari = int(input("masukan lama waktu penyewaan (hari) : "))
    # Hitung biaya keterlambatan dasar
    biaya_terlambat_dasar = 0
    if rental_hari > 5:
        biaya_terlambat_dasar = (rental_hari - 5) * 2500
    # Hitung biaya keterlambatan tambahan
    biaya_keterlambatan_tambahan = 0
    if rental_hari - 5 > 10:
        biaya_keterlambatan_tambahan = ((rental_hari - 5 ) // 5) * 5500 
    # Hitung total biaya keterlambatan
    total_biaya_terlambat = biaya_terlambat_dasar + biaya_keterlambatan_tambahan
    # Cetak total biaya keterlambatan
    print("jadi total denda nya adalah : Rp", total_biaya_terlambat)
    # Tanyakan kepada pengguna apakah mereka ingin menghitung ulang
    tanggapan = input("apa anda mau menghitungnya kembali (iya atau tidak) :")
    if tanggapan.lower() == 'iya':
        continue
    else:
        # Set the flag to False to exit the loop
        
        print("terimakasih telah menyewa dvd di sini :)")
        break