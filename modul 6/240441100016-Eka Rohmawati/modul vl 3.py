#input data
barang_list = []

def tambah_barang(nama_barang, id_barang, prioritas):
    barang = (nama_barang, id_barang, prioritas)
#menentukan prioritas
    #untuk diawal list 
    if prioritas == "darurat":
        barang_list.insert(0, barang)
    #untuk ditengah list
    elif prioritas == "biasa":
        if len(barang_list) == 0:
            barang_list.append(barang)
        else:
            barang_list.insert(len(barang_list) // 2, barang)
    #untuk diakhir list
    elif prioritas == "non-darurat":
        barang_list.append(barang)
    else:
        print("maaf prioritas tidak ada")

def tampilkan_barang():
    print("daftar Barang:")
    for barang in barang_list:
        print(f"Nama Barang: {barang[0]}")
        print(f"id barang:  {barang[1]}")
        print(f"prioritas: {barang[2]}")

#input mengulang
while True:
#input data
    nama_barang = input("masukkan nama barang: ")
    id_barang = input("masukkan ID barang: ")
    prioritas = input("pilih tingkat prioritas(darurat, biasa, non-darurat): ")
    
    #menambahkan barang ke list
    tambah_barang(nama_barang, id_barang, prioritas)

    #menampilkan semua barang
    tampilkan_barang()

    #input jika ingin mengulang
    ulang = input("apakah Anda ingin menambahkan barang lagi? (ya/no): ")
    if ulang != 'ya':
        print("terimakasi")
        break