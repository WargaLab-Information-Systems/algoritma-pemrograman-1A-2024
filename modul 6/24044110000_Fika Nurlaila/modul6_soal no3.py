# 3. program mengelola pengiriman barang
barang_list = [] # List untuk menyimpan data barang dalam bentuk tuple

def tampilkan_barang(barang_list):
    if not barang_list:
        print("Tidak ada barang yang terdaftar.")
        return

    print("\nDaftar Barang Pengiriman:")
    print("a. Barang darurat")
    print("b. Barang biasa")
    print("c. Barang non darurat")
    print("d. Semua barang")
    
    # Input untuk memilih menu tampilan
    daftar = input("Pilih menu (a/b/c/d): ")

    if daftar == 'a':
        # Menampilkan hanya barang dengan prioritas 'Darurat'
        print("\nBarang Darurat:")
        for barang in barang_list:
            if barang[2] == 'darurat':
                print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

    elif daftar == 'b':
        # Menampilkan hanya barang dengan prioritas 'Biasa'
        print("\nBarang Biasa:")
        for barang in barang_list:
            if barang[2] == 'biasa':
                print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

    elif daftar == 'c':
        # Menampilkan hanya barang dengan prioritas 'Non-Darurat'
        print("\nBarang Non-Darurat:")
        for barang in barang_list:
            if barang[2] == 'non-darurat':
                print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

    elif daftar == 'd':
        # Menampilkan semua barang
        print("\nSemua Barang:")
        for barang in barang_list:
            print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

    else:
        print("Pilihan tidak valid!")

def tambah_barang():
    while True:
        # Input data barang
        nama_barang = input("Masukkan Nama Barang: ")
        id_barang = input("Masukkan ID Barang: ")
        prioritas = input("Masukkan Prioritas (Darurat, Biasa, Non-Darurat): ")

        def menentukan_list(barang_list, nama_barang, id_barang, prioritas):
        # Menambahkan barang sesuai dengan prioritas yang dipilih
            if prioritas == "darurat":
                barang_list.insert(0, (nama_barang, id_barang, prioritas))  # Tambahkan di awal list
            elif prioritas == "biasa":
                # Tambahkan di tengah-tengah list (kurang lebih di tengah)
                tengah = (len(barang_list)+1)//2
                barang_list.insert(tengah, (nama_barang, id_barang, prioritas))
            elif prioritas == "non-darurat":
                barang_list.append((nama_barang, id_barang, prioritas))  # Tambahkan di akhir list
            else:
                print("Prioritas tidak valid!")
        menentukan_list(barang_list, nama_barang, id_barang, prioritas)

        # Tanya apakah ingin menambah barang lagi
        lagi = input("\nApakah Anda ingin menambah barang lagi? (y/n): ")
        if lagi == "y":
            tambah_barang()
        else:
            menu()

def menu ():
    while True:
        print("\nSISTEM PENGELOLA PENGIRIMAN BARANG")
        print("1. Tambah barang")
        print("2. Tampilkan data barang")
        print("3. keluar")
        pilih = input("Pilih menu (1/2/3): ")

        if pilih == "1":
            tambah_barang()
        elif pilih == "2":
            # Hanya memanggil tampilkan_barang untuk menampilkan barang
            tampilkan_barang(barang_list)
        elif pilih == "3":
            print("sekian dan terima kasih")
            break
        else :
            print ("bukan pilihan")
menu()   