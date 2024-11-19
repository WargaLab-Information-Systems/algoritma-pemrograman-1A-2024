# Inisialisasi daftar pengiriman barang
daftar_barang = []

def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    print("Pilih Tingkat Prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    pilihan_prioritas = input("Masukkan pilihan prioritas (1/2/3): ")

    if pilihan_prioritas == "1":
        prioritas = "Darurat"
        daftar_barang.insert(0, (nama_barang, id_barang, prioritas))
    elif pilihan_prioritas == "2":
        prioritas = "Biasa"
        index_biasa = sum(1 for barang in daftar_barang if barang[2] == "Darurat")
        daftar_barang.insert(index_biasa, (nama_barang, id_barang, prioritas))
    elif pilihan_prioritas == "3":
        prioritas = "Non-Darurat"
        daftar_barang.append((nama_barang, id_barang, prioritas))
    else:
        print("Pilihan prioritas tidak valid.")
        return

    print("\nBarang berhasil ditambahkan.")
    tampilkan_daftar_barang()

def tampilkan_daftar_barang():
    if not daftar_barang:
        print("Tidak ada barang yang terdaftar.")
    else:
        print("\nDaftar Barang:")
        print("Nama Barang | ID Barang | Prioritas")
        print("-" * 30)
        for barang in daftar_barang:
            print(f"{barang[0]} | {barang[1]} | {barang[2]}")

while True:
    tambah_barang()
    lanjut = input("Apakah Anda ingin menambahkan barang lagi? (y/n): ")
    if lanjut.lower() != "y":
        print("Program selesai.")
        break