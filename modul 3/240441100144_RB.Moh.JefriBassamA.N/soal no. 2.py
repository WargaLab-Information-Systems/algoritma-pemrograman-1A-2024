while True:
    # Menerima input (dinamis) angka bulat dari user
    angka = int(input("Masukkan angka bulat yang ada inginkan : "))

    if angka < 0:
        print("maaf anda harus memasukkan angka dengan benar")
    else:
        if angka > 0:
            # mengubah variabel angka menjadi string
            str_angka = str(angka)

            # Membalikkan urutan string
            str_angka_balik = str(str_angka[::-1])

            # Menampilkan hasil ouput
            print(f"Hasil Angka yang dibalik adalah : {str_angka_balik}")
            
    jawab = str(input("apakah anda ingin membalikkan angka bulat lagi ? {y/n} :"))
    
    if jawab == "y" or jawab == "ya":
        continue
    elif jawab == "n" or jawab == "tidak":
        break
    else: 
        print("maaf inputan anda invalid")
        break
      
