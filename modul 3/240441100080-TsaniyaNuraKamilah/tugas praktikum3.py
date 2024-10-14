# tugas no.1
#  Meminta input ukuran size
size = int(input("Masukan Size (harus lebih dari 3): "))

# Mengecek jika size kurang dari 3
if size < 3:
    print("Size harus lebih dari 3.")
else:
    # Cetak angka 0
    for row in range(size):
        if row == 0 or row == size-1:
            print("x" * size)
        else:
            print("x" + "" * (size-2) + "x")
    print()

    # Cetak angka 8
    for row in range(size):
        if row == 0 or row == size-1 or row == size//2:
            print("x" * size)
        else:
            print("x" + " " * (size-2) + "x")
    print()

    # Cetak angka 0
    for row in range(size):
        if row == 0 or row == size-1:
            print("x" * size)
        else:
            print("x" + " " * (size-2) + "x")
    print()

# tugas no.2
# input
angka_bulat = input("masukkan sebuah angka bulat :")
#inimisialisasi variabel untuk menyimpan angka yang dibalik
angka_terbalik = ""
#perulangan untuk membalik urutan angka
for digit in angka_bulat:
    angka_terbalik = digit + angka_terbalik
print("angka yg dibalik adalah:",angka_terbalik)

# tugas no.3
# Meminta input lama waktu penyewaan dari pengguna 
ulang = "ya" 
# Inisialisasi variabel ulang untuk pertama kali

while ulang == "ya":
    lama_peminjaman = int(input("Masukkan lama waktu penyewaan (dalam hari): "))

    if lama_peminjaman > 5:
        hari_terlambat = lama_peminjaman - 5
        denda_per_hari = 2500
        total_denda = hari_terlambat * denda_per_hari

        if hari_terlambat > 10:
            sisa_hari_terlambat = hari_terlambat - 10
            total_denda += (sisa_hari_terlambat // 5) * 5500

        print(f"Total denda keterlambatan: Rp{total_denda}")
    else:
        print("Tidak ada denda karena penyewaan masih dalam batas waktu.")

    # Menanyakan apakah user ingin menghitung lagi tanpa menggunakan lower()
    ulang = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")

print("Program selesai.")

