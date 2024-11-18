# # soal no 1
# alat_kesehatan = {
#     "Alat pengukur tekanan darah": 0,
#     "Termometer": 0,
#     "Stetoskop": 0,
#     "Inhaler": 0
# }
# def pinjam(alat, jumlah):
#     if alat in alat_kesehatan:
#         alat_kesehatan[alat] += jumlah
#         print(f"{jumlah} {alat} dipinjam.")
#     else:
#         print(f"{alat} tidak ditemukan di daftar alat kesehatan.")

# def kembalikan(alat, jumlah):
#     if alat in alat_kesehatan:
#         if alat_kesehatan[alat] >= jumlah:
#             alat_kesehatan[alat] -= jumlah
#             print(f"{jumlah} {alat} dikembalikan.")
#         else:
#             print(f"Jumlah pengembalian {alat} melebihi jumlah yang dipinjam.")
#     else:
#         print(f"{alat} tidak ditemukan di daftar alat kesehatan.")

# def tukar(alat_awal, jumlah_awal, alat_baru, jumlah_baru):
#     if alat_awal in alat_kesehatan and alat_baru in alat_kesehatan:
#         if alat_kesehatan[alat_awal] >= jumlah_awal:
#             alat_kesehatan[alat_awal] -= jumlah_awal
#             alat_kesehatan[alat_baru] += jumlah_baru
#             print(f"{jumlah_awal} {alat_awal} ditukar dengan {jumlah_baru} {alat_baru}.")
#         else:
#             print(f"Jumlah {alat_awal} yang dimiliki tidak cukup untuk ditukar.")
#     else:
#         print(f"Salah satu alat tidak ditemukan di daftar alat kesehatan.")

# def lihat_data():
#     print("\nAlat Kesehatan yang Masih Dipinjam:")
#     for alat, jumlah in alat_kesehatan.items():
#         if jumlah > 0:
#             print(f"{alat}: {jumlah}")
#     if all(jumlah == 0 for jumlah in alat_kesehatan.values()):
#         print("Tidak ada alat yang sedang dipinjam.")


# while True:
#     print("\n=== DATA PEMINJAMAN BARANG KESEHATAN ===")
#     print("1. Pinjam Alat")
#     print("2. Kembalikan Alat")
#     print("3. Tukar Alat")
#     print("4. Lihat Alat yang Dipinjam")
#     print("5. Keluar")
    
#     pilihan = input("Pilih menu (1-5): ")
    
#     if pilihan == "1":
#         alat = input("Masukkan nama alat yang dipinjam: ")
#         jumlah = int(input("Masukkan jumlah alat yang dipinjam: "))
#         pinjam(alat, jumlah)
#     elif pilihan == "2":
#         alat = input("Masukkan nama alat yang dikembalikan: ")
#         jumlah = int(input("Masukkan jumlah alat yang dikembalikan: "))
#         kembalikan(alat, jumlah)
#     elif pilihan == "3":
#         alat_awal = input("Masukkan nama alat yang ditukar: ")
#         jumlah_awal = int(input("Masukkan jumlah alat yang ditukar: "))
#         alat_baru = input("Masukkan nama alat pengganti: ")
#         jumlah_baru = int(input("Masukkan jumlah alat pengganti: "))
#         tukar(alat_awal, jumlah_awal, alat_baru, jumlah_baru)
#     elif pilihan == "4":
#         lihat_data()
#     elif pilihan == "5":
#         print("Program selesai. Terima kasih!")
#         break
#     else:
#         print("Pilihan tidak valid, silakan coba lagi.")


# soal no 2

siswa_basket = {"Ali", "Budi", "Citra", "Dewi", "Eka"}
siswa_renang = {"Budi", "Dewi", "Fahri", "Gita", "Hana"}

siswa_kedua_klub = siswa_basket & siswa_renang
print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

siswa_hanya_basket = siswa_basket - siswa_renang
siswa_hanya_renang = siswa_renang - siswa_basket
print("Siswa yang hanya mengikuti klub Basket:", siswa_hanya_basket)
print("Siswa yang hanya mengikuti klub Renang:", siswa_hanya_renang)

