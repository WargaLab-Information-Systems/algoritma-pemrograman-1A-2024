def tambah_barang(barang_list):
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    
    # Meminta input prioritas
    print("Pilih Tingkat Prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    pilihan_prioritas = input("Masukkan pilihan (1-3): ")

    # Menentukan prioritas
    if pilihan_prioritas == '1':
        prioritas = "Darurat"
    elif pilihan_prioritas == '2':
        prioritas = "Biasa"
    elif pilihan_prioritas == '3':
        prioritas = "Non-Darurat"
    else:
        print("Pilihan tidak valid. Barang tidak ditambahkan.")
        return

    # Membuat tuple untuk barang
    barang = (nama_barang, id_barang, prioritas)

    # Menyimpan barang sesuai dengan prioritas
    if prioritas == "Darurat":
        barang_list.insert(0, barang)  # Tambahkan di awal
    elif prioritas == "Biasa":
        # Tambahkan di tengah-tengah
        if len(barang_list) == 0:
            barang_list.append(barang)
        else:
            for i in range(len(barang_list)):
                if barang_list[i][2] == "Non-Darurat":
                    barang_list.insert(i, barang)
                    break
            else:
                barang_list.append(barang)  # Jika tidak ada Non-Darurat, tambahkan di akhir
    elif prioritas == "Non-Darurat":
        barang_list.append(barang)  # Tambahkan di akhir

    print("Barang berhasil ditambahkan.")

def tampilkan_barang(barang_list):
    if not barang_list:
        print("Tidak ada barang yang disimpan.")
    else:
        print("\nDaftar Barang:")
        for barang in barang_list:
            print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

def barang():
    barang_list = []
    
    while True:
        tambah_barang(barang_list)
        tampilkan_barang(barang_list)

        lagi = input("\nApakah Anda ingin menambahkan barang lagi? (ya/tidak): ")
        if lagi.lower() != 'ya':
            print("Terima kasih! Program selesai.")
            break

barang()
