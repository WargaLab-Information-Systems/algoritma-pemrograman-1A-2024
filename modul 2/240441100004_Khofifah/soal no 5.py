nama = str(input("Masukkan nama pembeli:"))
usia = int(input("Masukkan usia pembeli:"))
total_belanja = int(input("total belanja Rp:"))
member_input = str(input("Apakah anda memiliki kartu member?(ya/tidak):"))
diskon = 0

if usia <18:
    print("Maaf anda tidak cukup usia")

else:
    if member_input == "ya":
            diskon += 15
    if total_belanja > 500000:
            diskon += 10
    total_sebelum_diskon= total_belanja
    total_setelah_diskon = total_belanja*(1-diskon/100) 

    print(f"nama pembeli:{nama}")
    print(f"diskon yang didapat:Rp.{diskon}")
    print(f"total harga sebelum diskon:Rp.{int(total_sebelum_diskon)}")
    print(f"total harga sesudah diskon:Rp.{int(total_setelah_diskon)}")