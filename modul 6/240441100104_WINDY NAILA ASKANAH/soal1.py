data_karyawan = []


def masukkankaryawan():
    nip = input("Masukkan Nip: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")
    
    karyawan = [nip, nama, alamat, departemen, jabatan]
    data_karyawan.append(karyawan)
    print("Data karyawan berhasil ditambahkan!")

def carikaryawan():
    print("Pilih atribut untuk pencarian:")
    print("1. Nip")
    print("2. Nama")
    print("3. Alamat")
    print("4. Departemen")
    print("5. Jabatan")
    pilihan = input("Masukkan nomor pilihan pencarian: ")
    
    if pilihan == '1':
        indeks = 0
    elif pilihan == '2':
        indeks = 1
    elif pilihan == '3':
        indeks = 2
    elif pilihan == '4':
        indeks = 3
    elif pilihan == '5':
        indeks = 4
    else:
        print("Pilihan tidak valid!")
        return

    nilai = input("Masukkan kata atau angka yang dicari: ")
    hasil = [k for k in data_karyawan if k[indeks].lower() == nilai.lower()]
    
    if hasil:
        for karyawan in hasil:
            print(f"\nNIP     : {karyawan[0]}")
            print(f"Nama      : {karyawan[1]}")
            print(f"Alamat    : {karyawan[2]}")
            print(f"Departemen: {karyawan[3]}")
            print(f"Jabatan   : {karyawan[4]}")
    else:
        print("\nTidak ada data karyawan yang sesuai dengan pencarian.\n")

def tampilkan_semua_karyawan():
    print("\nData Semua Karyawan:")
    for i, karyawan in enumerate(data_karyawan, start=1):
        print(f"\nData Karyawan ke-{i}:")
        print(f"NIP       : {karyawan[0]}")
        print(f"Nama      : {karyawan[1]}")
        print(f"Alamat    : {karyawan[2]}")
        print(f"Departemen: {karyawan[3]}")
        print(f"Jabatan   : {karyawan[4]}")

def main():
    print("=== Input dan Pencarian Data Karyawan ===")
    
    for i in range(5):
        print(f"\nMasukkan data karyawan ke-{i+1}:")
        masukkankaryawan()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Data Karyawan")
        print("2. Cari Data Karyawan")
        print("3. Tampilkan Semua Data Karyawan")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan menu: ")
        
        if pilihan == '1':
            masukkankaryawan()
        elif pilihan == '2':
            carikaryawan()
        elif pilihan == '3':
            tampilkan_semua_karyawan()
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()