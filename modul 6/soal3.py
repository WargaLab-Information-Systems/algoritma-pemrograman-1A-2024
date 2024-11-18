barang_list = []
def tambah(barang_list):
    print("---Program Pengiriman Barang---")
    nama = str(input("masukkan nama barang anda : "))
    id = int(input("masukkan ID barang anda : "))
    print("tingkat prioritas")
    print("1. darurat")
    print("2. biasa")
    print("3. non-darurat")
    prioritas = int(input("pilih tingkat prioritas anda : "))

    barang = (nama, id, prioritas)
    akhir = barang_list
    print()
    if prioritas == 1:
        akhir.insert(0, barang)
    elif prioritas == 2:
        if len(barang_list) > 1:
            akhir.insert(len(barang_list) // 2, barang)
        else:
            akhir.append(barang)
    elif prioritas == 3:
        akhir.append(barang)
    else:
        print("maaf inputan anda salah!")
        pass

def tampilkan(barang_list):
    print()
    print("daftar barang yang telah diinput")
    for barang in barang_list:
        print(f"Nama     : {barang[0]}")
        print(f"ID       : {barang[1]}")
        print(f"Prioritas: {barang[2]}")

while True:
    tambah(barang_list)
 
    ulang = input("apakah anda ingin menambah barang lagi? (y/n): ")
  
    if ulang == "y":
        continue
    elif ulang == "n":
        print("program telah selesai!")
        print("terima kasih! !")
        break
    else:
        print("maaf inputan anda salah")
        pass
tampilkan(barang_list)
