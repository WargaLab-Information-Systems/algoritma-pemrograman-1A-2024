class BimbinganIntensif:
    def __init__(data):
        data.siswa = {}  # Dictionary untuk menyimpan data siswa
        data.kelas = {}  # Dictionary untuk menyimpan pengelompokan kelas

    def tambah_siswa(data):
        print("\n=== Tambah Data Siswa ===")
        nama = input("Masukkan nama siswa: ")
        if nama in data.siswa:
            print("Siswa dengan nama tersebut sudah terdaftar!")
            return
        
        kelas = input("Masukkan kelas: ")
        asal_sekolah = input("Masukkan asal sekolah: ")
        plotting = input("Masukkan plotting bimbingan (contoh: Matematika Pagi): ")

        # Menyimpan data siswa
        data.siswa[nama] = {
            'kelas': kelas,
            'asal_sekolah': asal_sekolah,
            'plotting': plotting
        }

        # Mengelompokkan siswa ke dalam kelas bimbingan
        if plotting not in data.kelas:
            data.kelas[plotting] = []
        data.kelas[plotting].append(nama)

        # Mengatur pengelompokan kelas otomatis
        data.atur_kelas()
        print("Data siswa berhasil ditambahkan!")

    def atur_kelas(data):
        for plotting, siswa_list in data.kelas.items():
            jumlah_siswa = len(siswa_list)
            jumlah_kelas = (jumlah_siswa + 2) // 3  # Pembulatan ke atas
            
            # Membuat pengelompokan kelas
            for i in range(jumlah_kelas):
                index_awal = i * 3
                index_akhir = min(index_awal + 3, jumlah_siswa)
                kelas_name = f"{plotting} - Kelas {i+1}"
                print(f"\n{kelas_name}:")
                for j in range(index_awal, index_akhir):
                    print(f"- {siswa_list[j]}")

    def lihat_data(data):
        while True:
            print("\n=== Lihat Data ===")
            print("1. Lihat semua data siswa")
            print("2. Lihat berdasarkan plotting")
            print("3. Cari siswa spesifik")
            print("4. Kembali ke menu utama")
            
            pilihan = input("Pilih menu (1-4): ")
            
            if pilihan == '1':
                if not data.siswa:
                    print("Belum ada data siswa!")
                else:
                    print("\nData Semua Siswa:")
                    for nama, data in data.siswa.items():
                        print(f"\nNama: {nama}")
                        print(f"Kelas: {data['kelas']}")
                        print(f"Asal Sekolah: {data['asal_sekolah']}")
                        print(f"Plotting: {data['plotting']}")
            
            elif pilihan == '2':
                if not data.kelas:
                    print("Belum ada data plotting!")
                else:
                    print("\nDaftar Plotting:")
                    for plotting in data.kelas:
                        print(f"- {plotting}")
                    pilih_plotting = input("\nMasukkan nama plotting: ")
                    if pilih_plotting in data.kelas:
                        print(f"\nSiswa dalam {pilih_plotting}:")
                        data.atur_kelas()
                    else:
                        print("Plotting tidak ditemukan!")
            
            elif pilihan == '3':
                nama = input("\nMasukkan nama siswa: ")
                if nama in data.siswa:
                    data = data.siswa[nama]
                    print(f"\nData siswa {nama}:")
                    print(f"Kelas: {data['kelas']}")
                    print(f"Asal Sekolah: {data['asal_sekolah']}")
                    print(f"Plotting: {data['plotting']}")
                else:
                    print("Siswa tidak ditemukan!")
            
            elif pilihan == '4':
                break

    def update_siswa(data):
        print("\n=== Update Data Siswa ===")
        nama = input("Masukkan nama siswa yang akan diupdate: ")
        if nama in data.siswa:
            # Hapus dari pengelompokan kelas lama
            plotting_lama = data.siswa[nama]['plotting']
            data.kelas[plotting_lama].remove(nama)
            if not data.kelas[plotting_lama]:
                del data.kelas[plotting_lama]

            # Update data
            print("\nMasukkan data baru:")
            data.siswa[nama]['kelas'] = input("Masukkan kelas baru: ")
            data.siswa[nama]['asal_sekolah'] = input("Masukkan asal sekolah baru: ")
            plotting_baru = input("Masukkan plotting bimbingan baru: ")
            data.siswa[nama]['plotting'] = plotting_baru

            # Tambahkan ke pengelompokan kelas baru
            if plotting_baru not in data.kelas:
                data.kelas[plotting_baru] = []
            data.kelas[plotting_baru].append(nama)

            print("Data berhasil diupdate!")
            data.atur_kelas()
        else:
            print("Siswa tidak ditemukan!")

    def hapus_siswa(data):
        print("\n=== Hapus Data Siswa ===")
        nama = input("Masukkan nama siswa yang akan dihapus: ")
        if nama in data.siswa:
            # Hapus dari pengelompokan kelas
            plotting = data.siswa[nama]['plotting']
            data.kelas[plotting].remove(nama)
            if not data.kelas[plotting]:
                del data.kelas[plotting]

            # Hapus data siswa
            del data.siswa[nama]
            print("Data siswa berhasil dihapus!")
            data.atur_kelas()
        else:
            print("Siswa tidak ditemukan!")

def main():
    bimbel = BimbinganIntensif()
    
    while True:
        print("\n=== SISTEM MANAJEMEN BIMBINGAN INTENSIF GEMA RIPAH ===")
        print("1. Tambah Siswa")
        print("2. Lihat Data")
        print("3. Update Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Keluar")
        
        pilihan = input("\nPilih menu (1-5): ")
        
        if pilihan == '1':
            bimbel.tambah_siswa()
        elif pilihan == '2':
            bimbel.lihat_data()
        elif pilihan == '3':
            bimbel.update_siswa()
        elif pilihan == '4':
            bimbel.hapus_siswa()
        elif pilihan == '5':
            print("\nTerima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()