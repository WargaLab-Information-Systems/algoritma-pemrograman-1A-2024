karyawan_list = []

def input_karyawan(karyawan_list):
    print()
    n = int(input("mau nambah berapa karyawan (min 5) ? "))
    for nambah in range(n):
        print(f"masukkan data karyawan ke-{nambah + 1}")
        nip = str(input("masukkan NIP anda : "))
        nama = str(input("masukkan nama anda : "))
        alamat = str(input("masukkan alamat anda : "))
        departemen = str(input("masukkan departemen anda : "))
        jabatan = str(input("masukkan jabatan anda : "))
        
        karyawan = (nip, nama, alamat, departemen, jabatan)
        karyawan_list.append(karyawan)
        print("karyawan berhasil diinputkan!")
    
def cari_karyawan(karyawan_list, inputan):
    akhir = [karyawan for karyawan in karyawan_list if 
                  inputan in karyawan[0]]
    return akhir

while True:
    print("menu yang bisa anda pilih:")
    print("1. input data karyawan")
    print("2. mencari data karyawan")
    print("3. keluar dari program")

    pilihan = int(input("pilih menu yang anda mau : "))
            
    if pilihan == 1:
        input_karyawan(karyawan_list)

    elif pilihan == 2:
        inputan = str(input("Masukkan kata kunci NIP untuk mencari karyawan: "))
        cari_karyawan(karyawan_list, inputan)
        
        if cari_karyawan(karyawan_list, inputan):
            print("data karyawan yang program temukan:")
            for karyawan in cari_karyawan(karyawan_list, inputan):
                print(f"NIP       : {karyawan[0]}")
                print(f"nama      : {karyawan[1]}")
                print(f"alamat    : {karyawan[2]}")
                print(f"departemen: {karyawan[3]}")
                print(f"jabatan   : {karyawan[4]}")
        elif not cari_karyawan(karyawan_list, inputan):
            print("program tidak menemukan data tersebut!")
            
    elif pilihan == 3:
        print("program telah selesai!")
        print("terima kasih! !")
        break

    else:
        print("maaf inputan anda salah!")