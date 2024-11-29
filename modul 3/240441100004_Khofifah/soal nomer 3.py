denda_perhari = 2500
denda_tambahan = 5500
while True:
    hari = int(input("masukkan berapa lama kamu meminjam DVD:"))
    if hari <= 10:
        total_denda=hari*denda_perhari
        print(f"denda yang harus dibayar =", total_denda)
    else:
        total_denda = hari*denda_perhari
        sisa_keterlambatan= hari-10
        total_denda += (sisa_keterlambatan // 5) * denda_tambahan
        print(f"Denda yang harus dibayar = Rp.", total_denda)
    ulang = input("apakah anda mau mengulang program lagi ya/tidak:")
    if ulang != "YA":
        print("terimakasih sudah menggunakan program ini")
        break