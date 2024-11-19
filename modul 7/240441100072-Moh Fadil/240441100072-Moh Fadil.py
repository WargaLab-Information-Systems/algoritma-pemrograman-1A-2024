#soal no 1
alat_sehat = {
    'alat_pengukur_tekanan_darah': 0,
    'termometer': 0,
    'stetoskop': 0,
    'alat_inhaler': 0
}

# ini hari pertama
alat_sehat['alat_pengukur_tekanan_darah'] += 2
alat_sehat['termometer'] += 3

# ini hari kedua
alat_sehat['stetoskop'] += 4

# pengembalian alat dan penukaran alat setelah seminggu
# Mengembalikan 1 alat pengukur tekanan darah dan 2 termometer
alat_sehat['alat_pengukur_tekanan_darah'] -= 1
alat_sehat['termometer'] -= 2

# menukar 3 stetoskop dengan 2 alat inhaler
alat_sehat['stetoskop'] -= 3
alat_sehat['alat_inhaler'] += 2

# Menampilkan alat kesehatan yang dipinjam saat ini
print("Alat kesehatan yang dipinjam Heni saat ini:")
for alat, jumlah in alat_sehat.items():
    if jumlah > 0:
        print(f"{alat}: {jumlah}")





#soal no 2
# ini membuat dua set yang berisi nama siswa yang mengikuti klub Basket dan Renang
klub_basket = {"fadil", "riko", "warisi", "wiwin", "putri"}
klub_renang = {"riko", "warisi", "budi", "salsa"}

# ini menampilkan daftar siswa yang mengikuti kedua klub
siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)

#ini menampilkan daftar siswa yang hanya mengikuti satu klub saja
siswa_hanya_satu_klub = klub_basket.symmetric_difference(klub_renang)
print("\nSiswa yang hanya mengikuti satu klub:")
print(siswa_hanya_satu_klub)

# ini menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
siswa_unik = klub_basket.union(klub_renang)
print("\nSiswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(siswa_unik)

# ini menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
jumlah_siswa_unik = len(siswa_unik)
print("\nJumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(jumlah_siswa_unik)




# #soal no 3
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