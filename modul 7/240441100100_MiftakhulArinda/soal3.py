data_siswa = {}

def menu():
    while True:
        print("\nMenu Sistem Lembaga Bimbingan Intensif Gema Ripah")
        print("1. Tambah Siswa")
        print("2. Menampilkan Data Siswa")
        print("3. Update Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Keluar")
        sub_menu = input("Pilih menu (1-5): ")

        if sub_menu == "1":
            print("\n1. Tambah Siswa")
            nama = input("Masukkan nama siswa: ")
            asal_sekolah = input("Masukkan asal sekolah: ")
            jumlah_siswa = sum(len(kelas) for kelas in data_siswa.values())
            kelas = (jumlah_siswa // 3) + 1

            absensi_siswa = {
                "nama": nama,
                "asal_sekolah": asal_sekolah
            }
            if f"Kelas {kelas}" not in data_siswa:
                data_siswa[f"Kelas {kelas}"] = []

            data_siswa[f"Kelas {kelas}"].append(absensi_siswa)
            print(f"{nama} dari {asal_sekolah} berhasil ditambahkan ke Kelas {kelas}.")

        elif sub_menu == "2":
            print("\n2. Menampilkan Data Siswa")
            if data_siswa:
                for kelas, daftar_siswa in data_siswa.items():
                    print(f"\n{kelas}:")
                    for siswa in daftar_siswa:
                        print(f"{siswa['nama']} ({siswa['asal_sekolah']})")
            else:
                print("Tidak ada data yang ditemukan.")

        elif sub_menu == "3":
            print("\n3. Update Data Siswa")
            nama = input("Masukkan nama siswa yang ingin diupdate: ")
            for kelas, daftar_siswa in data_siswa.items():
                for siswa in daftar_siswa:
                    if siswa["nama"] == nama:
                        nama_update = input("Masukkan nama baru siswa: ")
                        asal_sekolah_update = input("Masukkan asal sekolah baru: ")
                        siswa["nama"] = nama_update
                        siswa["asal_sekolah"] = asal_sekolah_update
                        print(f"Data siswa berhasil diperbarui menjadi {nama_update} dari {asal_sekolah_update}.")
                        break
            else:
                print("Data siswa tidak ditemukan.")

        elif sub_menu == "4":
            print("\n4. Hapus Data Siswa")
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            for kelas, daftar_siswa in data_siswa.items():
                for siswa in daftar_siswa:
                    if siswa["nama"] == nama:
                        daftar_siswa.remove(siswa)
                        print(f"Data siswa {nama} berhasil dihapus.")
                        break
            else:
                print("Data siswa tidak ditemukan.")

        elif sub_menu == "5":
            print("Terima kasih telah menggunakan sistem.")
            break

        else:
            print("Pilihan tidak valid.")
menu()
