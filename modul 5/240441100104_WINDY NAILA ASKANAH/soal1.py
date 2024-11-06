def calculate_discount(totalbelanja, membercard):
    diskon = 0
    if totalbelanja > 1000000:
        diskon += 5
    if membercard == "gold":
        diskon += 15
    elif membercard == "silver":
        diskon += 10
    elif membercard == "bronze":
        diskon += 5

    jumlahdiskon = totalbelanja *(diskon/100)
    total_setelah_diskon = totalbelanja - jumlahdiskon

    return jumlahdiskon, total_setelah_diskon

membercard = str(input("apakah anda memiliki member card? (ada/tidak ada) : "))
if membercard == "ada":
    membercard = input("Masukkan jenis member card (Gold/Silver/Bronze) : ")
    totalbelanja = int(input("Masukkan total belanja : Rp "))


elif membercard == "tidak ada":
    membercard == "tidak"
    totalbelanja = int(input("Masukkan total belanjaan yang anda beli : Rp "))


jumlahdiskon, total_setelah_diskon = calculate_discount(totalbelanja, membercard) 

print(f"Jumlah diskon yang di dapat : Rp {jumlahdiskon:}")
print(f"Total yang harus anda dibayar : Rp {total_setelah_diskon:}")