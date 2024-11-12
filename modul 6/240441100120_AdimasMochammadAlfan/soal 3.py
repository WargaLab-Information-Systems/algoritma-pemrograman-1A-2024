List_barang = []

def pengelolaan_tambah_barang():
    nama_barang = input("Masukkan nama barang: ")
    ID_barang = input("Masukkan ID barang: ")
    print("=== Pilihlah berapa tingkatan keprioritasan barang ===\n")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    
    prioritas = input("Masukkan tingkatan prioritas (1/2/3): ")

    if prioritas == "1":
        tingkatan_prioritas = "Darurat"
    elif prioritas == "2":
        tingkatan_prioritas = "Biasa"
    elif prioritas == "3":
        tingkatan_prioritas = "Non-Darurat"
    else:
        print("Masukkan data yang valid! Prioritas harus 1, 2, atau 3.")
        return
    
    barang = (nama_barang, ID_barang, tingkatan_prioritas)

    if tingkatan_prioritas == "Darurat":
        List_barang.insert(0, barang)
    elif tingkatan_prioritas == "Biasa":
        Indeks = len([b for b in List_barang if b[2] == "Darurat"])
        List_barang.insert(Indeks, barang) 
    elif tingkatan_prioritas == "Non-Darurat":
        List_barang.append(barang) 
    
    print("Data berhasil ditambahkan!\n")

def Layar_Awal_barang():
    if not List_barang:
        print("Data barang masih kosong!\n")
    else:
        print("=== DATA BARANG ===\n")
        for barang in List_barang:
            print("Nama Barang: ", barang[0])
            print("ID Barang: ", barang[1])
            print("Tingkatan Prioritas: ", barang[2])
            print()

while True:
    print("=== Menu Pengelolaan Barang ===\n")
    print("1. Tambah Barang")
    print("2. Tampilkan Data Barang")
    print("3. Keluar")
    
    pilihan = input("Pilih opsi (1/2/3): ")
    print()

    if pilihan == '1':
        pengelolaan_tambah_barang()  
    elif pilihan == '2':
        Layar_Awal_barang()  
    elif pilihan == '3':
        print("Terima kasih telah memilih program pengelolaan barang!")
        break  
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
