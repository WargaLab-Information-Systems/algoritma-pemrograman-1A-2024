#struktur Data
siswa = {}

#create
def tambah_siswa(nama, kelas, sekolah):
    if kelas not in siswa:
        siswa[kelas] = []
        
    if len(siswa[kelas]) < 3:
        siswa[kelas].append({'nama': nama, 'sekolah': sekolah})
        print(f"siswa {nama} berhasil ditambahkan ke kelas {kelas}.")
    else:
        print(f"kelas {kelas} sudah penuh")

#read
def tampilkan_siswa():
    if not siswa:
        print("tidak ada siswa")
        return
    
    for kelas, daftar_siswa in siswa.items():
        print(f"daftar siswa di kelas {kelas}:")
        for s in daftar_siswa:
            print(f"- {s['nama']}, sekolah: {s['sekolah']}")

#update
def update_siswa(nama_lama, nama_baru, kelas_baru, sekolah_baru):
    for kelas, daftar_siswa in siswa.items():
        for s in list(daftar_siswa):
            if s['nama'] == nama_lama:
                daftar_siswa.remove(s)
                tambah_siswa(nama_baru, kelas_baru, sekolah_baru)
                print(f"siswa {nama_lama} berhasil diupdate")
                return
    print(f"siswa {nama_lama} tidak ditemukan")

#delete
def delete_siswa(nama):
    for kelas, daftar_siswa in siswa.items():
        for s in list(daftar_siswa):
            if s['nama'] == nama:
                daftar_siswa.remove(s)
                print(f"siswa {nama} berhasil dihapus")
                return
    print(f"siswa {nama} tidak ditemukan")

#menu untuk tampilan
def menu():
    while True:
        print("1. tambah siswa")
        print("2. tampilkan semua siswa")
        print("3. update siswa")
        print("4. delete siswa")
        pilihan = input("pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            nama = input("masukkan nama siswa: ")
            kelas = input("masukkan nama kelas: ")
            sekolah = input("masukkan asal sekolah: ")
            tambah_siswa(nama, kelas, sekolah)
        elif pilihan == '2':
            tampilkan_siswa()
        elif pilihan == '3':
            nama_lama = input("masukkan nama siswa yang ingin diupdate: ")
            nama_baru = input("masukkan nama baru: ")
            kelas_baru = input("masukkan kelas baru: ")
            sekolah_baru = input("masukkan asal sekolah baru: ")
            update_siswa(nama_lama, nama_baru, kelas_baru, sekolah_baru)
        elif pilihan == '4':
            nama = input("masukkan nama siswa yang ingin dihapus: ")
            delete_siswa(nama)
        else:
            print("kode tidak ada")

        ulang = input("apakah ingin mengulang kembali? (ya/no): ")
        if ulang != 'ya':
            print("terimakasi")
            break
menu()