barang = []

# Fungsi untuk menambah barang
def tambah_barang(nama_barang, id_barang, prioritas):
    if prioritas == "Darurat":
        barang.insert(0, {"nama_barang": nama_barang, "id_barang": id_barang, "prioritas": prioritas})
    elif prioritas == "Biasa":
        tengah = len(barang) // 2
        barang.insert(tengah, {"nama_barang": nama_barang, "id_barang": id_barang, "prioritas": prioritas})
    elif prioritas == "Non-Darurat":
        barang.append({"nama_barang": nama_barang, "id_barang": id_barang, "prioritas": prioritas})

# Fungsi untuk menampilkan semua barang
def tampilkan_barang():
    print("\nData Barang yang Tersimpan:")
    for b in barang:
        print(f"ID Barang: {b['id_barang']}, Nama Barang: {b['nama_barang']}, Prioritas: {b['prioritas']}")

# Menu utama
while True:
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Masukkan Prioritas Barang (Darurat/Biasa/Non-Darurat): ").capitalize()

    # Menambah barang ke dalam list sesuai prioritas
    tambah_barang(nama_barang, id_barang, prioritas)

    tampilkan_barang()

    lanjut = input("\nApakah Anda ingin menambah barang lagi? (ya/tidak): ").lower()
    if lanjut != 'ya':
        print("Program selesai.")
        break