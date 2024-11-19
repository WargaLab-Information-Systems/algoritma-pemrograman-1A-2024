data_siswa = {
    1: [],  
    2: [], 
    3: []   
}

def tambah_siswa(nama, kelas, asal_sekolah, plotting):
    if plotting not in data_siswa:
        print(f"Plotting {plotting} tidak valid. Pilih antara 1, 2, atau 3.")
        return

    kelas_tersedia = None
    for kelas_ in data_siswa[plotting]:
        if len(kelas_) < 3:  
            kelas_tersedia = kelas_
            break
    
    if kelas_tersedia is None:
        kelas_tersedia = []
        data_siswa[plotting].append(kelas_tersedia)

    kelas_tersedia.append({
        'nama': nama,
        'kelas': kelas,
        'asal_sekolah': asal_sekolah
    })
    print(f"Siswa {nama} berhasil ditambahkan ke plotting {plotting}, kelas {len(data_siswa[plotting])}.")

def tampilkan_data():
    if not any(data_siswa.values()):
        print("Belum ada data siswa.")
        return
    
    for plotting, kelas_list in data_siswa.items():
        print(f"\nPlotting {plotting}:")
        if not kelas_list:
            print("Belum ada siswa di plotting ini.")
            continue
        kelas_ke = 1
        for kelas in kelas_list:
            print(f"Kelas {kelas_ke}:")
            for siswa in kelas:
                print(f"- Nama: {siswa['nama']}, Kelas: {siswa['kelas']}, Asal Sekolah: {siswa['asal_sekolah']}")
            kelas_ke += 1

def update_siswa(nama_lama, nama_baru, kelas_baru, asal_sekolah_baru, plotting):
    if plotting not in data_siswa:
        print(f"Plotting {plotting} tidak valid. Pilih antara 1, 2, atau 3.")
        return
    
    for kelas in data_siswa[plotting]:
        for siswa in kelas:
            if siswa['nama'] == nama_lama:
                siswa['nama'] = nama_baru
                siswa['kelas'] = kelas_baru
                siswa['asal_sekolah'] = asal_sekolah_baru
                print(f"Data siswa {nama_lama} berhasil diperbarui.")
                return
    print(f"Siswa dengan nama {nama_lama} tidak ditemukan di plotting {plotting}.")

def hapus_siswa(nama, plotting):
    if plotting not in data_siswa:
        print(f"Plotting {plotting} tidak valid. Pilih antara 1, 2, atau 3.")
        return
    
    siswa_ditemukan = False
    for kelas in data_siswa[plotting]:
        for siswa in kelas:
            if siswa['nama'] == nama:
                kelas.remove(siswa)
                print(f"Siswa {nama} berhasil dihapus dari plotting {plotting}.")
                siswa_ditemukan = True
                break
        if siswa_ditemukan:
            break
    
    if not siswa_ditemukan:
        print(f"Siswa dengan nama {nama} tidak ditemukan di plotting {plotting}.")

def menu():
    while True:
        print("\n===Selamat datang di lembaga bimbingan intensif Gema Ripah===")
        print("Berikut adalah menu yang kami sediakan:")
        print("1. Menambahkan nama siswa yang ikut bimbingan")
        print("2. Tampilkan Data Siswa bimbingan")
        print("3. Update Siswa yang ikut bimbingan")
        print("4. Hapus Siswa dari bimbingan")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        if pilihan == '1':
            nama = input("Masukkan nama siswa: ")
            kelas = input("Masukkan kelas siswa: ")
            asal_sekolah = input("Masukkan asal sekolah: ")
            print("Pilih plotting:")
            print("1. Plotting 1")
            print("2. Plotting 2")
            print("3. Plotting 3")
            plotting = int(input("Masukkan plotting (1/2/3): "))
            tambah_siswa(nama, kelas, asal_sekolah, plotting)
        elif pilihan == '2':
            tampilkan_data()
        elif pilihan == '3':
            nama_lama = input("Masukkan nama siswa yang ingin diubah: ")
            nama_baru = input("Masukkan nama baru: ")
            kelas_baru = input("Masukkan kelas baru: ")
            asal_sekolah_baru = input("Masukkan asal sekolah baru: ")
            print("Pilih plotting:")
            print("1. Plotting 1")
            print("2. Plotting 2")
            print("3. Plotting 3")
            plotting = int(input("Masukkan plotting (1/2/3): "))
            update_siswa(nama_lama, nama_baru, kelas_baru, asal_sekolah_baru, plotting)
        elif pilihan == '4':
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            print("Pilih plotting:")
            print("1. Plotting 1")
            print("2. Plotting 2")
            print("3. Plotting 3")
            plotting = int(input("Masukkan plotting (1/2/3): "))
            hapus_siswa(nama, plotting)
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

def main():
    while True:
        jawab = input("Apa yang ingin Anda lakukan? (mencari/menambahkan/keluar): ").lower()
    
        if jawab == "mencari":
            if any(data_siswa.values()): 
                menu()
            else:
                print("Data Siswa masih kosong. Silakan tambahkan data terlebih dahulu.")
        
        elif jawab == "menambahkan":
            menu()
        
        elif jawab == "keluar":
            print("Terimakasih telah menggunakan program ini. Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih 'mencari', 'menambahkan', atau 'keluar'.")

main()
