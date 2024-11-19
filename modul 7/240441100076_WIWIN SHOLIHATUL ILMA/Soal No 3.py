kelas = {}

while True:
    print("Menu:")
    print("1. Tambah Siswa")
    print("2. Lihat Siswa per Kelas")
    print("3. Update Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == '1':
        nama = input("Masukkan nama siswa: ")
        asal_sekolah = input("Masukkan asal sekolah siswa: ")
        
        kelas_baru = len(kelas) + 1
        if kelas_baru not in kelas:
            kelas[kelas_baru] = []

        if len(kelas[kelas_baru]) < 3:
            kelas[kelas_baru].append({'nama': nama, 'asal_sekolah': asal_sekolah})
        else:
            kelas_baru += 1
            kelas[kelas_baru] = [{'nama': nama, 'asal_sekolah': asal_sekolah}]
        
        print(f"Siswa {nama} dari {asal_sekolah} berhasil ditambahkan ke kelas {kelas_baru}.")

    elif pilihan == '2':
        kelas_ke = int(input("Masukkan nomor kelas yang ingin dilihat: "))
        if kelas_ke in kelas:
            print(f"Siswa di kelas {kelas_ke}:")
            for siswa in kelas[kelas_ke]:
                print(f"Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")
        else:
            print(f"Kelas {kelas_ke} tidak ditemukan.")

    elif pilihan == '3':
        nama_lama = input("Masukkan nama siswa yang ingin diubah: ")
        nama_baru = input("Masukkan nama baru: ")
        asal_sekolah_baru = input("Masukkan asal sekolah baru: ")
        
        ditemukan = False
        for kelas_ke, siswa_list in kelas.items():
            for siswa in siswa_list:
                if siswa['nama'] == nama_lama:
                    siswa['nama'] = nama_baru
                    siswa['asal_sekolah'] = asal_sekolah_baru
                    ditemukan = True
                    print(f"Data siswa {nama_lama} berhasil diperbarui.")
                    break
            if ditemukan:
                break
        if not ditemukan:
            print(f"Siswa dengan nama {nama_lama} tidak ditemukan.")

    elif pilihan == '4':
        nama = input("Masukkan nama siswa yang ingin dihapus: ")
        
        ditemukan = False
        for kelas_ke, siswa_list in kelas.items():
            for siswa in siswa_list:
                if siswa['nama'] == nama:
                    siswa_list.remove(siswa)
                    print(f"Siswa {nama} berhasil dihapus")
                    ditemukan = True
                    break
            if ditemukan:
                break
        if not ditemukan:
            print(f"Siswa dengan nama {nama} tidak ditemukan")

    elif pilihan == '5':
        print("Keluar")
        break
    
    else:
        print("Pilihan tidak valid, silahkan coba lagi")