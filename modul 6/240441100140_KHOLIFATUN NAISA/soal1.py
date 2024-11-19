simpan = []
def data_karyawan():
    for i in range(2):
        print(f"Silakan masukkan data karyawan ke-{i + 1}")
        NIP = int(input("Masukkan NIP anda: "))
        Nama = input("Masukkan Nama anda: ")
        Alamat = input("Masukkan Alamat anda: ")
        Departemen = input("Masukkan Departemen anda: ")
        Jabatan = input("Masukkan Jabatan anda: ")
        print()
        data = [NIP,Nama,Alamat,Departemen,Jabatan]
        simpan.append(data)
    while True:
        jawab = input("Apakah anda ingin mencari data? (ya/tidak): ")
        if jawab != "ya":
            break
        print("1. NIP")
        print("2. NAMA")
        print("3. ALAMAT")
        print("4. DEPARTEMEN")
        print("5. JABATAN")
        cari = input("Silakan masukkan nomor data yang anda akan cari: ")
        if cari not in ["1", "2", "3", "4", "5"]:
            print("Nomor tidak valid.")
            continue  
        hasil = input("Silakan masukkan hasil yang anda akan cari: ")
        for data in simpan:
            if cari == "1" and str(data[0]) == hasil:
                print("Data ditemukan:")
                print(data)
            elif cari == "2" and data[1] == hasil:
                print("Data ditemukan:")
                print(data)
            elif cari == "3" and data[2] == hasil:
                print("Data ditemukan:")
                print(data)
            elif cari == "4" and data[3] == hasil:
                print("Data ditemukan:")
                print(data)
            elif cari == "5" and data[4] == hasil:
                print("Data ditemukan:")
                print(data)
data_karyawan()
