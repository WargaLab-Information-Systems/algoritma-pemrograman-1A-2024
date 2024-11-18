# input total belanja
total_belanja = int(input("masukkan total belanja anda :"))
nama_pembeli = input("masukkan nama anda :")
member = (input("apakah anda mempunyai member ?, (ya/tidak) :"))
usia_pembeli = int(input("masukkan usia anda :"))

diskon = 0

if member == "ya":
    diskon += 10

if total_belanja > 500000:
    diskon += 10
total_harga_diskon = total_belanja - (diskon / 100 * total_belanja)

if (usia_pembeli < 18):
    print("maaf usia anda belum mencukupi")
else:
    print(nama_pembeli)
    print(total_belanja)
    print("diskon yang anda dapatkan sebesar", diskon)
    print("total harga setelah diskon :", total_harga_diskon)