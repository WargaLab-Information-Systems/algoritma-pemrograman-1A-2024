data_list = []

def input_data():
    i = 0
    while True:
        print(f"Masukkan data karyawan ke-{i + 1} : ")

        nip = input("Masukkan nomor NIP : ")
        nama = input("Masukkan nama : ")
        alamat = input("Masukkan alamat : ")
        departemen = input("Masukkan departemen : ")
        jabatan = input("Masukkan jabatan : ")

        data_karyawan = [nip, nama, alamat, departemen, jabatan]
        data_list.append(data_karyawan)
        print("Data karyawan telah berhasil ditambahkan!\n")
        i += 1

        if i >= 5:
            konfirmasi = input("Apakah anda ingin menginput data karyawan lagi? (y/n): ")
            if konfirmasi != "y":
                break

    return data_list

def semua_data():
    if not data_list:
        print("Tidak ada data karyawan dalam sistem ini.\n")
    else:
        print("Daftar data karyawan :")
        for index, data_karyawan in enumerate(data_list, start=1):
            print(f"{index}. NIP : {data_karyawan[0]}, Nama : {data_karyawan[1]}, Alamat : {data_karyawan[2]}, Departemen : {data_karyawan[3]}, Jabatan : {data_karyawan[4]}")
        print()

def pencarian(nip_karyawan):
    for index, data_karyawan in enumerate(data_list):
        if data_karyawan[0] == nip_karyawan:  
            return index
    return -1

def pencarian_karyawan():
    nip_karyawan = input("Masukkan NIP karyawan yang ingin dicari : ")
    index = pencarian(nip_karyawan)

    if index != -1:
        data_karyawan = data_list[index]
        print(f"Data ditemukan:\nNIP : {data_karyawan[0]}, Nama : {data_karyawan[1]}, Alamat : {data_karyawan[2]}, Departemen : {data_karyawan[3]}, Jabatan : {data_karyawan[4]}")
    else:
        print("Data karyawan tidak ditemukan.")
    print()

def menu():
    while True:
        print("======SISTEM INPUT DATA KARYAWAN======")
        print("1. Input data")
        print("2. Tampilkan data")
        print("3. Pencarian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            input_data()
        elif pilihan == "2":
            semua_data()
        elif pilihan == "3":
            pencarian_karyawan()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem input data karyawan ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.\n")

menu()
