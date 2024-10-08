#memiliki kartu = diskon 15%
#total belanja > 500rb = diskon 10%
#usia<18 = program berhenti

#Diskon pembelian minuman di bar
Pembeli = str(input("Masukkan nama pembeli :"))
usia = int(input("Berapa usia anda? "))
if usia <18:
    print("Maaf usia anda belum mencukupi")
    exit()

#memiliki kartu
harga_awal = int(input("Masukkan harga minuman :"))
diskon15persen = 15/100*harga_awal
harga_setelah_diskon1 = harga_awal-diskon15persen
kartu_member = str(input("Apakah anda memiliki kartu member? (iya/tidak)"))
diskon10persen = 10/100*harga_awal
harga_setelah_diskon2 = harga_awal-diskon10persen
diskon_25persen = 25/100*harga_awal
harga_setelah_diskon3 = harga_awal-diskon_25persen
if (kartu_member == "iya"):
    print(f"selamat {Pembeli} Anda mendapatkan diskon {diskon15persen} dari harga awal {harga_awal} menjadi {harga_setelah_diskon1}")
else:
    if(kartu_member == "iya" and harga_awal > 500000):
        print(f"selamat {Pembeli} Anda mendapatkan diskon {diskon_25persen} dari harga awal {harga_awal} menjadi {harga_setelah_diskon1}")
    elif (harga_awal > 500000):
        print(f"selamat {Pembeli} Anda mendapatkan diskon {diskon15persen} dari harga awal {harga_awal} menjadi {harga_setelah_diskon2}")
    else:
        print(f"Maaf {Pembeli} Anda tidak mendapatkan diskon")
#total belanja >500000
# total_belanja = int(input("Berapa total belanja anda? "))
# diskon10persen = 10/100*total_belanja
# harga_setelah_diskon2 = total_belanja-diskon10persen

# if total_belanja > 500000:
#     print(f"selamat {Pembeli} Anda mendapatkan diskon {diskon10persen} dari harga awal {total_belanja} menjadi {harga_setelah_diskon2}")
