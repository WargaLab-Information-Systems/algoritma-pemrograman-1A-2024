data_barang = []
def pendataan_barang():
    while True:
        print("===== SELAMAT DATANG DI PENGIRIMAN JNT =====")
        barang = input("Masukkan nama barang : ")
        id_barang = int(input("Buat ID barang : "))
        while True:
            print("STATUS PRORITAS BARANG\n 1. Darurat\n 2. Biasa\n 3. Non-Darurat")
            status = int(input("Masukkan status : "))
            
            if status == 1 :
                status = "Darurat"
                data_barang.insert(0, {"Nama Barang": barang , "ID Barang": id_barang, "Prioritas": status})
                break
            elif status == 2 :
                status = "Biasa"
                index_awal = 0
                i = 0
                for darurat in data_barang:
                    if darurat["Prioritas"] == "Darurat":
                        index_awal = i + 1
                    i += 1
                data_barang.insert(index_awal, {"Nama Barang": barang , "ID Barang": id_barang, "Prioritas": status})
                break
            elif status == 3 :
                status = "Non-Darurat"
                data_barang.append({"Nama Barang": barang , "ID Barang": id_barang, "Prioritas": status})
                break
            else:
                print("Invalid")
        print("\n ===== DATA BARANG SAAT INI =====")
        for data in data_barang:
            print(f"\n Nama Barang: {data["Nama Barang"]}\n ID Barang: {data["ID Barang"]}\n Status: {data["Prioritas"]}")

        lanjut = input("Apakah ingin menginput barang? (ya/tidak) ").lower()
        if lanjut != "ya" :
            break

pendataan_barang() 
