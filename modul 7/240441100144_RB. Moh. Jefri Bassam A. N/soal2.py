
basket = {"nanda", "sekar", "yuda", "jefri", "akbar"}
renang = {"sekar", "jefri", "putri", "reput", "hany"}


while True:
    print() 
    print("=== Selamat datang di klub ekskul basket & renang ===")
    print("1. siswa yang mengikuti kedua klub")
    print("2. siswa yang hanya mengikuti satu klub")
    print("3. semua siswa unik yang mengikuti setidaknya satu klub")
    print("4. jumlah siswa unik yang mengikuti setidaknya satu klub")

    tanya = int(input("apa yang ingin anda cek ? [1/2/3/4] "))
    if tanya == 1:
        print()
        print("--- siswa yang mengikuti kedua klub ---")
        print(basket&renang)

    elif tanya == 2:
        siswa_hanya_basket = basket.difference(renang)
        siswa_hanya_renang = renang.difference(basket)

        print()
        print("--- siswa yang hanya mengikuti satu klub ---")
        print(siswa_hanya_basket|siswa_hanya_renang)

    elif tanya == 3:
        print()
        print("--- semua siswa unik yang mengikuti setidaknya satu klub ---")
        print(basket|renang)

    elif tanya == 4:
        print()
        jumlah_siswa_unik = len(basket|renang)
        print(f"jumlah siswa unik yang mengikuti setidaknya satu klub: {jumlah_siswa_unik} orang")

    else:
        print("inputan anda salah !!!!")
        continue

    ulang = input("apakah anda ingin kembali ke menu awal ? [y/n] ")
    if ulang == "y":
        continue
    elif ulang == "n":
        print("Program telah selesai!")
        print("Terima kasih!")
        break
    else:
        print("inputan anda salah !!!!")
        continue