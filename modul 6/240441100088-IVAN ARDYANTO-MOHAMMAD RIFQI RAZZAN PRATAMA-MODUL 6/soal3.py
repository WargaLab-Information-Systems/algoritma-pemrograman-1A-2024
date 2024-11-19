list_barang = []

def tambah_barang(nama_barang, id_barang, prioritas):
    data_baru = [nama_barang, id_barang, prioritas]

    if prioritas == "Darurat":
        list_barang.insert(0, data_baru)
    elif prioritas == "Biasa":
        list_barang.insert(len(list_barang) // 2, data_baru)
    elif prioritas == "Non-Darurat":
        list_barang.append(data_baru)
    
    return True

while True:
    tingkat_prioritas = ["Darurat", "Biasa", "Non-Darurat"]
    print("Pengelola pengiriman barang")

    nama_barang = input("Masukkan nama barang: ")
    id_barang = input("Masukkan ID barang: ")
    
    print("\nPilih tingkat prioritas barang: ")
    for i in range(len(tingkat_prioritas)):
        print(f"{i}. {tingkat_prioritas[i]}")
    
    prioritas = int(input("Opsi anda: "))

    if prioritas > len(tingkat_prioritas) - 1:
        print("Opsi yang anda pilih tidak terdapat dalam menu!")
        continue

    hasil = tambah_barang(nama_barang, id_barang, tingkat_prioritas[prioritas])

    if not hasil:
        print("Barang gagal ditambahkan")
        continue

    print(list_barang)

    is_lanjut = input("apakah anda ingin mengisi barang lagi atau tidak? (y/n): ")

    if is_lanjut == "n":
        print("Program diakhiri.")
        break