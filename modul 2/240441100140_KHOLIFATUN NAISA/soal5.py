nama = (input("masukkan nama anda: "))
usia = int(input("masukkan usia anda: "))
if usia > 18:
    total_belanja = int(input("masukkan total belanja: "))
    member = input("apakah anda memiliki kartu member? (iya/tidak:) )")
    diskon = 0
    if member == "iya":
        diskon += 15
    if total_belanja > 500000:
        diskon += 10
    hasil_diskon = total_belanja * (1 - diskon / 100) #1 adalah 100/100 rumus dari diskon 
    print(f"Nama pembeli: {nama}")
    print(f"Total belanja sebelum diskon: {total_belanja:}Rp")
    print(f"Diskon yang didapatkan: {diskon}%")
    print(f"Total harga setelah diskon: {hasil_diskon:}Rp")
else:
    print("mohon maaf anda belum legal")