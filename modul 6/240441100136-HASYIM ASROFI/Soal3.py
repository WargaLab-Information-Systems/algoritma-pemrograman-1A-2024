list_barang = []

def tambah_barang():
    while True:
        id_barang = input("Masukkan ID Barang (angka): ")
        if not id_barang.isdigit():
            print("!! ID barang harus berupa angka !!")
            continue
        id_barang = int(id_barang)
        
        # Cek apakah ID barang sudah ada
        if any(i['id'] == id_barang for i in list_barang):
            print("!! Barang dengan ID tersebut sudah ada !!")
            continue
        break
    
    nama_barang = input("Masukkan Nama Barang: ").strip()
    while not nama_barang:
        print("Nama barang tidak boleh kosong!")
        nama_barang = input("Masukkan Nama Barang: ").strip()
    
    prioritas = input("Prioritas Barang (darurat, biasa, non-darurat): ").lower()
    while prioritas not in ["darurat", "biasa", "non-darurat"]:
        print("Masukkan sesuai dengan format yang ditentukan (darurat, biasa, non-darurat)")
        prioritas = input("Prioritas Barang (darurat, biasa, non-darurat): ").lower()
    
    # Tambahkan barang berdasarkan prioritas
    barang = {"id": id_barang, "nama": nama_barang, "prioritas": prioritas}
    
    if prioritas == "darurat":
        list_barang.insert(0, barang)
    elif prioritas == "biasa":
        index = next((i for i, item in enumerate(list_barang) if item["prioritas"] == "non-darurat"), len(list_barang))
        list_barang.insert(index, barang)
    else:  # non-darurat
        list_barang.append(barang)

def tampilkan_barang():
    print("\nDaftar Barang:")
    if not list_barang:
        print("Tidak ada barang yang terdaftar.")
    else:
        for i in list_barang:
            print(f"ID: {i['id']}, Nama: {i['nama']}, Prioritas: {i['prioritas']}")

while True:
    tambah_barang()
    tampilkan_barang()
    
    konfirmasi = input("\nApakah Anda ingin menambah barang lagi? (y/n): ").lower()
    if konfirmasi != "y":
        break

print("Terima Kasih!")
