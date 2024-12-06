#Soal No 1
alat_medis = {}

def tambah_item(peralatan_dict, item, jumlah):
    if item in peralatan_dict:
        peralatan_dict[item] += jumlah
    else:
        peralatan_dict[item] = jumlah

def hapus_item(peralatan_dict, item, jumlah):
    if item in peralatan_dict:
        if peralatan_dict[item] <= jumlah:
            del peralatan_dict[item]
        else:
            peralatan_dict[item] -= jumlah
        return True
    return False

def tukar_item(peralatan_dict, item_remove, jumlah_remove, item_add, jumlah_add):
    if item_remove in peralatan_dict:
        if peralatan_dict[item_remove] >= jumlah_remove:
            if peralatan_dict[item_remove] == jumlah_remove:
                del peralatan_dict[item_remove]
            else:
                peralatan_dict[item_remove] -= jumlah_remove
            
            if item_add in peralatan_dict:
                peralatan_dict[item_add] += jumlah_add
            else:
                peralatan_dict[item_add] = jumlah_add
            return True
    return False

def lihat_item(peralatan_dict):
    if not peralatan_dict:
        print("Inventory kosong!")
        return
    
    print("Alat yang dipinjam saat ini:")
    for item, jumlah in peralatan_dict.items():
        print("-",item,":",jumlah,"buah")
    print("Total jenis alat:",len(peralatan_dict))

def input_jumlah(prompt):
    while True:
        
        jumlah = int(input(prompt))
        if jumlah > 0:
            return jumlah
        print("Jumlah harus lebih dari 0!")
        if jumlah <0:
            print("Masukkan angka yang valid !")

#program utama
while True:
    print("=== SISTEM PEMINJAMAN ALAT KESEHATAN ===")
    print("1. Pinjam alat")
    print("2. Kembalikan alat")
    print("3. Tukar alat")
    print("4. Lihat inventory")
    print("5. Keluar")
    
    menu = input("Pilih menu (1-5): ")
    
    if menu == '1':
        item = input("Masukkan nama alat: ").lower()
        jumlah = input_jumlah("Masukkan jumlah alat: ")
        tambah_item(alat_medis, item, jumlah)
        print("Berhasil meminjam",jumlah,"buah",item)
            
    elif menu == '2':
        if not alat_medis:
            print("Inventory kosong!")
            continue
            
        item = input("Masukkan nama alat yang akan dikembalikan: ").lower()
        if item not in alat_medis:
            print(item,"tidak ada dalam inventory !")
            continue
            
        jumlah = input_jumlah("Masukkan jumlah yang akan dikembalikan: ")
        if jumlah > alat_medis[item]:
            print("Jumlah melebihi yang dipinjam! (Tersedia:",alat_medis[item],"buah)")
            continue
                
        hapus_item(alat_medis, item, jumlah)
        print("Berhasil mengembalikan",jumlah,"buah",item)
            
    elif menu == '3':
        if not alat_medis:
            print("Inventory kosong!")
            continue
            
        item_remove = input("Masukkan nama alat yang akan ditukar: ").lower()
        if item_remove not in alat_medis:
            print(item_remove,"tidak ada dalam inventory !")
            continue
            
        jumlah_remove = input_jumlah("Masukkan jumlah yang akan ditukar: ")
        if jumlah_remove > alat_medis[item_remove]:
            print("Jumlah melebihi yang dipinjam! (Tersedia:",alat_medis[item_remove],"buah)")
            continue
            
        item_add = input("Masukkan nama alat pengganti: ").lower()
        jumlah_add = input_jumlah("Masukkan jumlah alat pengganti: ")
        
        tukar_item(alat_medis, item_remove, jumlah_remove, item_add, jumlah_add)
        print("Berhasil menukar",jumlah_remove,"buah",item_remove,"dengan",jumlah_add,"buah",item_add)
            
    elif menu == '4':
        lihat_item(alat_medis)
        
    elif menu == '5':
        print("Terima kasih telah menggunakan sistem ini!")
        break
        
    else:
        print("Pilihan tidak valid !")

 #Soal No 2
def analisis_club():
    print()
    print("Masukkan anggota club Basket")
    print("Ketik 'selesai' untuk mengakhiri")
    anggota_basket = set()
    while True:
        nama = input("Masukkan nama anggota basket : ")
        if nama == "selesai":
            break
        anggota_basket.add(nama)

    print()
    print("Masukkan anggota renang")
    print("Ketik 'selesai' untuk mengakhiri")
    anggota_renang = set()
    while True:
        nama = input("Masukkan nama anggota renang : ")
        if nama == "selesai":
            break
        anggota_renang.add(nama)

    print()
    print("Daftar Anggota setiap club")
    print("Anggota Club Basket : ",anggota_basket)
    print("Anggota Club Renang : ",anggota_renang)
    
    print()
    kedua_club = anggota_basket.intersection(anggota_renang)
    print("Siswa yang mengikuti kedua club")
    if kedua_club:
        for siswa in kedua_club:
            print("-",siswa)
    else:
        print("Tidak ada siswa yang mengikuti kedua club")

    hanya_basket = anggota_basket - anggota_renang
    hanya_renang = anggota_renang - anggota_basket

    print()
    print("Hanya ikut basket")
    for siswa in hanya_basket:
        print("-",siswa)
    print("Hanya ikut renang")
    for siswa in hanya_renang:
        print("-",siswa)
 
    print()
    print("Daftar siswa yang minimal mengikuti satu club")
    semua_siswa = anggota_basket.union(anggota_renang)
    for siswa in semua_siswa:
        print("-",siswa)

    print()
    print("Daftar total",)
    print("Siswa yang mengikuti basket",len(anggota_basket), "siswa")
    print("Siswa yang mengikuti renang",len(anggota_renang), "siswa")
    print("Siswa yang mengikuti kedua club",len(kedua_club), "siswa")
    print("Siswa yang hanya mengikuti basket",len(hanya_basket), "siswa")
    print("Siswa yang hanya mengikuti renang",len(hanya_renang), "siswa")

print("===Selamat Datang di program Analis Club===")
analisis_club()

# soal no 3
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