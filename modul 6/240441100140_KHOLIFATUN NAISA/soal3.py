datapengirimanbarang = []
def datapengiriman ():
        while True:
            namabarang = str(input("masukkan nama barang: "))
            idbarang  = int(input("masukkan id barang: "))
            print("1. Darurat")
            print("2. Biasa")
            print("3. Non-Darurat")
            prioritas = int(input("prioritas barang: "))
            if prioritas == 1:
                prioritas = "Darurat"
                datapengirimanbarang.insert(0, (namabarang, idbarang, prioritas))
            elif prioritas == 2:
                prioritas = "Biasa"
                if len(datapengirimanbarang) > 1:
                    datapengirimanbarang.insert(len(datapengirimanbarang)// 2, (namabarang, idbarang, prioritas))
                else:
                    datapengirimanbarang.append((namabarang, idbarang, prioritas))
            elif prioritas == 3:
                prioritas = "Non-Darurat"
                datapengirimanbarang.append((namabarang, idbarang, prioritas))
            else:
                print("Nomor yang Anda masukkan invalid")
            for data in datapengirimanbarang:
                print(f"Nama Barang: {data[0]}")
                print(f"ID Barang: {data[1]}")   
                print(f"Prioritas: {data[2]}")
            jawab = input("apakah anda ingin menginputkan kembali?: (ya/tidak) ")
            if jawab != "ya":
                print("terimakasih")
                break
datapengiriman()
