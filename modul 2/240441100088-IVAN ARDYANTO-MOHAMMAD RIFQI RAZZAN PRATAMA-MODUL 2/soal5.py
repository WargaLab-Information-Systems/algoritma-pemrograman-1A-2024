# input total belanja
total_belanja = int(input("Masukkan total belanja anda: ")) 

# input apakah user memiliki member/tidak
apakah_member = input("Apakah anda memiliki kartu memeber?: (yes/no) ") 

# Inisialisasi total diskon
total_diskon = 0

# Jika user memiliki member, maka diberi diskon sebesar 15%
if apakah_member == "yes":
    total_diskon += 15

# Jika total belanja user lebih dair 500.000, maka akan diberi diskon sebesar 10%
if total_belanja > 500000:
    total_diskon += 10

# Rumus perhitungan diskon
total_harga_diskon = total_belanja - (total_diskon / 100 * total_belanja)

# input nama pembeli
nama_pembeli = input("Masukkan nama anda: ")

# input usia pembeli
usia_pembeli = int(input("Masukkan usia anda: "))

# Jika usia pembeli dibawah 18, maka tidak akan menjalankan proses transaksi
if (usia_pembeli < 18):
    print("Maaf usia anda belum mencukupi")

# Jika usia pembeli diatas 18, maka akan melanjutkan proses transaksi
else:
    print(f"Nama pembeli: {nama_pembeli}")
    print(f"Diskon yang anda dapatkan:) {total_diskon}%")
    print(f"Total harga sebelum diskon: {total_belanja}")
    print(f"Total harga setelah diskon: {total_harga_diskon}")