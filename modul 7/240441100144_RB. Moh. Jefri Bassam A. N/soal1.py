peminjaman = {
    "alat ukur tekanan darah": 2,
    "termometer": 3,
    "stetoskop": 4,
    "alat Inhaler": 0
}

def tampilkan_peminjaman(peminjaman):
    print()
    print("--- List Peminjaman Heni ---")
    for key, values in peminjaman.items():
        print(f"{key}: {values}")
    print()

def pengembalian(peminjaman):
    # Mengembalikan 1 alat pengukur tekanan darah dan 2 termometer
    peminjaman.update({"alat ukur tekanan darah" : 1})
    peminjaman.update({"termometer" : 1})

    # Menukar 3 stetoskop dengan 2 pengukur tensi
    del peminjaman["stetoskop"]
    peminjaman["stetoskop"] = 1
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

        cek = int(input("[1/2] ? "))

        if cek == 1:
            tampilkan_peminjaman(peminjaman)
        elif cek == 2:
            ask = input("apakah Heni telah meminjam selama 7 hari ? [ya/no] ")
            if ask == "ya":
                pengembalian(peminjaman)
            elif ask == "no":
                menu()

        ulang = input("apakah anda ingin kembali ke menu awal ? [y/n] ")
        if ulang == "y":
            continue
        elif ulang == "n":
            print("Program telah selesai!")
            print("Terima kasih!")
            break
        else:
            print("inputan anda salah")
            continue
menu()