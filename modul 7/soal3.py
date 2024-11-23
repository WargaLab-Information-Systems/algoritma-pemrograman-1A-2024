siswa = []  # L Menyimpan data siswa (nama, asal sekolah, kelas)
kelas = {}  # D Menyimpan kelas dan siswa yang ada di kelas tersebut

def tambah_siswa(nama, asal_sekolah):
    # Menentukan kelas berdasarkan jumlah siswa
    kelas_id = (len(siswa) // 3) + 1  # Setiap kelas maksimal 3 siswa
    siswa_baru = {"nama": nama, "asal_sekolah": asal_sekolah, "kelas": kelas_id}
    siswa.append(siswa_baru)
    print(f"Siswa {nama} dari {asal_sekolah} ditambahkan ke kelas {kelas_id}.")


def tampilkan_siswa():
    if not siswa:
        print("Belum ada siswa yang terdaftar.")
        return
    print("\nDaftar Siswa yang Terdaftar:")
    for siswa_item in siswa:
        print(f"Nama: {siswa_item['nama']}, Asal Sekolah: {siswa_item['asal_sekolah']}, Kelas: {siswa_item['kelas']}")

def update_siswa(nama, nama_baru=None, asal_sekolah_baru=None, kelas_baru=None):
    for siswa_item in siswa:
        if siswa_item["nama"].lower() == nama.lower():
            if nama_baru:
                siswa_item["nama"] = nama_baru
            if asal_sekolah_baru:
                siswa_item["asal_sekolah"] = asal_sekolah_baru
            if kelas_baru:
                # Update kelas dan pastikan kelas tersebut memiliki siswa baru
                siswa_item["kelas"] = kelas_baru
                if kelas_baru not in kelas:
                    kelas[kelas_baru] = []
                kelas[kelas_baru].append(siswa_item)
                
            print(f"Data siswa {nama} berhasil diperbarui.")
            return
    print(f"Siswa dengan nama {nama} tidak ditemukan.")

def hapus_siswa(nama):
    for siswa_item in siswa:
        if siswa_item["nama"].lower() == nama.lower():
            siswa.remove(siswa_item)
            kelas[siswa_item["kelas"]].remove(siswa_item)
            print(f"Siswa {nama} telah dihapus.")
            return
    print(f"Siswa dengan nama {nama} tidak ditemukan.")

def tampilkan_kelas():
    if not kelas:
        print("Belum ada kelas yang terdaftar.")
        return
    print("\nDaftar Kelas dan Siswa yang Terdaftar:")
    for kelas_id, siswa_list in kelas.items():
        print(f"Kelas {kelas_id}:")
        for siswa_item in siswa_list:
            print(f"  - {siswa_item['nama']} dari {siswa_item['asal_sekolah']}")

def main():
    while True:
        print("\nMenu Bimbingan:")
        print("1. Tambah Siswa")
        print("2. Tampilkan Semua Siswa")
        print("3. Update Data Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            nama = input("Masukkan Nama Siswa: ")
            asal_sekolah = input("Masukkan Asal Sekolah: ")
            tambah_siswa(nama, asal_sekolah)

        elif pilihan == "2":
            tampilkan_siswa()

        elif pilihan == "3":
            nama = input("Masukkan Nama Siswa yang ingin diupdate: ")
            nama_baru = input("Masukkan Nama Baru (kosongkan jika tidak ingin mengubah): ")
            asal_sekolah_baru = input("Masukkan Asal Sekolah Baru (kosongkan jika tidak ingin mengubah): ")
            kelas_baru = input("Masukkan Kelas Baru (kosongkan jika tidak ingin mengubah): ")
            kelas_baru = int(kelas_baru) if kelas_baru else None
            update_siswa(nama, nama_baru, asal_sekolah_baru, kelas_baru)

        elif pilihan == "4":
            nama = input("Masukkan Nama Siswa yang ingin dihapus: ")
            hapus_siswa(nama)

        elif pilihan == "5":
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-6.")
main()