siswa_unik = siswa_basket | siswa_renang
print("Siswa yang mengikuti setidaknya satu klub:", siswa_unik)


jumlah_siswa_unik = len(siswa_unik)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)




# # # soal no 3

# siswa_data = {}
# max_siswa_per_kelas = 3

# def tambah_siswa():
#     nama = input("Masukkan nama siswa: ")
#     kelas = input("Masukkan kelas siswa: ")


#     if kelas not in siswa_data:
#         siswa_data[kelas] = []  

#     if len(siswa_data[kelas]) >= max_siswa_per_kelas:
#         print(f"Kelas {kelas} sudah penuh (maksimum {max_siswa_per_kelas} siswa). Tidak dapat menambah siswa masukan ke kelas baru.")
#         return
    
#     asal_sekolah = input("Masukkan asal sekolah siswa: ")
#     bimbingan_grup = input("Masukkan grup bimbingan siswa: ")

#     siswa_data[kelas].append({
#         'nama': nama,
#         'asal_sekolah': asal_sekolah,
#         'bimbingan_grup': bimbingan_grup
#     })
#     print(f"Siswa {nama} berhasil ditambahkan ke kelas {kelas}!")

# def lihat_semua_siswa():
#     if siswa_data:
#         print("Data siswa:")
#         for kelas, siswa_list in siswa_data.items():
#             print(f"Kelas {kelas}:")
#             for siswa in siswa_list:
#                 print(f"  Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}, Grup Bimbingan: {siswa['bimbingan_grup']}")
#     else:
#         print("Belum ada siswa yang terdaftar.")

# def ubah_siswa():
#     nama = input("Masukkan nama siswa yang ingin diubah: ")
#     ditemukan = False

#     for kelas, siswa_list in siswa_data.items():
#         for siswa in siswa_list:
#             if siswa['nama'] == nama:
#                 ditemukan = True
#                 kelas_baru = input(f"Masukkan kelas baru untuk {nama}: ")
#                 asal_sekolah_baru = input(f"Masukkan asal sekolah baru untuk {nama}: ")
#                 bimbingan_grup_baru = input(f"Masukkan grup bimbingan baru untuk {nama}: ")
                
#                 siswa['asal_sekolah'] = asal_sekolah_baru
#                 siswa['bimbingan_grup'] = bimbingan_grup_baru
                
#                 if kelas != kelas_baru:
#                     siswa_data[kelas].remove(siswa)
#                     if kelas_baru not in siswa_data:
#                         siswa_data[kelas_baru] = []
#                     siswa_data[kelas_baru].append(siswa)
                
#                 print(f"Data siswa {nama} berhasil diubah!")
#                 break
#         if ditemukan:
#             break
    
#     if not ditemukan:
#         print(f"Siswa dengan nama {nama} tidak ditemukan.")

# def hapus_siswa():
#     nama = input("Masukkan nama siswa yang ingin dihapus: ")
#     ditemukan = False

#     # Mencari siswa di seluruh kelas
#     for kelas, siswa_list in siswa_data.items():
#         for siswa in siswa_list:
#             if siswa['nama'] == nama:
#                 ditemukan = True
#                 siswa_data[kelas].remove(siswa)
#                 print(f"Siswa {nama} berhasil dihapus dari kelas {kelas}.")
#                 break
#         if ditemukan:
#             break
    
#     if not ditemukan:
#         print(f"Siswa dengan nama {nama} tidak ditemukan.")

# def menu_utama():
#     while True:
#         print("\n===== DATA BIMBINGAN INTENSIF GEMA RIPAH =====")
#         print("1. Tambah Siswa")
#         print("2. Lihat Semua Siswa")
#         print("3. Ubah Data Siswa")
#         print("4. Hapus Siswa")
#         print("5. Keluar")
        
#         pilihan = input("Pilih menu (1-5): ")
#         if pilihan == '1':
#             tambah_siswa()
#         elif pilihan == '2':
#             lihat_semua_siswa()
#         elif pilihan == '3':
#             ubah_siswa()
#         elif pilihan == '4':
#             hapus_siswa()
#         elif pilihan == '5':
#             print("Keluar dari program.")
#             break
#         else:
#             print("Pilihan tidak valid, coba lagi.")

# menu_utama()

