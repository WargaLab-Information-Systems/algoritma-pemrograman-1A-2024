data=[]
def data_karyawan():
    for i in range(3):
        print(f"Masukkan data karyawan ke-{i+1}")
        nip=input("Masukkan NIP: ")
        nama=input("Masukkan nama: ")
        alamat=input("Masukkan alamat: ")
        departemen=input("Masukkan departemen: ")
        jabatan=input("Masukkan jabatan: ")
        karyawan=(nip,nama,alamat,departemen,jabatan)
        data.append(karyawan)
        print("Data berhasil ditambahkan.")

def cari_karyawan():
    while True:
        print("\nMenu Pencarian:")
        print("1. Cari berdasarkan NIP: ")
        print("2. Cari berdasarkan nama: ")
        print("3. Cari berdasarkan alamat: ")
        print("4. Cari berdasarkan departemen: ")
        print("5. Cari berdasarkan jabatan: ")
        print("6. Keluar")
        opsi=input("Masukkan opsi yang ingin dicari (nip/nama/alamat/departemen/jabatan): ")
        hasil=input("Masukkan hasil pencarian: ")
        
        if opsi=="nip":
            atribut=0
        elif opsi=="nama":
            atribut=1
        elif opsi=="alamat":
            atribut=2
        elif opsi=="departemen":
            atribut=3
        elif opsi=="jabatan":
            atribut=4
        else:
            print("Pilihan tidak valid.")

        hasil_pencarian=[]
        for karyawan in data:
            if karyawan[atribut]==hasil:
                hasil_pencarian.append(karyawan)

        if hasil:
            print("\nHasil pencarian: ")
            for karyawan in hasil_pencarian:
                print(f"NIP: {karyawan[0]}, nama: {karyawan[1]}, alamat: {karyawan[2]}, departemen: {karyawan[3]}, jabatan: {karyawan[4]}")
        else:
            print("Data tidak ditemukan")
data_karyawan()
cari_karyawan()