while True:
    print("---Selamat Datang di Supermarket Jefri---")
    print("Pilih jenis keanggotaan anda:")
    print("1. Gold")
    print("2. Silver")
    print("3. Bronze")
    print("4. Tidak punya")

    keanggotaan = str(input("Pilih jenis keanggotaan apa yang anda punya : "))
    total_belanja = int(input("Masukkan berapa total belanja anda : Rp"))
             
    def calculate_discount():
        a = 0
        if keanggotaan == "1":
            if total_belanja > 1000000:
                a += 5
                a += 15

            elif 0 < total_belanja <= 1000000:
                a += 15

        elif keanggotaan == "2":
            if total_belanja > 1000000:
                a += 5
                a += 10

            elif 0 < total_belanja <= 1000000:
                a += 10

        elif keanggotaan == "3":
            if total_belanja > 1000000:
                a += 5
                a += 5
            elif 0 < total_belanja <= 1000000:
                a += 5

        elif keanggotaan == "4":
            if total_belanja > 1000000:
                a += 5
                a += 0
                print("Maaf anda hanya mendapatkan diskon tambahan")
            elif 0 < total_belanja <= 1000000:
                a += 5
                print("Maaf anda tidak mendapatkan diskon")
            
        else:
            print("Maaf inputan anda salah")
        print()
        print(f"Selamat diskon yang anda dapatkan sebesar {a}%")     
        b = total_belanja - (a/100 * total_belanja)
        print("Total belanja setelah diskon : Rp",b)
    calculate_discount()

    ulang = str(input("ingin kembali ke menu awal? [y/n]"))
    if ulang == "y":
        continue
    elif ulang == "n":
        break
