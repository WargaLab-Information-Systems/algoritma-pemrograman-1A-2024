# List untuk menyimpan data karyawan
data_karyawan = []

# Fungsi untuk menambah data karyawan
def tambah_karyawan(nip, nama, alamat, departemen, jabatan):
    karyawan = {
        "nip": nip,
        "nama": nama,
        "alamat": alamat,
        "departemen": departemen,
        "jabatan": jabatan}
    data_karyawan.append(karyawan)

# Fungsi untuk menampilkan seluruh data karyawan
def tampilkan_karyawan():
    print("\nData Karyawan:")
    if data_karyawan:
        for k in data_karyawan:
            print(f"NIP: {k['nip']}, Nama: {k['nama']}, Alamat: {k['alamat']}, Departemen: {k['departemen']}, Jabatan: {k['jabatan']}")
    else:
        print("Tidak ada data karyawan.")

# Fungsi untuk mencari karyawan berdasarkan atribut tertentu
def cari_karyawan(atribut, nilai):
    hasil_cari = []
    for k in data_karyawan:
        if k.get(atribut) == nilai:  # Menggunakan .get() untuk mengakses nilai atribut
            hasil_cari.append(k)
    return hasil_cari

# Input data karyawan (minimal 5)
for i in range(5):
    print(f"\nMasukkan data karyawan ke-{i + 1}")
    nip = input("NIP: ")
    nama = input("Nama: ")
    alamat = input("Alamat: ")
    departemen = input("Departemen: ")
    jabatan = input("Jabatan: ")
    tambah_karyawan(nip, nama, alamat, departemen, jabatan)

# Menu utama
while True:
    print("\nMenu:")
    print("1. Tampilkan semua data karyawan")
    print("2. Cari data karyawan")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        tampilkan_karyawan()
    elif pilihan == "2":
        atribut = input("Masukkan atribut yang ingin dicari (nip/nama/alamat/departemen/jabatan): ")
        nilai = input(f"Masukkan nilai untuk {atribut}: ")
        hasil = cari_karyawan(atribut, nilai)
        if hasil:
            print("\nHasil Pencarian:")
            for k in hasil:
                print(f"NIP: {k['nip']}, Nama: {k['nama']}, Alamat: {k['alamat']}, Departemen: {k['departemen']}, Jabatan: {k['jabatan']}")
        else:
            print("Karyawan tidak ditemukan.")
    elif pilihan == "3":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")