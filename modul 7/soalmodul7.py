# # soal1
# # Menggunakan dictionary untuk menyimpan jumlah alat kesehatan yang dipinjam Heni
# alat_pinjaman = {
#     "pengukur_tek_darah": 2,  
#     "termometer": 3,         
#     "stetoskop": 4,           
#     "inhaler": 0              
# }

# # Mengembalikan alat
# alat_pinjaman["pengukur_tek_darah"] -= 1  # Heni mengembalikan 1 pengukur tekanan darah
# alat_pinjaman["termometer"] -= 2          # Heni mengembalikan 2 termometer

# # Menukar stetoskop dengan inhaler
# alat_pinjaman["stetoskop"] -= 3           # Heni menukar 3 stetoskop
# alat_pinjaman["inhaler"] += 2             # Heni mendapatkan 2 inhaler sebagai pengganti stetoskop

# # Menampilkan hasil alat yang dipinjam saat ini
# print("Alat kesehatan yang dipinjam Heni saat ini:")
# for alat, jumlah in alat_pinjaman.items():
#     print(f"{alat}:{jumlah}")

# soal2
# Set yang berisi nama siswa yang mengikuti klub Basket dan Renang
klub_basket = {"Ali", "Budi", "Charlie", "Dina", "Eka"}
klub_renang = {"Budi", "Charlie", "Feni", "Gina", "Dina"}

# a. Menampilkan daftar siswa yang mengikuti kedua klub
siswa_kedua_klub = klub_basket & klub_renang  # Operator & untuk irisan set
print("Siswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)

# b. Menampilkan daftar siswa yang hanya mengikuti satu klub saja
siswa_hanya_satu_klub = (klub_basket | klub_renang) - siswa_kedua_klub  # Operator | untuk gabungan dan - untuk selisih
print("Siswa yang hanya mengikuti satu klub:")
print(siswa_hanya_satu_klub)

# c. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
siswa_unik = (klub_basket | klub_renang)
print("menampilkan daftar siswa unik yang mengikuti satu dari kedua klub tersebut")
print(siswa_unik)

# d. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu klub
jumlah_siswa_unik = len(siswa_unik)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:")
print(jumlah_siswa_unik)


# # soal3
# def buat_kelas_baru(jumlah_kelas):
#     #Membuat kelas baru dengan nama kelas yang sesuai.
#     return {
#         'nama_kelas': f"Kelas {jumlah_kelas}",
#         'siswa': []
#     }

# def tambah_siswa_ke_kelas(kelas_list, nama_siswa, asal_sekolah, plot_bimbingan):
#     # Menambahkan siswa ke kelas yang sudah ada atau membuka kelas baru.
#     # Mencari kelas yang masih memiliki ruang
#     for kelas in kelas_list:
#         if len(kelas['siswa']) < 3:
#             kelas['siswa'].append({
#                 'nama': nama_siswa,
#                 'sekolah': asal_sekolah,
#                 'plot': plot_bimbingan
#             })
#             print(f"Siswa {nama_siswa} berhasil ditambahkan ke {kelas['nama_kelas']}.")
#             return

#     # Jika tidak ada kelas yang bisa menampung, buat kelas baru
#     kelas_baru = buat_kelas_baru(len(kelas_list) + 1)
#     kelas_baru['siswa'].append({
#         'nama': nama_siswa,
#         'sekolah': asal_sekolah,
#         'plot': plot_bimbingan
#     })
#     kelas_list.append(kelas_baru)
#     print(f"Siswa {nama_siswa} berhasil ditambahkan ke {kelas_baru['nama_kelas']}.")

# def tampilkan_semua_kelas(kelas_list):
#     # Menampilkan semua kelas dan siswa yang ada.
#     if not kelas_list:
#         print("Belum ada kelas yang terbentuk.")
#         return

#     for kelas in kelas_list:
#         print(f"{kelas['nama_kelas']}:")
#         for siswa in kelas['siswa']:
#             print(f"Nama: {siswa['nama']}, Sekolah: {siswa['sekolah']}, Plot: {siswa['plot']}")
#         print("-" * 20)

# def perbarui_data_siswa(kelas_list, nama_lama, nama_baru=None, sekolah_baru=None, plot_baru=None):
#     # Memperbarui data siswa yang sudah ada.
#     ditemukan = False
#     for kelas in kelas_list:
#         for siswa in kelas['siswa']:
#             if siswa['nama'] == nama_lama:
#                 if nama_baru:
#                     siswa['nama'] = nama_baru
#                 if sekolah_baru:
#                     siswa['sekolah'] = sekolah_baru
#                 if plot_baru:
#                     siswa['plot'] = plot_baru
#                 print(f"Data siswa {nama_lama} berhasil diperbarui.")
#                 ditemukan = True
#                 break
#         if ditemukan:
#             break
#     if not ditemukan:
#         print(f"Siswa dengan nama {nama_lama} tidak ditemukan.")

# def hapus_siswa(kelas_list, nama_siswa):
#     # Menghapus siswa dari kelas.
#     ditemukan = False
#     for kelas in kelas_list:
#         for siswa in kelas['siswa']:
#             if siswa['nama'] == nama_siswa:
#                 kelas['siswa'].remove(siswa)
#                 print(f"Siswa {nama_siswa} berhasil dihapus.")
#                 ditemukan = True
#                 break
#         if ditemukan:
#             break
#     if not ditemukan:
#         print(f"Siswa dengan nama {nama_siswa} tidak ditemukan.")

# # Fungsi utama untuk menjalankan program
# def utama():
#     kelas_list = []  # List untuk menyimpan semua kelas
#     while True:
#         print("Menu:")
#         print("1. Tambah Siswa")
#         print("2. Lihat Semua Kelas")
#         print("3. Update Data Siswa")
#         print("4. Hapus Siswa")
#         print("5. Keluar")
#         pilihan = input("Pilih menu: ")

#         if pilihan == '1':
#             nama = input("Nama Siswa: ")
#             sekolah = input("Asal Sekolah: ")
#             plot = input("Plot Bimbingan: ")
#             tambah_siswa_ke_kelas(kelas_list, nama, sekolah, plot)
#         elif pilihan == '2':
#             tampilkan_semua_kelas(kelas_list)
#         elif pilihan == '3':
#             nama_lama = input("Nama Siswa yang ingin diubah: ")
#             nama_baru = input("Nama Baru (tekan Enter jika tidak ada perubahan): ")
#             sekolah_baru = input("Asal Sekolah Baru (tekan Enter jika tidak ada perubahan): ")
#             plot_baru = input("Plot Baru (tekan Enter jika tidak ada perubahan): ")
#             perbarui_data_siswa(kelas_list, nama_lama, nama_baru, sekolah_baru, plot_baru)
#         elif pilihan == '4':
#             nama = input("Nama Siswa yang ingin dihapus: ")
#             hapus_siswa(kelas_list, nama)
#         elif pilihan == '5':
#             print("Terima kasih! Program selesai.")
#             break
#         else:
#             print("Pilihan tidak valid!")

# utama()