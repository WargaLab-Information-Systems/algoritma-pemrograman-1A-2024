# soal no 1
data_karyawan = [] #list kosong yang akan menyimpan data karyawan. 
                    # Setiap data karyawan akan disimpan dalam bentuk dictionary.
def tambah_karyawan(): # fungsi ini untuk memasukkan data
    while len(data_karyawan) < 5: #Input akan diminta berulang kali hingga jumlah karyawan mencapai 5.
        print(f"Masukkan data karyawan ke-{len(data_karyawan) + 1}:") # len mengitung elemen yang ada di dalam list
        nip = input("NIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")
        

        karyawan = {  # membuat dictionary untuk karyawan
            'NIP': nip,
            'Nama': nama,
            'Alamat': alamat,
            'Departemen': departemen,
            'Jabatan': jabatan
        }
        # menambah karyawan dalam list
        data_karyawan.append(karyawan)
        print()  

    print("Jumlah karyawan sudah mencapai batas minimum (5 karyawan).")

def tampilkan_karyawan(data_karyawan):
    print("Data Karyawan: ")
    if not data_karyawan: # memeriksa apakah list data_karyawan kosong.
        print("Belum ada data karyawan yang di input.")
    else:  #fungsi akan melakukan loop (for) untuk setiap karyawan dalam list data_karyawan.
        for karyawan in data_karyawan:
            print(f"NIP        : {karyawan['NIP']}")
            print(f"Nama       : {karyawan['Nama']}")
            print(f"Alamat     : {karyawan['Alamat']}")
            print(f"Departemen : {karyawan['Departemen']}")
            print(f"Jabatan    : {karyawan['Jabatan']}")
            print()

def cari_karyawan(data_karyawan):
    print("===== PENCARIAN KARYAWAN =====")
    while True:
        jenis = input("Masukkan jenis pencarian (1. NIP/ 2. Nama/ 3. Alamat/ 4. Departemen/ 5. Jabatan) : ")
        if jenis == "1":
            jenis = "NIP"
            break
        elif jenis == "2":
            jenis = "Nama"
            break
        elif jenis == "3":
            jenis = "Alamat"
            break
        elif jenis == "4":
            jenis = "Departemen"
            break
        elif jenis == "5":
            jenis = "Jabatan"
            break
        else:
            print("Input invalid....")

    nilai = input(f"Cari data {jenis} : ")

    hasil = []
    for karyawan in data_karyawan: #membandingkan nilai dari atribut tersebut dengan nilai yang diinginkan (nilai), 
        if karyawan.get(jenis) and karyawan[jenis].lower() == nilai.lower(): #tanpa memperhatikan huruf besar atau kecil
            hasil.append(karyawan) #jika karyawan memenuhi kriteria yang ditentukan
                                    # maka data karyawan tersebut ditambahkan ke dalam list hasil
    if hasil:
        print("Hasil pencarian: ")
        for karyawan in hasil:
            print(f"  NIP        : {karyawan['NIP']}")
            print(f"  Nama       : {karyawan['Nama']}")
            print(f"  Alamat     : {karyawan['Alamat']}")
            print(f"  Departemen : {karyawan['Departemen']}")
            print(f"  Jabatan    : {karyawan['Jabatan']}")
            print()
    else:
        print("Data tidak ditemukan.") #Jika tidak ada karyawan yang memenuhi kriteria,akan ditampilkan pesan "Data tidak ditemukan."
                                       
def remove_karyawan(data_karyawan): # untuk menghapus data karyawan berdasarkan pilihan pengguna
    print("===== HAPUS DATA =====")
    if not data_karyawan: #ungsi memeriksa apakah list data_karyawan kosong.
        print("Belum ada data karyawan yang bisa dihapus.")
        return

    for i in range(len(data_karyawan)):
        karyawan = data_karyawan[i]
        print(f"{i + 1}. NIP: {karyawan['NIP']}, Nama: {karyawan['Nama']}, Alamat: {karyawan['Alamat']}, Departemen: {karyawan['Departemen']}, Jabatan: {karyawan['Jabatan']}")
    
    pilihan = input("Pilih nomor yang ingin dihapus : ")  #Fungsi memeriksa apakah input yang diberikan adalah angka 
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(data_karyawan):  # dan apakah angka tersebut berada dalam rentang yang valid
        print("Nomor tidak valid.")
        return
    pilihan = int(pilihan) # Jika input valid, pilihan diubah menjadi integer.
    del data_karyawan[pilihan - 1] # dan karyawan yang dipilih dihapus dari list menggunakan perintah del(menghapus)
    print("Berhasil menghapus...")

while True: #Loop utama yang menampilkan menu untuk pengguna.
    print("\n===== SELAMAT DATANG DI PT GRAMEDIA =====")
    print("1. Tambah Karyawan")
    print("2. Cari Karyawan")
    print("3. Daftar Karyawan")
    print("4. Hapus Data Karyawan")
    print("5. Keluar")
    pilih = int(input("Silahkan pilih menu : "))

    if pilih == 1:
        tambah_karyawan()
    elif pilih == 2:
        cari_karyawan(data_karyawan)
    elif pilih == 3:
        tampilkan_karyawan(data_karyawan)
    elif pilih == 4:
        remove_karyawan(data_karyawan)
    elif pilih == 5:
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
