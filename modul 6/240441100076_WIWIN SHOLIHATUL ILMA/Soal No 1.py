data_karyawan= []
karyawan = int(input("Masukkan jumlah  karyawan: "))

for i in range (karyawan):
        print(f"masukkan data karyawan ke-{i +1}:")
        nip = input("Masukkan NIP karyawan: ")
        nama = input("Masukkan Nama karyawan: ")
        alamat = input("masukkan alamat karyawan: ")
        departemen = input("Masukkan departemen karyawan: ")
        jabatan = input("Masukkan jabatan karyawan: ")

        karyawan = (nip, nama, alamat, departemen, jabatan)
        data_karyawan.append(karyawan)
        print()

while True:
    print("Mencari Karyawan")
    print("1. Cari berdasarkan NIP")
    print("2. Cari berdasarkan Nama")
    print("3. Cari berdasarkan Alamat")
    print("4. Cari berdasarkan Departemen")
    print("5. Cari berdasarkan Jabatan")
    print("6. Keluar")

    pilihan = input("Pilih opsi karyawan (1-6): ")
    if pilihan == "6":
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
    
    hasil = input("Masukkan hasil pencarian: ")
    hasil_pencarian = []

    for karyawan in data_karyawan:
        if karyawan[atribut] == hasil:
            hasil_pencarian.append(karyawan)

    if hasil_pencarian:
        print("Hasil pencarian karyawan: ")
        for k in hasil_pencarian:
            print(f"NIP: {k[0]}, Nama: {k[1]}, Alamat: {k[2]}, Departemen: {k[3]}, Jabatan: {k[4]}")
    else:
        print("Tidak ada karyawan yang ditemukan.")

print()