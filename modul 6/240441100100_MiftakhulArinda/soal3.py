data=[]

def tambah_barang():
    while True:
        nama=input("Masukkan nama barang: ")
        id=input("Masukkan ID barang: ")
        prioritas=input("Masukkan tingkat prioritas (Darurat, Biasa, Non-Darurat): ")
        barang=(nama,id,prioritas)

        if prioritas=="Darurat":
            data.insert(0,barang)
        elif prioritas=="Biasa":
            tengah=0
            for i in data:
                if i[2]=="Non-Darurat":
                    break
                tengah+=1
            data.insert(tengah,barang)
        else:
            data.append(barang)
        print("\nBarang berhasil ditambahkan.")
    
        print("\nData Barang:")
        if not data:
            print("Tidak ada data")
        else:
            for barang in data:
                print(f"Nama barang: {barang[0]}, ID barang: {barang[1]}, Tingkat prioritas: {barang[2]}")

        lanjut=input("Apakah ingin mengisi data barang lagi atau tidak (ya/tidak): ")
        if lanjut != "ya":
            print("Terima kasih")
            break
tambah_barang()