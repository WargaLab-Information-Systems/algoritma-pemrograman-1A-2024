data_barang = []

def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Masukkan Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ").lower()
    
    barang = {"Nama Barang": nama_barang, "ID Barang": id_barang, "Prioritas": prioritas}
    
    if prioritas == "darurat":
        data_barang.insert(0, barang) 
    elif prioritas == "biasa":
        posisi_biasa = len([b for b in data_barang if b['Prioritas'] == "darurat"])
        data_barang.insert(posisi_biasa, barang)  
    elif prioritas == "non-darurat":
        data_barang.append(barang)  
    else:
        print("Prioritas tidak valid. Data barang tidak ditambahkan.")
        return
    
    print("Data barang berhasil ditambahkan.")

def tampilkan_barang():
    if not data_barang:
        print("Belum ada data barang yang ditambahkan.")
    else:
        print("\nDaftar Barang:")
        for barang in data_barang:
            print(f"Nama Barang: {barang['Nama Barang']}, ID Barang: {barang['ID Barang']}, Prioritas: {barang['Prioritas']}")

while True:
    tambah_barang()
    tampilkan_barang()
    
    lanjut = input("\nApakah Anda ingin menambahkan barang lagi? (y/n): ").lower()
    if lanjut != 'y':
        print("Program selesai.")
        break