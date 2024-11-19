# # # soal no 1
# data_karyawan = []
# def tambah_karyawan():
#     print("===== MASUKKAN DATA KARYAWAN =====")
#     nip = input("Masukkan NIP : ")
#     nama = input("Masukkan Nama : ")
#     alamat = input("Masukkan Alamat : ")
#     departemen = input("Masukkan Departemen : ")
#     jabatan = input("Masukkan Jabatan : ")

#     karyawan = {
#         "NIP": nip,
#         "Nama": nama,
#         "Alamat": alamat,
#         "Departemen": departemen,
#         "Jabatan": jabatan
#     }

#     data_karyawan.append(karyawan)
#     print("Berhasil ditambahkan...")

# def tampilkan_karyawan(data_karyawan):
#     print("===== DATA KARYAWAN =====")
#     if not data_karyawan:
#         print("Belum ada data karyawan yang di input..")
#     else:
#         for idx, karyawan in enumerate(data_karyawan, start=1):
#             print(f"{idx}. Nama       : {karyawan['Nama']}")
#             print(f"   NIP        : {karyawan['NIP']}")
#             print(f"   Alamat     : {karyawan['Alamat']}")
#             print(f"   Departemen : {karyawan['Departemen']}")
#             print(f"   Jabatan    : {karyawan['Jabatan']}")
#             print("-" * 30)

# def cari_karyawan(data_karyawan):
#     print("===== PENCARIAN KARYAWAN =====")
#     while True:
#         jenis = input("Masukkan jenis pencarian (1. NIP/ 2. Nama/ 3. Alamat/ 4. Departemen/ 5. Jabatan) : ")
#         if jenis == "1":
#             jenis = "NIP"
#             break
#         elif jenis == "2":
#             jenis = "Nama"
#             break
#         elif jenis == "3":
#             jenis = "Alamat"
#             break
#         elif jenis == "4":
#             jenis = "Departemen"
#             break
#         elif jenis == "5":
#             jenis = "Jabatan"
#             break
#         else:
#             print("Input invalid....")

#     nilai = input(f"Cari data {jenis} : ")

#     hasil = [karyawan for karyawan in data_karyawan if karyawan.get(jenis) and karyawan[jenis].lower() == nilai.lower()]
    
#     if hasil:
#         print("===== HASIL PENCARIAN =====")
#         for karyawan in hasil:
#             print(f"NIP        : {karyawan['NIP']}")
#             print(f"Nama       : {karyawan['Nama']}")
#             print(f"Alamat     : {karyawan['Alamat']}")
#             print(f"Departemen : {karyawan['Departemen']}")
#             print(f"Jabatan    : {karyawan['Jabatan']}")
#             print("-" * 30)
#     else:
#         print("Data tidak ditemukan..")

# def hapus_karyawan(data_karyawan):
#     print("===== HAPUS DATA KARYAWAN =====")
#     tampilkan_karyawan(data_karyawan)
    
#     # Meminta input nomor urut karyawan yang akan dihapus
#     pilihan = input("Pilih nomor urut karyawan yang ingin dihapus (misalnya 1, 2, 3, dll): ")
    
#     if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data_karyawan):
#         print("Nomor tidak valid. Silakan pilih nomor yang sesuai..")
#         return

#     # Menghapus data karyawan berdasarkan nomor urut yang dipilih
#     del data_karyawan[int(pilihan) - 1]
#     print("Data karyawan berhasil dihapus.")

# while True:
#     print("\n===== SELAMAT DATANG DI PT KESANA KEMARI =====")
#     print("1. Tambah Karyawan")
#     print("2. Cari Karyawan")
#     print("3. Daftar Karyawan")
#     print("4. Hapus Data Karyawan")
#     print("5. Keluar")
#     pilih = input("Silahkan pilih menu : ")

#     if pilih == "1":
#         tambah_karyawan()
#     elif pilih == "2":
#         cari_karyawan(data_karyawan)
#     elif pilih == "3":
#         tampilkan_karyawan(data_karyawan)
#     elif pilih == "4":
#         hapus_karyawan(data_karyawan)
#     elif pilih == "5":
#         print("Terima kasih! Program selesai.")
#         break
#     else:
#         print("Pilihan tidak valid. Silakan coba lagi.")


# # soal no 2
# data = []
# def daftar_buku():
#     print("\n===== DAFTAR BUKU =====")
#     print("1. Putri Duyung")
#     print("2. Bawang Putih & Bawang Merah")
#     print("3. Putri Malu")
#     print("4. Cerita Nusantara")

# def pilih_buku():
#     while True:
#         pilih = int(input("Silahkan pilih buku (1-4): "))
#         nama = input("Nama peminjam: ")
#         tanggal = input("Tanggal Pinjam (DD/MM/YYYY): ")
        
#         if pilih == 1:
#             judul = "Putri Duyung"
#             id_buku = 4235
#             break
#         elif pilih == 2:
#             judul = "Bawang Putih & Bawang Merah"
#             id_buku = 7765
#             break
#         elif pilih == 3:
#             judul = "Putri Malu"
#             id_buku = 8854
#             break
#         elif pilih == 4:
#             judul = "Cerita Nusantara"
#             id_buku = 3457
#             break
#         else:
#             print("Invalid, pilih angka antara 1 dan 4.")
#             continue
    
#     peminjaman = {
#         "nama": nama,
#         "id_buku": id_buku,
#         "judul": judul,
#         "tanggal": tanggal
#     }
    
