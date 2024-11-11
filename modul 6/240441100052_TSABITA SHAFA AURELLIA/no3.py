# soal no 3

data_barang = [] # digunakan untuk menyimpan informasi barang yang dimasukkan. Setiap barang disimpan sebagai dictionary.
def pendataan_barang():  #Fungsi ini akan terus berjalan dalam loop,
    while True:          # memungkinkan pengguna untuk memasukkan informasi barang baru sebanyak yang diinginkan
        print("===== WELCOME TO JNT EXPRESS=====")
        barang = input("Masukkan nama barang : ")  #Pengguna diminta untuk memasukkan nama barang 
        id_barang = int(input("Buat ID barang : ")) #dan ID barang yang brp angka (int)
        while True:              # Pengguna diminta untuk memilih status prioritas barang. 
            print("STATUS PRORITAS BARANG\n 1. Darurat\n 2. Biasa\n 3. Non-Darurat")  
            status = int(input("Masukkan status : "))
            
            if status == 1 :  # Jika pengguna memilih status 1 (Darurat), barang akan ditambahkan ke awal list data_barang.
                status = "Darurat"
                data_barang.insert(0, {"Nama Barang": barang , "ID Barang": id_barang, "Prioritas": status})
                break
            elif status == 2 : #Jika statusnya Biasa, program mencari posisi terakhir dari barang Darurat 
                status = "Biasa"  #dan menempatkan barang baru setelahnya.
                index_awal = 0
                i = 0
                for darurat in data_barang:
                    if darurat["Prioritas"] == "Darurat":
                        index_awal = i + 1
                    i += 1
                data_barang.insert(index_awal, {"Nama Barang": barang , "ID Barang": id_barang, "Prioritas": status})
                break
            elif status == 3 :  # Jika statusnya Non-Darurat, barang akan ditambahkan ke akhir list data_barang.
                status = "Non-Darurat"
                data_barang.append({"Nama Barang": barang , "ID Barang": id_barang, "Prioritas": status})
                break
            else:
                print("Invalid")
        print("\n ===== DATA BARANG SAAT INI =====")
        for data in data_barang:
            print(f"\n Nama Barang: {data["Nama Barang"]}\n ID Barang: {data["ID Barang"]}\n Status: {data["Prioritas"]}")
        # Setelah setiap input barang, program menampilkan semua barang yang telah dimasukkan beserta statusnya.

        lanjut = input("Apakah ingin menginput barang? (ya/tidak) ").lower() 
        if lanjut != "ya" :
            break
        # Program menanyakan kepada pengguna apakah mereka ingin memasukkan barang lain. 
pendataan_barang()  #Jika pengguna menjawab selain "ya", loop akan berhenti.


