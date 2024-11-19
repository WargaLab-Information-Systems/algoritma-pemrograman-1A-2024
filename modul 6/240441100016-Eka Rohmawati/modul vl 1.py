#daftar untuk menyimpan data karyawan
karyawan_list = []

def tambah_karyawan(nip, nama, alamat, departemen, jabatan):
    karyawan = (nip, nama, alamat, departemen, jabatan)
    karyawan_list.append(karyawan)

def tampilkan_karyawan():
    print("Daftar Karyawan:")
    for karyawan in karyawan_list:
        print(f"NIP: {karyawan[0]}")
        print(f"Nama: {karyawan[1]}")
        print(f"Alamat: {karyawan[2]}")
        print(f"Departemen: {karyawan[3]}")
        print(f"Jabatan: {karyawan[4]}")

def cari_karyawan(cari_atribut):
    hasil_cari = []
    for karyawan in karyawan_list:
        if cari_atribut in karyawan[0]:
            hasil_cari.append(karyawan)
        elif cari_atribut in karyawan[1]:
            hasil_cari.append(karyawan)
        elif cari_atribut in karyawan[2]:
            hasil_cari.append(karyawan)
        elif cari_atribut in karyawan[3]:
            hasil_cari.append(karyawan)
        elif cari_atribut in karyawan[4]:
            hasil_cari.append(karyawan)
    return hasil_cari

#input minimal 5 data karyawan
while len(karyawan_list) < 5:
    print(f"masukkan data karyawan ke-{len(karyawan_list) + 1}:")
    nip = input("masukkan nip: ")
    nama = input("masukkan nama: ")
    alamat = input("masukkan alamat: ")
    departemen = input("masukkan departemen: ")
    jabatan = input("masukkan jabatan: ")
    print()
    
    #menambahkan karyawan ke list
    tambah_karyawan(nip, nama, alamat, departemen, jabatan)

print("data karyawan telah berhasil dimasukkan.")

#pencarian data karyawan
while True:
    ulang = input("masukkan atribut yang ingin dicari (nip/nama/alamat/departemen/jabatan) atau (no) untuk berhenti: ")
    if ulang == 'no':
        print("terimakasi")
        break

    #mencari karyawan berdasarkan atribut
    hasil = cari_karyawan(ulang)
    if hasil:
        print("Hasil Pencarian:")
        for karyawan in hasil:
            print(f"nip: {karyawan[0]}")
            print(f"nama: {karyawan[1]}")
            print(f"alamat: {karyawan[2]}")
            print(f"departemen: {karyawan[3]}")
            print(f"jabatan: {karyawan[4]}")
            print()
    else:
        print("Tidak ada karyawan yang ditemukan dengan atribut tersebut")