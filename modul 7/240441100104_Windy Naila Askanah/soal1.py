peminjaman_alat = {
    'glukometer' : 2,
    'termometer' : 3,
    'sphygmomanometer' : 4,
    'inhaler' : 0
}

def data_peminjaman(peminjaman_alat):
    print("*** alat yang dipinjam heni ***")
    for key, values in peminjaman_alat.items():
        print(f"{key}: {values}")
    print()

def pengembalian_alat(peminjaman_alat):
    peminjaman_alat.update({"glukometer" : 1})
    peminjaman_alat.update({"termometer" : 2})
    del peminjaman_alat["sphygmomanometer"]
    peminjaman_alat["sphygmomanometer"] = 1
    peminjaman_alat["inaler"] = 2
    print()
    print("*** alat yang dipinjam heni setelah 1 minggu ***")
    for key, values in peminjaman_alat.items():
        if values > 0:
            print(f"{key}: {values}")
    print()

def menu():
    while True:
        print()
        print("=== Selamat datang di Lab ===")
        print("apa yang ingin anda pilih : ")
        print("1. list peminjaman Heni")
        print("2. pengembalian Heni")

        pilihan = int(input("[1/2] ? "))

        if pilihan == 1:
            data_peminjaman(peminjaman_alat)
        elif pilihan == 2:
            tanya = input("apakah Heni telah meminjam selama 7 hari ? [iya/gak] ")
            if tanya == "iya":
                pengembalian_alat(peminjaman_alat)
            elif tanya == "gak":
                menu()
        else:
            print("masukkan inputan yang benar!!!")
            continue

        lagi = input("apakah anda ingin kembali ke menu awal ? [iya/gak] ")
        if lagi== "iya":
            continue
        elif lagi == "gak":
            print("Program telah selesai!")
            print("Terima kasih!")
            break
        else:
            print("masukkan inputan yang benar!!!")
            break
menu()