data_barang = []
def pendataan_barang():
    while True:
        print("SELAMAT DATANG DI TOKO")
        barang = input("Masukkan nama barang : ")
        id_barang = int(input("Buat ID barang : "))
        while True:
            print("STATUS PRIORITAS BARANG")
            print("1. Darurat")
            print("2. Biasa")
            print("3. Non-Darurat")
            status = int(input("Masukkan status : "))
            
            if status == 1:
                status = "Darurat"
                data_barang.insert(0, [barang, id_barang, status])
                break
            elif status == 2:
                status = "Biasa"
                index_awal = 0
                i = 0
                for darurat in data_barang:
                    if darurat[2] == "Darurat":
                        index_awal = i + 1
                    i += 1
                data_barang.insert(index_awal, [barang, id_barang, status])
                break
            elif status == 3:
                status = "Non-Darurat"
                data_barang.append([barang, id_barang, status])
                break
            else:
                print("Invalid")
        
        print("\nDATA BARANG SAAT INI")
        for data in data_barang:
            print(f"\n Nama Barang: {data[0]}\n ID Barang: {data[1]}\n Status: {data[2]}")

        lanjut = input("Apakah ingin menginput barang? (ya/tidak) ")
        if lanjut != "ya":
            break

pendataan_barang()