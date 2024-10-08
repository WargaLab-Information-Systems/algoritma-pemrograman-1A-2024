#input pembeli
nama_pembeli = input("masukkan nama pembeli: ")
usia = int(input("masukkan usia pembeli: "))
if usia < 18:
    print("maaf usia anda tidak mencukupi.")


#menampilkan hasil

else:
    total_harga = int(input("masukkan total harga belanja: "))
    member = input("apakah memiliki kartu member?(ya/no): ")
    diskon = 0

    if member == 'ya':
        diskon += 15

    if total_harga > 500000:
        diskon += 10

    total_diskon = (diskon / 100) * total_harga
    total_harga_setelah_diskon = total_harga - total_diskon


    print(f"nama pembeli: {nama_pembeli}")
    print(f"diskon yang didapatkan: {diskon}%")
    print(f"total harga sebelum mendapat diskon:Rp.{total_harga}")
    print(f"total harga setelah mendapat diskon:Rp.{total_harga_setelah_diskon}")