siswa_list = []

def tambah(nama, asal_sekolah, plotting):
    kelas = (len(siswa_list) // 3) + 1
    siswa = {
        "nama": nama, 
        "kelas": kelas, 
        "asal_sekolah": asal_sekolah,
        "plotting": plotting
        }
    siswa_list.append(siswa)
    print()

def tampilkan():
    if not siswa_list:
        print("tidak ada siswa yang terdaftar dalam listt!!")
        return
    elif siswa_list:
        print()
        print("--- data bimbigan intensif Gema Ripah ---")
        for siswa in siswa_list:
            print(f"kelas        : {siswa['kelas']}")
            print(f"plotting     : {siswa['plotting']}")
            print(f"nama         : {siswa['nama']}")
            print(f"asal Sekolah : {siswa['asal_sekolah']}")
            print()
    
def update(nama, new_asal_sekolah, new_plotting):
    for siswa in siswa_list:
        if siswa["nama"] == nama:
            siswa["asal_sekolah"] = new_asal_sekolah
            siswa["plotting"] = new_plotting
            print(f"data bimbingan intensif dengan nama '{nama}' berhasil diupdate!")
        elif siswa["nama"] != nama:
            print("maaf nama tersbut tidak ada dalam data !!")
    print()

def delete(nama):
    for i in range(len(siswa_list)):
        siswa = siswa_list[i]
        if siswa["nama"] == nama:
            del siswa_list[i]
            print(f"data bimbingan intensif dengan nama '{nama}' berhasil dihapus!")
        elif siswa["nama"] != nama:
            print(f"data bimbingan intensif dengan nama '{nama}' tidak ditemukan!")
while True:
    print("=== lembaga bimbingan intensif Gema Ripah ===")
    print("1. tambah siswa")
    print("2. lihat siswa")
    print("3. update siswa")
    print("4. delete siswa")
    print("5. keluar")
    
    pilih = int(input("pilih menu yang anda mau : "))

    if pilih == 1:
        print()
        nama = input("Masukkan nama siswa: ")
        asal_sekolah = input("Masukkan asal sekolah: ")
        plotting = input("Masukkan plotting bimbingan intensif: ")
        tambah(nama, asal_sekolah, plotting)

    elif pilih == 2:
        tampilkan()

    elif pilih == 3:
        print()
        nama = input("Masukkan nama siswa yang ingin diupdate: ")
        asal_sekolah_baru = input("Masukkan asal sekolah baru: ")
        plotting_baru = input("Masukkan plotting baru: ")
        update(nama, asal_sekolah_baru, plotting_baru)

    elif pilih == 4:
        nama = input("Masukkan nama siswa yang ingin dihapus: ")
        delete(nama)

    elif pilih == 5:
        print("program telah selesai!")
        print("terima kasih! !")
        break
    
    else:
        print("maaf inputan anda salah !!!")
        continue