#Soal no 1
karyawan = []

while True:
    print("=== PROGRAM DATA KARYAWAN ===")
    print("1. Input Data")
    print("2. Tampilkan Data")
    print("3. Cari Data")
    print("4. Keluar")
    
    menu = input("Pilih menu (1-4): ")
    #Menu 1
    if menu == "1":
        print("Input Data Karyawan")
        nip = input("NIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")
        
        data = [nip, nama, alamat, departemen, jabatan]
        karyawan.append(data)
        print("Data berhasil disimpan!")
    # Menu 2
    elif menu == "2":
        if len(karyawan) == 0 :
            print("Belum ada data !")
        else:
            print("Data Karyawan:")
            print ("--------------------")
            for data in karyawan:
                print("NIP: ", data[0])
                print("Nama: ", data[1])
                print("Alamat: ", data[2])
                print("Departemen: ", data[3])
                print("Jabatan: ", data[4])
                print("--------------------")
    # Menu 3
    elif menu == "3":
        if len(karyawan) == 0:
            print("Belum ada data !")
        else:
            cari = input("Masukkan NIP atau Nama: ")
            ketemu = False
            for data in karyawan:
                if cari in data[0] or cari in data[1]:
                    print("Data ditemukan:")
                    print("NIP: ", data[0])
                    print("Nama: ", data[1])
                    print("Alamat: ", data[2])
                    print("Departemen: ", data[3])
                    print("Jabatan: ", data[4])
                    ketemu = True
            
            if ketemu == False :
                print("Data tidak ditemukan!")
    # Menu 4
    elif menu == "4":
        print("Program selesai !")
        break
    
    else:
        print("Menu tidak valid !")

#Soal No 2
peminjaman = []

while True:
    print("=== PROGRAM PEMINJAMAN BUKU ===")
    print("1. Input Peminjaman")
    print("2. Tampilkan Peminjaman") 
    print("3. Cari Peminjaman")
    print("4. Update Peminjaman")
    print("5. Hapus Peminjaman")
    print("6. Keluar")
    
    menu = input("Pilih menu (1-6): ")
    
    # Menu 1
    if menu == "1":
        print("Input Data Peminjaman")
        id_peminjaman = input("ID Peminjaman: ")
        nama_peminjam = input("Nama Peminjam: ")
        judul_buku = input("Judul Buku: ")
        tanggal_peminjaman = input("Tanggal Peminjaman (DD-MM-YYYY): ")
        
        data = [id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman]
        peminjaman.append(data)
        print("Data berhasil disimpan!")
        
    # Menu 2
    elif menu == "2":
        if len(peminjaman) == 0:
            print("Belum ada data!")
        else:
            print("Data Peminjaman Buku:")
            print("--------------------")
            for data in peminjaman:
                print("ID Peminjaman:", data[0])
                print("Nama Peminjam:", data[1])
                print("Judul Buku:", data[2])
                print("Tanggal Peminjaman:", data[3])
                print("--------------------")
                
    # Menu 3
    elif menu == "3":
        if len(peminjaman) == 0:
            print("Belum ada data !")
        else:
            cari = input("Masukkan ID Peminjaman atau Nama Peminjam: ")
            ketemu = False
            for data in peminjaman:
                if cari in data[0] or cari in data[1]:
                    print("Data ditemukan:")
                    print("---------------------")
                    print("ID Peminjaman:", data[0])
                    print("Nama Peminjam:", data[1])
                    print("Judul Buku:", data[2])
                    print("Tanggal Peminjaman:", data[3])
                    print("---------------------")
                    ketemu = True
                    
            if ketemu == False:
                print("Data tidak ditemukan!")
                
    # Menu 4
    elif menu == "4":
        if len(peminjaman) == 0:
            print("Belum ada data!")
        else:
            id_update = input("Masukkan ID Peminjaman yang ingin diupdate: ")
            temp_peminjaman = []
            ketemu = False
            for data in peminjaman:
                if data[0] == id_update:
                    print("Masukkan data baru:")
                    nama_peminjam = input("Nama Peminjam: ")
                    judul_buku = input("Judul Buku: ")
                    tanggal_peminjaman = input("Tanggal Peminjaman (DD-MM-YYYY): ")
                    
                    temp_peminjaman.append([id_update, nama_peminjam, judul_buku, tanggal_peminjaman])
                    ketemu = True
                else:
                    temp_peminjaman.append(data)
                    
            if ketemu:
                peminjaman = temp_peminjaman
                print("Data berhasil diupdate!")
            else:
                print("Data tidak ditemukan!")
                
    # Menu 5     
    elif menu == "5":
        if len(peminjaman) == 0:
            print("Belum ada data!")
        else:
            id_hapus = input("Masukkan ID Peminjaman yang ingin dihapus: ")
            temp_peminjaman = []
            ketemu = False
            for data in peminjaman:
                if data[0] == id_hapus:
                    ketemu = True
                    continue  
                temp_peminjaman.append(data)
                    
            if ketemu == True :
                peminjaman = temp_peminjaman 
                print("Data berhasil dihapus!")
            else:
                print("Data tidak ditemukan!")
    # Menu 6
    elif menu == "6":
        print("Program selesai!")
        break
        
    else:
        print("Menu tidak valid !")

#Soal No 3
barang_list = []

def tambah_barang(barang_list):
    nama = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    
    while True :
        print("=== Pilih Prioritas Berikut ===")
        print("1. Darurat")
        print("2. Biasa")
        print("3. Non-Darurat")
        prioritas = input("Pilih Tingkat Prioritas (1-3): ")
        
        if prioritas == "1":
            barang_list = [ (id_barang, nama, "Darurat") ] + barang_list
            break
        elif prioritas == "2":
            if len(barang_list) == 0 :
                barang_list = [ (id_barang, nama, "Biasa") ]
            else:
                tengah = len(barang_list) // 2
                barang_list = barang_list[:tengah] + [ (id_barang, nama, "Biasa") ] + barang_list[tengah:]
            break
        elif prioritas == "3":
            barang_list.append((id_barang, nama, "Non-Darurat"))
            break
        else:
            print("Prioritas tidak valid, silakan pilih lagi.")
    
    return barang_list

def tampilkan_barang(barang_list):
    print("Daftar Barang:")
    print("--------------------")
    for id_barang, nama, prioritas in barang_list:
        print("ID:", id_barang)
        print("Nama:", nama)
        print( "Prioritas:", prioritas)
        print("--------------------")

while True:
    barang_list = tambah_barang(barang_list)
    tampilkan_barang(barang_list)
    
    lagi = input("Apakah Anda ingin menambahkan barang lagi? (ya/tidak): ")
    if lagi != "ya":
        break

print("Program selesai.")