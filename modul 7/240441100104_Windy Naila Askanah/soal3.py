data = {}

def menghitungkelas():
    jmlsiswa = 0  
    for siswa in data.items():
        jmlsiswa += len(siswa)

    return (jmlsiswa // 3) + 1

def create():
    nama = input("Masukkan nama: ")
    sekolah = input("Masukkan asal sekolah: ")
    plotting = input("Masukkan plotting: ")

    kelas = menghitungkelas()
    kelaske = data.get(f"Kelas {kelas}", [])

    if len(kelaske) >= 3:
        kelas += 1
        kelaske = []

    if f"Kelas {kelas}" not in data:
        data[f"Kelas {kelas}"] = []

    data[f"Kelas {kelas}"].append({
        "nama": nama,
        "sekolah": sekolah,
        "plotting": plotting
    })
    print(f"{nama} masuk Kelas ke-{kelas}.")

def read():
    if not data:
        print("Belum ada data siswa")
    else:
        print("\nData Siswa:")
        for kelas, siswa in data.items():
            print(f"{kelas}:")
            for siswakelas in siswa:
                print(f"  - Nama: {siswakelas['nama']}, Asal Sekolah: {siswakelas['sekolah']}, Plotting: {siswakelas['plotting']}")

def update():
    nama = input("Masukkan nama siswa yang ingin diperbarui: ")
    found = False
    for kelas, siswa in data.items():
        for siswakelas in siswa:
            if siswakelas["nama"] == nama:
                print(f"Siswa ditemukan di {kelas}.")
                siswakelas["sekolah"] = input("Masukkan asal sekolah baru: ")
                siswakelas["plotting"] = input("Masukkan plotting baru: ")
                print(f"Data siswa {nama} berhasil diperbarui.")
                found = True
                break
        if found:
            break
    if not found:
        print(f"{nama} tidak ditemukan.")


def delete():
    nama = input("Masukkan nama siswa ingin dihapus: ")
    found = False
    for kelas, siswa in data.items():
        for siswakelas in siswa:
            if siswakelas["nama"] == nama:
                print(f"Siswa ditemukan di {kelas}.")
                siswa.remove(siswakelas)
                print(f"{nama} berhasil dihapus.")
                if not siswa:
                    del data[kelas]
                found = True
                break
        if found:
            break
    if not found:
        print(f"{nama} tidak ditemukan.")

while True:
    print("\nSelamat datang di lembaga bimbingan intensif Gema Ripah")
    print("1. tambah data siswa")
    print("2. Lihat data siswa")
    print("3. Perbarui data siswa")
    print("4. Hapus data siswa")
    print("5. Keluar")
    pilihan = input("Masukkan menu pilihan Anda: ")
    if pilihan == "1":
         create()
    elif pilihan == "2":
        read()
    elif pilihan == "3":
           update()
    elif pilihan == "4":
        delete()
    elif pilihan == "5":
        print("Terimakasih")
        break
    else:
        print("Input salah!")