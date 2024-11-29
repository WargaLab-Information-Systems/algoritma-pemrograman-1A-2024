def pengelola_pengiriman_barang(barang_list=None):
    if barang_list is None:
        barang_list = []
    while True:
        print("==== Sistem Pengelola Pengiriman Barang ====")
        
        nama_barang = input("Masukkan Nama Barang: ")
        id_barang = input("Masukkan ID Barang: ")
        
        print("1. Darurat")
        print("2. Biasa")
        print("3. Non-Darurat")
        prioritas = input("Masukkan prioritas (1/2/3): ")
        
        if prioritas == "1":
            prioritas = "Darurat"
            barang_list.insert(0, {'nama': nama_barang, 'id': id_barang, 'prioritas': prioritas})
        
        elif prioritas == "2":
            prioritas = "Biasa"
            if len(barang_list) == 0:
                barang_list.append({'nama': nama_barang, 'id': id_barang, 'prioritas': prioritas})
            else:
                for i in range(len(barang_list)):
                    if barang_list[i]['prioritas'] != "Darurat":
                        barang_list.insert(i, {'nama': nama_barang, 'id': id_barang, 'prioritas': prioritas})
                        break
                else:
                    barang_list.append({'nama': nama_barang, 'id': id_barang, 'prioritas': prioritas})
        
        elif prioritas == "3":
            prioritas = "Non-Darurat"
            barang_list.append({'nama': nama_barang, 'id': id_barang, 'prioritas': prioritas})
        
        else:
            print("Prioritas tidak valid. Pilih antara 1, 2, atau 3.")
            continue
        
        print("Daftar Barang yang Telah Dimasukkan:")
        nomor = 1
        for barang in barang_list:
            print(f"{nomor} | Nama Barang: {barang['nama']} | ID Barang: {barang['id']} | Prioritas: {barang['prioritas']}")
            nomor += 1
            
        lanjut = input("Apakah Anda ingin menambahkan barang lagi? (iya/tidak): ")
        if lanjut != "iya":
            print("Program selesai. Terima kasih!")
            break

pengelola_pengiriman_barang()
