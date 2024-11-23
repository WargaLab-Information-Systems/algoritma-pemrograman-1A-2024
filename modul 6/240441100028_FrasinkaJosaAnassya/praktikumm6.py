# #soal no 1
# data_karyawan= []
# for i in range (2):
#         print(f"masukkan data karyawan ke-{i +1}:")
#         nip = input("NIP karyawan: ")
#         nama = input("Nama karyawan: ")
#         alamat = input("Alamat karyawan: ")
#         departemen = input("Departemen karyawan: ")
#         jabatan = input("Jabatan karyawan: ")

#         karyawan = (nip, nama, alamat, departemen, jabatan)
#         data_karyawan.append(karyawan)
#         print()
# while True:
#     print("Mencari Karyawan")
#     print("1. Cari berdasarkan NIP")
#     print("2. Cari berdasarkan Nama")
#     print("3. Cari berdasarkan Alamat")
#     print("4. Cari berdasarkan Departemen")
#     print("5. Cari berdasarkan Jabatan")
#     print("6. Keluar")
    # pilihan = input("Pilih opsi karyawan (1-6): ")
    # if pilihan == "6":
    #     break
    # if pilihan == "1":
    #     atribut = 0
    # elif pilihan == "2":
    #     atribut = 1
    # elif pilihan == "3":
    #     atribut = 2
    # elif pilihan == "4":
    #     atribut = 3  
    # elif pilihan == "5":
    #     atribut = 4  
    # else:
    #     print("Pilihan anda tidak valid. Silakan coba lagi.")
    
    # hasil = input("Masukkan hasil pencarian: ")
    # hasil_pencarian = [ ]

    # for karyawan in data_karyawan:
    #     if karyawan[atribut] == hasil:
    #         hasil_pencarian.append(karyawan)

    # if hasil_pencarian:
    #     print("Hasil pencarian karyawan: ")
    #     for k in hasil_pencarian:
    #         print(f"NIP: {k[0]}, Nama: {k[1]}, Alamat: {k[2]}, Departemen: {k[3]}, Jabatan: {k[4]}")
    # else:
    #     print("Tidak ada karyawan yang ditemukan.")
    # break

# #soal no 2
# daftarpinjam = []

# def creatpeminjaman():
#     print("-- Tambah Peminjaman Buku --")
#     id_pinjam = input("Masukkan ID Peminjaman: ")
#     nama = input("Masukkan Nama Peminjam: ")
#     judul = input("Masukkan Judul Buku: ")
#     tanggal = input("Masukkan Tanggal Peminjaman: ")
    
#     peminjaman = (id_pinjam, nama, judul, tanggal)
#     daftarpinjam.append(peminjaman)
#     print("Peminjaman buku berhasil ditambahkan ke list!")
#     print()

# def tampilkan_peminjaman():
#     print("-- Daftar Peminjaman Buku --")
#     if not daftarpinjam:
#         print("Belum ada data peminjaman.")
#         return
#     for pinjam in daftarpinjam :
#         print(f"ID Peminjaman: {pinjam[0]}")
#         print(f"nama Peminjam: {pinjam[1]}")
#         print(f"nudul Buku: {pinjam[2]}")
#         print(f"tanggal Peminjaman: {pinjam[3]}")
#         print()
  
# def updatepeminjaman():
#     print("-- Update Data Peminjaman --")
#     if not daftarpinjam:
#         print("Belum ada data peminjaman")
#         return
    
#     id_pinjam = input("Masukkan ID Peminjaman yang akan diupdate: ")
#     indeks = -1
#     for i in range(len(daftarpinjam)):
#         if daftarpinjam[i][0] == id_pinjam:
#             indeks = i
#             break
#     if indeks == -1:
#         print("ID Peminjaman tidak ditemukan!")
#         return   
#     #data baru
#     print("masukkan data baru:")
#     nama = input("masukkan Nama Peminjam: ")
#     judul = input("asukkan judul Buku: ")
#     tanggal = input("asukkan tanggal peminjaman: ")
    
#     peminjaman_baru = (id_pinjam, nama, judul, tanggal)
#     daftarpinjam[indeks] = peminjaman_baru
#     print("Data peminjaman berhasil diupdate!")
    

# def hapus_peminjaman(daftarpinjam):
#     print("-- HAPUS DATA PINJAM --")
#     if not daftarpinjam:
#         print("belum ada data peminjaman")
#         return
    
#     id_pinjam = input("masukkan ID Peminjaman yang akan dihapus: ")

#     while True :
#         for i in range(len(daftarpinjam)):
#             if daftarpinjam[i][0] == id_pinjam:
#                 del daftarpinjam[i]
#                 print("data peminjaman berhasil dihapus!")
#                 return
# def menu():
#     print("-- MENU --")
#     print("a. Tambah Peminjaman")
#     print("b. Lihat Daftar Peminjaman") 
#     print("c. Update Peminjaman")
#     print("d. Hapus Peminjaman")
#     print("e. Keluar")
    
#     pilihan = input("Masukkan pilihan (a/b/c/d/e): ").lower()
#     return pilihan

# while True:
#     pilihan = menu()
    
#     if pilihan == "a":
#         creatpeminjaman()
#     elif pilihan == "b":
#         tampilkan_peminjaman()
#     elif pilihan == "c":
#         updatepeminjaman()
#     elif pilihan == "d":
#         hapus_peminjaman(daftarpinjam)
#     elif pilihan == "e":
#         print("terima kasih !")
#         break
#     else:
#         print("tidak valid!")


# #soal no 3
# daftar = []
# def tambah_barang():
#     nama_barang = input("Nama Barang: ")
#     id_barang = input("ID Barang: ")
#     prioritas = input("tingkat Prioritas (darurat/biasa/non-darurat): ")

#     while prioritas not in ['darurat', 'biasa', 'non-darurat']:
#         print("tidak valid")
#         prioritas = input("Tingkat Prioritas (darurat/biasa/non-darurat): ")
#     barang = (id_barang, nama_barang, prioritas)
#     daftar.append(barang)
#     print("Barang berhasil ditambahkan!")

# def tampilbarang():
#     if not (daftar):
#         print("Belum ada barang yang ditambahkan.")
#     else:
#         print("daftar Barang yang Dikirim:")
#         for barang in daftar:
#             if barang[2] == 'darurat':
#                 print(f"ID : {barang[0]}, Nama Barang: {barang[1]}, Darurat")
#         for barang in daftar:
#             if barang[2] == 'biasa':
#                 print(f"ID: {barang[0]}, Nama Barang: {barang[1]}, Biasa")
#         for barang in daftar:
#             if barang[2] == 'non darurat':
#                 print(f"ID: {barang[0]}, Nama Barang: {barang[1]}, Non-Darurat")

# def tanya():
#     while True:
#         tambah_barang()
#         tampilbarang()
#         lagi = input("apakah Anda ingin menambahkan barang lain? (ya/tidak): ")
#         if lagi != "ya":
#             print("maaciw cmiwwww")
#             break
# tanya()