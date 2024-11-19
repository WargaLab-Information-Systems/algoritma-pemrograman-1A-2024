def tambah_karyawan(data_karyawan):
    while True:
        jumlah_karyawan = int(input("Masukkan jumlah karyawan (minimal 5): "))
        if jumlah_karyawan >= 5:
            break
        else:
            print("Jumlah karyawan harus minimal 5. Silakan masukkan ulang.")

    for i in range(jumlah_karyawan):
        print(f"\nMasukkan data karyawan ke-{i + 1}:")
        nip = input("Masukkan NIP karyawan: ")
        nama = input("Masukkan Nama karyawan: ")
        alamat = input("Masukkan Alamat karyawan: ")
        departemen = input("Masukkan Departemen karyawan: ")
        jabatan = input("Masukkan Jabatan karyawan: ")

        karyawan = (nip, nama, alamat, departemen, jabatan)
        data_karyawan.append(karyawan)
        print()

    print("Data karyawan berhasil ditambahkan!")
    return data_karyawan

def cari_karyawan(data_karyawan):
    while True:
        print("\nMencari Karyawan")
        print("1. Cari berdasarkan NIP")
        print("2. Cari berdasarkan Nama")
        print("3. Cari berdasarkan Alamat")
        print("4. Cari berdasarkan Departemen")
        print("5. Cari berdasarkan Jabatan")
        print("6. Keluar")

        pilihan = input("Pilih opsi karyawan (1-6): ")
        if pilihan == "6":
            print("Terimakasih sudah menggunakan pencarian")
            break

        if pilihan == "1":
            atribut = 0
        elif pilihan == "2":
            atribut = 1
        elif pilihan == "3":
            atribut = 2
        elif pilihan == "4":
            atribut = 3  
        elif pilihan == "5":
            atribut = 4  
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue
        
        hasil = input("Masukkan sesuai opsi yang dipilih: ")
        hasil_pencarian = [k for k in data_karyawan if k[atribut].lower() == hasil]
        
        if hasil_pencarian:
            print("Hasil pencarian karyawan: ")
            for k in hasil_pencarian:
                print(f"NIP: {k[0]}, Nama: {k[1]}, Alamat: {k[2]}, Departemen: {k[3]}, Jabatan: {k[4]}")
        else:
            print("Tidak ada karyawan yang ditemukan.")
        print()

def main():
    data_karyawan = []
    
    while True:
        jawab = input("Apa yang ingin Anda lakukan? (mencari/menambahkan/keluar): ")
    
        if jawab == "mencari":
            if data_karyawan:
                cari_karyawan(data_karyawan)
            else:
                print("Data karyawan masih kosong. Silakan tambahkan data terlebih dahulu.")
        
        elif jawab == "menambahkan":
            data_karyawan = tambah_karyawan(data_karyawan)
        
        elif jawab == "keluar":
            print("Terimakasih telah menggunakan program ini. Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih 'mencari', 'menambahkan', atau 'keluar'.")

main()
#menanyakan ingin mencari atau menambahkan terlebih dahulu