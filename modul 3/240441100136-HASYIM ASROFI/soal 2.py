while True:
    angka = input("Masukkan angka bilangan bulat: ")

    # Membalik angka menggunakan string slicing
    angka_terbalik = angka[:: -1]

    # Menampilkan hasil setelah dibalik
    print("Angka setelah dibalik:", angka_terbalik)

    # Menanyakan apakah ingin menghitung lagi
    hitung_lagi = input("Apakah Anda ingin menghitung lagi?(iya/tidak): ")
    if hitung_lagi.lower() != "iya":
        print("Terima kasih telah mencoba programku")
       break