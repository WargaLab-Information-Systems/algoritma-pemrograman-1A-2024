data_siswa = []

def tampilkan_siswa():
    for siswa in data_siswa:
        print(f"Nama: {siswa['nama']}, Kelas: {siswa['kelas']}")

def tambah_siswa():
    nama = input("Nama siswa: ")
    kelas = int(input("Kelas: "))
    siswa = {'nama': nama, 'kelas': kelas}
    data_siswa.append(siswa)
    print("Data siswa berhasil ditambahkan.")

def hapus_siswa(data_siswa):
    if not data_siswa:

        return False
    

while True:
    print("\nMenu:")
    print("1. Tampilkan siswa")
    print("2. Tambah siswa") 
    print("3. hapus siswa")
    print("4. Keluar")
    
    pilihan = input("Pilih (1-4): ")
    
    if pilihan == "1":
        tampilkan_siswa()
    elif pilihan == "2":
        tambah_siswa()
    elif pilihan == "3":
        data_siswa()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")