data_barang = []

while True:
    print("Pengelola Pengiriman Barang")
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Pilih Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ")

    if prioritas not in ["Darurat", "Biasa", "Non-Darurat"]:
        print("Prioritas tidak valid. Silakan pilih antara Darurat, Biasa, atau Non-Darurat.")
        break  

    if prioritas == "Darurat":
        data_barang = [(nama_barang, id_barang, prioritas)] + data_barang
    elif prioritas == "Biasa":
        tengah = (len(data_barang) + 1) // 2  
        data_barang = data_barang[:tengah] + [(nama_barang, id_barang, prioritas)] + data_barang[tengah:]
    elif prioritas == "Non-Darurat":
        data_barang.append((nama_barang, id_barang, prioritas))

    print("Data Barang yang Telah Dimasukkan:")
    for barang in data_barang:
        print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

    lagi = input("\nApakah Anda ingin menambahkan barang lagi? (ya/tidak): ")
    if lagi != 'ya':
        print("Terima kasih! Program selesai.")
        break