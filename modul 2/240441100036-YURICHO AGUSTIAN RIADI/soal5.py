nama =input("masukkan nama pembeli: ")
usia =int(input("masukkan usia pembeli: "))
total_harga =int(input("masukkan total harga: "))
kartu_member =input("apakah anda memiliki kartu member? (ya/tidak): ")

# memeriksa usia
if usia <18:
    print("maaf, usia anda belum mencukupi")
else:
    diskon = 0

# cek kartu member
if kartu_member == "ya":
    diskon += 15
    print("diskon yang di dapatkan:", diskon, "%" )
     
# cek total harga
if total_harga > 500000:
    diskon += 10
    print("diskon yang di dapatkan:", diskon, "%")

# menghitung total harga setelah diskon
total_diskon = total_harga * (diskon / 100)
total_harga_setelah_diskon = total_harga - total_diskon
