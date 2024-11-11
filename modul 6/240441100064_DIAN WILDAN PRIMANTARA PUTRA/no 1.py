data_karyawan = []

def tambah_karyawan():
    print("MASUKKAN DATA KARYAWAN")
    if len(data_karyawan) < 5:
        nip = input("Masukkan NIP : ")
        nama = input("Masukkan Nama : ")
        alamat = input("Masukkan Alamat : ")
        departemen = input("Masukkan Departemen : ")
        jabatan = input("Masukkan Jabatan : ")

        karyawan = [nip, nama, alamat, departemen, jabatan]
        data_karyawan.append(karyawan)
        print("Berhasil ditambahkan...")
    else:
        print("Jumlah karyawan sudah mencapai batas minimum (5 karyawan).")

def tampilkan_karyawan(data_karyawan):
    print("Data Karyawan : ")
    if not data_karyawan:
        print("Belum ada data karyawan yang di input..")
    else:
        for karyawan in data_karyawan:
            print(f"NIP        : {karyawan[0]}\nNama       : {karyawan[1]}\nAlamat     : {karyawan[2]}\nDepartemen : {karyawan[3]}\nJabatan    : {karyawan[4]}\n")

def cari_karyawan(data_karyawan):
    print("PENCARIAN KARYAWAN")
    print("1. NIP\n2. Nama\n3. Alamat\n4. Departemen\n5. Jabatan")
    
    while True:
        jenis = input("Masukkan jenis pencarian (1-5) : ")
        if jenis.isdigit() and 1 <= int(jenis) <= 5:
            jenis = int(jenis) - 1  
            break
        print("Input invalid....")

    nilai = input("Masukkan nilai yang dicari: ")
    hasil = [karyawan for karyawan in data_karyawan if karyawan[jenis].lower() == nilai.lower()]

    if hasil:
        print("Hasil pencarian : ")
        for karyawan in hasil:
            print(f"NIP        : {karyawan[0]}\nNama       : {karyawan[1]}\nAlamat     : {karyawan[2]}\nDepartemen : {karyawan[3]}\nJabatan    : {karyawan[4]}\n")
    else:
        print("Data tidak ditemukan..")

def remove_karyawan(data_karyawan):
    print("HAPUS DATA")
    if not data_karyawan:
        print("Tidak ada data karyawan untuk dihapus.")
        return
    
    for i in range(len(data_karyawan)):
        karyawan = data_karyawan[i]
        print(f"{i + 1}. NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
    
    pilihan = input("Pilih nomer yang ingin di hapus : ")
    if pilihan.isdigit() and 1 <= int(pilihan) <= len(data_karyawan):
        del data_karyawan[int(pilihan) - 1]
        print("Berhasil menghapus...")
    else:
        print("Nomer tidak valid..")

while True:
    print("\nSELAMAT DATANG DI PT PT AN")
    print("1. Tambah Karyawan\n2. Cari Karyawan\n3. Daftar Karyawan\n4. Hapus Data Karyawan\n5. Keluar")
    pilih = input("Silahkan pilih menu : ")

    if pilih == '1':
        tambah_karyawan()
    elif pilih == '2':
        if len(data_karyawan) < 5:
            print("Data karyawan belum mencukupi untuk melakukan pencarian. Pastikan minimal 5 karyawan telah ditambahkan.")
        else:
            cari_karyawan(data_karyawan)
    elif pilih == '3':
        tampilkan_karyawan(data_karyawan)
    elif pilih == '4':
        remove_karyawan(data_karyawan)
    elif pilih == '5':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")