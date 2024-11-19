# soal 1
# Menggunakan dictionary untuk mencatat jumlah alat yang dipinjam
# alat_kesehatan = {
#     "pengukur tekanan darah": 0,
#     "termometer": 0,
#     "stetoskop": 0,
#     "inhaler": 0
# }
# def tambah_alat():
#     jenis = input("Masukkan jenis alat kesehatan: ")
#     jumlah = int(input(f"Masukkan jumlah {jenis} yang ingin ditambahkan: ")) #pengguna untuk memasukkan jumlah alat kesehatan yang ingin ditambahkan
#     if jenis in alat_kesehatan:
#         alat_kesehatan[jenis] += jumlah
#     else:
#         alat_kesehatan[jenis] = jumlah
#     print(f"{jumlah} {jenis} berhasil ditambahkan.")

# def Mengembalikan_alat(): #fungsi ini akan mengembalikan alat yang ada 
#     jenis = input("Masukkan jenis alat kesehatan: ")
#     jumlah = int(input(f"Masukkan jumlah {jenis} yang ingin dikembalikan: "))
#     if jenis in alat_kesehatan and alat_kesehatan[jenis] >= jumlah:
#         alat_kesehatan[jenis] -= jumlah
#         if alat_kesehatan[jenis] == 0:
#             alat_kesehatan.pop(jenis)
#         print(f"{jumlah} {jenis} berhasil dikurangi.")
#     else:
#         print("Gagal mengurangi. Pastikan jenis dan jumlah alat benar.")

# def tukar_alat(): # fungsi ini akan menukar alat yang ada
#     jenis_awal = input("Masukkan jenis alat yang ingin ditukar: ")
#     jumlah_awal = int(input(f"Masukkan jumlah {jenis_awal} yang ingin ditukar: "))
#     jenis_baru = input("Masukkan jenis alat baru: ")
#     jumlah_baru = int(input(f"Masukkan jumlah {jenis_baru} yang ingin ditambahkan: "))

#     if jenis_awal in alat_kesehatan and alat_kesehatan[jenis_awal] >= jumlah_awal:
#         alat_kesehatan[jenis_awal] -= jumlah_awal
#         if alat_kesehatan[jenis_awal] == 0:
#             alat_kesehatan.pop(jenis_awal)

#         if jenis_baru in alat_kesehatan:
#             alat_kesehatan[jenis_baru] += jumlah_baru
#         else:
#             alat_kesehatan[jenis_baru] = jumlah_baru
        
#         print(f"{jumlah_awal} {jenis_awal} berhasil ditukar dengan {jumlah_baru} {jenis_baru}.")
#     else:
#         print(f"Gagal menukar. Pastikan jumlah {jenis_awal} yang dimasukkan benar dan tersedia.")
# def tampilkan_alat():  # fungsi menampilkan semua alat kesehatan yang ada saat ini
#     print("\nAlat kesehatan yang dipinjam saat ini:")
#     if alat_kesehatan:
#         for jenis, jumlah in alat_kesehatan.items(): 
#             print(f"{jenis}: {jumlah} buah")
#     else:
#         print("Tidak ada alat yang dipinjam.")


# while True:
#     print("\n=== Menu ===")
#     print("1. Tambah alat kesehatan")
#     print("2. Mengembalikan alat kesehatan")
#     print("3. Tukar alat kesehatan")
#     print("4. Tampilkan alat kesehatan")
#     print("5. Keluar")
#     pilihan = input("Pilih menu (1/2/3/4/5): ")

#     if pilihan == "1":
#         tambah_alat()
#     elif pilihan == "2":
#         Mengembalikan_alat()
#     elif pilihan == "3":
#         tukar_alat()
#     elif pilihan == "4":
#         tampilkan_alat()
#     elif pilihan == "5":
#         print("program telah selesai.")
#         print("Terima kasih")
#         break
#     else:
#         print("Pilihan tidak valid.")


# soal no 2
# membuat set berisi data siswa yang mengikuti klub basket dan renang
basket =  {'lia','Windi','citra','Yesica','Rendi','Agung','Jefri'}
renang =  {'citra','Dimas','Agung','Naisa','Eka','Bita','Rendi'}


