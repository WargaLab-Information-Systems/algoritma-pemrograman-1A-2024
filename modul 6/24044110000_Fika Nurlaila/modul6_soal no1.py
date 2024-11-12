# 1. membuat list data karyawan
# List untuk menyimpan data karyawan
kode = []
list_nip = []
list_nama = []
list_alamat = []
list_departemen = []
list_jabatan = []

# Fungsi untuk menambahkan data karyawan
def tambah_karyawan():
    n = int(input("Berapa karyawan yang ingin anda data (Minimal 5)? "))
    while n < 5:
        n = int(input("Jumlah karyawan minimal 5. Masukkan lagi jumlah karyawan: "))
    
    # Input data karyawan
    for i in range(n):
        nip = input("\nMasukkan No NIP: ")
        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat (Kabupaten): ")
        departemen = input("Masukkan Departemen: ")
        jabatan = input("Masukkan Jabatan: ")
        
        simpan_data = input("Apakah kamu ingin menyimpan data ini? (y/t): ")
        if simpan_data.lower() == "t":
            print("Data tidak tersimpan.")
        elif simpan_data.lower() == "y":
            # Menambahkan data ke dalam list
            list_nip.append(nip)
            list_nama.append(nama)
            list_alamat.append(alamat)
            list_departemen.append(departemen)
            list_jabatan.append(jabatan)
            kode.append(i+100)
            print(f"Data karyawan berhasil disimpan dengan kode data: {i+100}")

# Fungsi untuk mencari data karyawan berdasarkan atribut
def cari_karyawan(atribut, nilai):
    hasil = []
    # Menentukan list yang sesuai dengan atribut
    if atribut == "nip":
        list = list_nip
    elif atribut == "nama":
        list = list_nama
    elif atribut == "alamat":
        list = list_alamat
    elif atribut == "departemen":
        list = list_departemen
    elif atribut == "jabatan":
        list = list_jabatan
    elif atribut == "kode":
        list = kode
    else:
        return hasil  # jika atribut tidak dikenal, return hasil kosong
    # Melakukan pencarian berdasarkan nilai
    for i in range(len(list)):
        if nilai.lower() in list[i].lower():  # mencari berdasarkan indeks dan karakter yang cocok dengan data karyawan
            hasil.append(i)
    return hasil

# Fungsi untuk menampilkan data karyawan
def tampilkan_karyawan():
    if len(kode) == 0:
        print("Data karyawan belum tersedia.")
    else:
        for i in range(len(kode)):
            print(f"\nKaryawan {i+1}")
            print(f"Kode : {kode[i]}   NIP : {list_nip[i]}  Nama : {list_nama[i]}   Alamat : {list_alamat[i]}   Departemen : {list_departemen[i]}   Jabatan : {list_jabatan[i]}")
# Menu utama program
while True:
    print("\nPENCARIAN DATA KARYAWAN")
    print("1. Tambah Data Karyawan")
    print("2. Cari berdasarkan NIP")
    print("3. Cari berdasarkan Nama")
    print("4. Cari berdasarkan Alamat")
    print("5. Cari berdasarkan Departemen")
    print("6. Cari berdasarkan Jabatan")
    print("7. Cari berdasarkan kode")
    print("8. Tampilkan semua data karyawan")
    print("9. Keluar")
        
    pilihan = input("Pilih menu (1-9): ")
    if pilihan == "1":
        tambah_karyawan()
        
    elif pilihan == "2":
        nip = input("Masukkan NIP yang dicari: ")
        hasil = cari_karyawan("nip", nip)
        if hasil:
            print("Data yang ditemukan:")
            for no in hasil:
                print(f"Karyawan {no+1} NIP {list_nip[no]}, Nama {list_nama[no]}, Alamat {list_alamat[no]}, Departemen {list_departemen[no]}, Jabatan {list_jabatan[no]}, Kode {kode[no]}")
        else:
            print("Data NIP tidak ditemukan.")
     
    elif pilihan == "3":
        nama = input("Masukkan Nama yang dicari: ")
        hasil = cari_karyawan("nama", nama)
        if hasil:
            print("Data yang ditemukan:")
            for no in hasil:
                print(f"Karyawan {no+1} NIP {list_nip[no]}, Nama {list_nama[no]}, Alamat {list_alamat[no]}, Departemen {list_departemen[no]}, Jabatan {list_jabatan[no]}, Kode {kode[no]}")
        else:
            print("Data Nama tidak ditemukan.")
        
    elif pilihan == "4":
        alamat = input("Masukkan Alamat yang dicari: ")
        hasil = cari_karyawan("alamat", alamat)
        if hasil:
            print("Data yang ditemukan:")
            for no in hasil:
                print(f"Karyawan {no+1} NIP {list_nip[no]}, Nama {list_nama[no]}, Alamat {list_alamat[no]}, Departemen {list_departemen[no]}, Jabatan {list_jabatan[no]}, Kode {kode[no]}")
        else:
            print("Data Alamat tidak ditemukan.")
        
    elif pilihan == "5":
        departemen = input("Masukkan Departemen yang dicari: ")
        hasil = cari_karyawan("departemen", departemen)
        if hasil:
            print("Data yang ditemukan:")
            for no in hasil:
                print(f"Karyawan {no+1} NIP {list_nip[no]}, Nama {list_nama[no]}, Alamat {list_alamat[no]}, Departemen {list_departemen[no]}, Jabatan {list_jabatan[no]}, Kode {kode[no]}")
        else:
            print("Data Departemen tidak ditemukan.")
        
    elif pilihan == "6":
        jabatan = input("Masukkan Jabatan yang dicari: ")
        hasil = cari_karyawan("jabatan", jabatan)
        if hasil:
            print("Data yang ditemukan:")
            for no in hasil:
                 print(f"Karyawan {no+1} NIP {list_nip[no]}, Nama {list_nama[no]}, Alamat {list_alamat[no]}, Departemen {list_departemen[no]}, Jabatan {list_jabatan[no]}, Kode {kode[no]}")
        else:
            print("Data Jabatan tidak ditemukan.")

    elif pilihan == "7":
        kode = input("Masukkan Kode yang dicari: ")
        hasil = cari_karyawan("kode", kode)
        if hasil:
            print("Data yang ditemukan:")
            for no in hasil:
                 print(f"Karyawan {no+1} NIP {list_nip[no]}, Nama {list_nama[no]}, Alamat {list_alamat[no]}, Departemen {list_departemen[no]}, Jabatan {list_jabatan[no]}, Kode {kode[no]}")
        else:
            print("Data Kode tidak ditemukan.")
        
    elif pilihan == "8":
        print("\n============================")
        print("        DATA KARYAWAN       ")
        tampilkan_karyawan()
        print("============================")
        
    elif pilihan == "9":
        print("Keluar dari program.")
        break
        
    else:
        print("Pilihan tidak valid, coba lagi.")