#     data.append(peminjaman)
#     return peminjaman

# def tampilkan_peminjam():
#     print("\n===== DAFTAR PEMINJAM =====")
#     if not data:
#         print("Tidak ada peminjam buku saat ini.")
#     else:
#         for i, peminjaman in enumerate(data, start=1):
#             print(f"{i}. Nama: {peminjaman['nama']}, Judul Buku: {peminjaman['judul']}, Tanggal Pinjam: {peminjaman['tanggal']}")

# def edit_buku():
#     if not data:
#         print("Tidak ada data yang dapat diubah...")
#         return

#     print("\n===== DATA PEMINJAMAN =====")
#     for i, peminjaman in enumerate(data, start=1):
#         print(f"{i}. Nama: {peminjaman['nama']}, Judul Buku: {peminjaman['judul']}, Tanggal Pinjam: {peminjaman['tanggal']}")
    
#     pilihan = input("Pilih nomor yang ingin diubah: ")
#     if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data):
#         print("Nomor tidak valid.")
#         return

#     pilihan = int(pilihan) - 1
#     nama_baru = input("Masukkan nama baru: ")

#     daftar_buku()
#     pilih_baru = int(input("Silahkan pilih buku baru (1-4): "))
#     if pilih_baru == 1:
#         judul_baru = "Putri Duyung"
#         id_buku_baru = 4235
#     elif pilih_baru == 2:
#         judul_baru = "Bawang Putih & Bawang Merah"
#         id_buku_baru = 7765
#     elif pilih_baru == 3:
#         judul_baru = "Putri Malu"
#         id_buku_baru = 8854
#     elif pilih_baru == 4:
#         judul_baru = "Cerita Nusantara"
#         id_buku_baru = 3457
#     else:
#         print("Invalid")
#         return

#     data[pilihan]["nama"] = nama_baru
#     data[pilihan]["judul"] = judul_baru
#     data[pilihan]["id_buku"] = id_buku_baru
#     print("\nBerhasil mengubah data peminjaman...")

# def remove_buku():
#     if not data:
#         print("Tidak ada data untuk dihapus.")
#         return

#     print("\n===== DATA PEMINJAMAN =====")
#     for i, peminjaman in enumerate(data, start=1):
#         print(f"{i}. Nama: {peminjaman['nama']}, Judul Buku: {peminjaman['judul']}, Tanggal Pinjam: {peminjaman['tanggal']}")

#     pilihan = input("Pilih nomor yang ingin dihapus: ")
#     if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data):
#         print("Nomor tidak valid.")
#         return

#     pilihan = int(pilihan) - 1
#     del data[pilihan]
#     print("Berhasil menghapus data peminjaman...")

# while True:
#     print("\n===== SELAMAT DATANG DI PERPUSTAKAAN =====")
#     print("1. Pilih Buku")
#     print("2. Edit Peminjaman")
#     print("3. Hapus Peminjaman")
#     print("4. Lihat Daftar Peminjam")
#     print("5. Keluar")

#     pilih = input("Silahkan pilih: ")

#     if pilih == "1":
#         daftar_buku()
#         peminjaman = pilih_buku()
#         print(f"\nBerhasil meminjam...\nID Buku: {peminjaman['id_buku']}\nJudul: {peminjaman['judul']}\nPeminjam: {peminjaman['nama']}\nTanggal Pinjam: {peminjaman['tanggal']}")
#     elif pilih == "2":
#         edit_buku()
#     elif pilih == "3":
#         remove_buku()
#     elif pilih == "4":
#         tampilkan_peminjam()
#     elif pilih == "5":
#         print("Terimakasih sudah berkunjung ke perpustakaan! Jangan lupa kembali lagi!")
#         break
#     else:
#         print("Invalid! Masukkan pilihan yang valid.")

# # Soal no 3
# data_barang = []
# def pendataan_barang():
#     while True:
#         print("===== SELAMAT DATANG DI PENGIRIMAN EXPRESSS =====")
#         barang = input("Masukkan nama barang : ")
#         id_barang = int(input("Buat ID barang : "))
#         while True:
#             print("STATUS PRORITAS BARANG\n 1. Darurat\n 2. Biasa\n 3. Non-Darurat")
#             status = int(input("Masukkan status : "))
            
#             if status == 1 :
#                 status = "Darurat"
#                 data_barang.insert(0, {"Nama Barang": barang , "ID Barang": id_barang, "Prioritas": status})
#                 break
#             elif status == 2 :
#                 status = "Biasa"
#                 index_awal = 0
#                 i = 0
#                 for darurat in data_barang:
#                     if darurat["Prioritas"] == "Darurat":
#                         index_awal = i + 1
#                     i += 1
#                 data_barang.insert(index_awal, {"Nama Barang": barang , "ID Barang": id_barang, "Prioritas": status})
#                 break
#             elif status == 3 :
#                 status = "Non-Darurat"
#                 data_barang.append({"Nama Barang": barang , "ID Barang": id_barang, "Prioritas": status})
#                 break
#             else:
#                 print("Invalid")
#         print("\n ===== DATA BARANG SAAT INI =====")
#         for data in data_barang:
#             print(f"\n Nama Barang: {data["Nama Barang"]}\n ID Barang: {data["ID Barang"]}\n Status: {data["Prioritas"]}")

#         lanjut = input("Apakah ingin menginput barang? (ya/tidak): ").lower()
#         if lanjut != "ya" :
#             break

# pendataan_barang()