# daftar siswa yang mengikuti kedua klub
print("siswa yang mengikuti klub basket dan renang:\n",basket.intersection(renang))

# daftar siswa yang mengikuti satu klub
a = basket.difference(renang) # selisih
b = renang.difference(basket)
gabung = a.union(b)
print("siswa yang mengikuti satu klub:\n",basket.union(renang))
# daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub
print("\n daftar semua siswa unik yang setidaknya mengikuti satu dari kedua klub:\n",basket.union(renang))

# jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub
print("\n jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:",len(basket.union(renang)))

#  soal no 3
# data = {}

# #fungsi untuk menghitung kelas
# def menghitungkelas():
#     jmlsiswa = 0  
#     for siswa in data.items():
#         jmlsiswa += len(siswa)

#     return (jmlsiswa // 3) + 1

# #fungsi untuk menambah siswa
# def create():
#     nama = input("Masukkan nama: ")
#     sekolah = input("Masukkan asal sekolah: ")
#     plotting = input("Masukkan plotting: ")

#     kelas = menghitungkelas()
#     kelaske = data.get(f"Kelas {kelas}", [])

#     if len(kelaske) >= 3:
#         kelas += 1
#         kelaske = []

#     if f"Kelas {kelas}" not in data:
#         data[f"Kelas {kelas}"] = []

#     data[f"Kelas {kelas}"].append({
#         "nama": nama,
#         "sekolah": sekolah,
#         "plotting": plotting
#     })
#     print(f"{nama} masuk Kelas ke-{kelas}.")

# #membuat fungsi read
# def read():
#     if not data:
#         print("Belum ada data siswa")
#     else:
#         print("\nData Siswa:")
#         for kelas, siswa in data.items():
#             print(f"{kelas}:")
#             for siswakelas in siswa:
#                 print(f"  - Nama: {siswakelas['nama']}, Asal Sekolah: {siswakelas['sekolah']}, Plotting: {siswakelas['plotting']}")


# #membuat fungsi update
# def update():
#     nama = input("Masukkan nama siswa yang ingin diperbarui: ")
#     found = False
#     for kelas, siswa in data.items():
#         for siswakelas in siswa:
#             if siswakelas["nama"] == nama:
#                 print(f"Siswa ditemukan di {kelas}.")
#                 siswakelas["sekolah"] = input("Masukkan asal sekolah baru: ")
#                 siswakelas["plotting"] = input("Masukkan plotting baru: ")
#                 print(f"Data siswa {nama} berhasil diperbarui.")
#                 found = True
#                 break
#         if found:
#             break
#     if not found:
#         print(f"{nama} tidak ditemukan.")

# #membuat fungsi delete
# def delete():
#     nama = input("Masukkan nama siswa ingin dihapus: ")
#     found = False
#     for kelas, siswa in data.items():
#         for siswakelas in siswa:
#             if siswakelas["nama"] == nama:
#                 print(f"Siswa ditemukan di {kelas}.")
#                 siswa.remove(siswakelas)
#                 print(f"{nama} berhasil dihapus.")
#                 if not siswa:
#                     del data[kelas]
#                 found = True
#                 break
#         if found:
#             break
#     if not found:
#         print(f"{nama} tidak ditemukan.")

# #jalankan fungsi
# while True:
#     print("\nSelamat datang di lembaga bimbingan intensif Gema Ripah")
#     print("1. Absen data siswa")
#     print("2. Lihat data siswa")
#     print("3. Perbarui data siswa")
#     print("4. Hapus data siswa")
#     print("5. Keluar")
#     pilihan = input("Masukkan menu pilihan Anda: ")
#     if pilihan == "1":
#          create()
#     elif pilihan == "2":
#         read()
#     elif pilihan == "3":
#            update()
#     elif pilihan == "4":
#         delete()
#     elif pilihan == "5":
#         print("Terimakasih")
#         break
#     else:
#         print("Input salah!")