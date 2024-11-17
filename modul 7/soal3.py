data_siswa = {}
def tambah():
    nama = input("masukkan nama: ")
    asal_sekolah = input("masukkan asal sekolah: ")
    kelas = int(input("masukkan kelas bimbingan: "))
    kelas_terakhir = len(data_siswa)
    if kelas_terakhir == 0 or len(data_siswa[f"Kelas {kelas_terakhir}"]) == 3:
        kelas_terakhir += 1
        data_siswa[f"kelas {kelas_terakhir}"] = []
    data_siswa[f"kelas {kelas_terakhir}"].append({
        "nama": nama,
        "asal sekolah": asal_sekolah,
        "kelas bimbingan": kelas
    })
    print(f"{nama} berhasil di tambahkan ke daftar kelas bimbingan {kelas_terakhir}")
def tampil():
    if data_siswa == {}:
        print("data peminjam kosong.")
    else:
        for kelas, siswa in data_siswa.items():
            print(f"{kelas}:")
            nomor = 1   
            for data in siswa: 
                print(f"    {nomor}. nama: {data['nama']}, asal sekolah: {data['asal sekolah']}, kelas: {data['kelas bimbingan']}")
                nomor += 1  
def edit():
    nama_lama = input("masukkan nama siswa yang akan diubah: ")
    for siswa in data_siswa.values():
        for data in siswa:
            if data["nama"] == nama_lama:
                nama_baru = input("masukkan nama baru: ")
                asal_sekolah_baru = input("masukkan asal sekolah baru: ")
                kelas_baru = int(input("masukkan kleas bimbingan baru: "))
                data["nama"] = nama_baru
                data["asal Sekolah"] = asal_sekolah_baru
                data["kelas bimbingan"] = kelas_baru
                print("data berhasil diubah!")
                return
    print("data tidak ditemukan!")
def hapus():
    nama = input("masukkan nama siswa yang akan dihapus: ")
    for kelas, siswa in data_siswa.items():
        for data in siswa: 
            if data["nama"] == nama:
                siswa.remove(data)
                print("data berhasil dihapus!")
                return
    print("data tidak ditemukan!")
while True:
    print("1. tambah siswa")
    print("2. tampilkan data")
    print("3. ubah data")
    print("4. hapus data")
    pilihan = input("pilih menu: ")
    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampil()
    elif pilihan == "3":
        edit()
    elif pilihan == "4":
        hapus()
    else:
        print("Pilihan tidak ada")
