while True:
    lama_pinjam = int(input("Masukkan jumlah hari keterlambatan: "))
    
    if lama_pinjam <= 5:
        denda = 0
    elif lama_pinjam <= 10:
        denda = (lama_pinjam - 5) * 2500
    else:
        denda = (5 * 2500) + ((lama_pinjam - 10) // 5) * 5500 + ((lama_pinjam - 10) % 5) * 2500

    print("Total denda keterlambatan: Rp", denda)
    
    ulang = input("Apakah Anda ingin menghitung lagi? (y/t): ")
    if ulang != "y":
        break

       