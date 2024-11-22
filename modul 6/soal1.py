def input_karyawan():
    karyawan_list = []
    for _ in range(5):
        nip = input("Masukkan Data Karyawan \nNIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")
        karyawan_list.append((nip, nama, alamat, departemen, jabatan))
    return karyawan_list


def cari_karyawan(karyawan_list, katakunci):
    hasil_cari = []
    for karyawan in karyawan_list:
        for kolom in karyawan:
            if katakunci in kolom:  # Pencarian tanpa lower()
                hasil_cari.append(karyawan)
                break  # Jika ditemukan, tidak perlu periksa field lain
    return hasil_cari


def Karyawan():
    karyawan_list = input_karyawan()
    
    while True:
        keyword = input("\nMasukkan kata kunci untuk pencarian Karyawan (atau ketik 'exit' untuk keluar): ")
        if keyword == 'exit':
            break
        
        hasil_cari = cari_karyawan(karyawan_list, keyword)
        
        if hasil_cari:
            print("\nData Karyawan yang ditemukan:")
            for nip, nama, alamat, departemen, jabatan in hasil_cari:
                print(f"NIP: {nip}, Nama: {nama}, Alamat: {alamat}, Departemen: {departemen}, Jabatan: {jabatan}")
        else:
            print("Tidak ada data karyawan yang sesuai.")

Karyawan()
