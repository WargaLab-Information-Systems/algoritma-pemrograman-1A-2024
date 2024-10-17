
nama = str(input("masukkan nama anda:"))
umur = int(input("masukkan umur anda: "))
#seleksi umur
if umur <= 18:
    print(f"maaf {nama}, umur kamu belum mencukupi")
else:
    print("untuk melakukan pembayaran silahkan isi data di bawah ini")
    kartumember = str(input("apakah anda memiliki kartu member? (ya/tidak):"))
    totalbelanja = float(input("masukkan total belanja anda:"))
    #seleksi diskon
    diskon10= totalbelanja * (10/100)
    diskon15= totalbelanja * (15/100)
    diskon25= totalbelanja * (25/100)
    #menghitung harga setelah diskon
    hrgstlhdiskon10 = totalbelanja-diskon10
    hrgstlhdiskon15 = totalbelanja-diskon15
    hrgstlhdiskon25 = totalbelanja-diskon25
    if kartumember == "ya" and totalbelanja >= 500000:
        print("Halo", nama )
        print("anda mendapat diskon sebesar 25%")
        print("Total belanja anda sebesar Rp.", totalbelanja)            
        print("anda mendapatkan potongan harga sebesar Rp.",diskon25)
        print("Total akhir harga yang harus anda bayar adalah Rp.",hrgstlhdiskon25)
    elif kartumember == "tidak" and totalbelanja >= 500000:
        print("Halo", nama)
        print("anda mendapat diskon sebesar 10%")
        print("Total belanja anda sebesar Rp.",totalbelanja)
        print("anda mendapatkan potongan harga sebesar Rp.",diskon10)
        print("Total akhir harga yang harus anda bayar adalah Rp.",hrgstlhdiskon10)
    elif kartumember == "ya" and totalbelanja <= 500000:
        print("Halo", nama)
        print("anda mendapat diskon sebesar 15%")
        print("Total belanja anda sebesar Rp.",totalbelanja)
        print("anda mendapatkan potongan harga sebesar Rp.",diskon15)
        print("Total akhir harga yang harus anda bayar adalah Rp.",hrgstlhdiskon15)
    else:
         print("halo", nama)
         print("Anda tidak mendapatkan diskon belanja")
         print("Total harga yang harus anda bayar adalah Rp.",totalbelanja)
