peminjaman = {
    "glukometer": 2,
    "termometer": 3,
    "Sphygmomanometer": 4,
    "alat Inhaler": 0
}

def tampilkan_peminjaman(peminjaman):
    print()
    print("--- List Peminjaman Heni ---")
    for key, values in peminjaman.items():
        print(f"{key}: {values}")
    print()

def pengembalian(peminjaman):
    peminjaman.update({"glukometer" : 1})
    peminjaman.update({"termometer" : 1})

    del peminjaman["Sphygmomanometer"]
    peminjaman["Sphygmomanometer"] = 1
    peminjaman["alat Inhaler"] = 2
    print()
    print("--- list peminjam Heni setelah seminggu ---")
    for key, values in peminjaman.items():
        if values > 0:
            print(f"{key}: {values}")
    print()

def menu():   
    while True:
        print()
        print("=== Selamat datang di Lab ===")
        print("apa yang ingin anda cek:")
        print("1. list peminjaman Heni")
        print("2. pengembalian Heni")

        cek = int(input("apa yang ingin anda cek ? 1 atau 2"))

        if cek == 1:
            tampilkan_peminjaman(peminjaman)
            break
        elif cek == 2:
            ask = input("apakah Heni telah meminjam selama 7 hari ? [ya/no] ")
            if ask == "ya":
                pengembalian(peminjaman)
            elif ask == "no":
                print("program selesai,terimakasih")
            break
        else:
            print("inputan anda salah")
            break
menu()