nama =input("masukkan mana anda :")
usia =int(input("masuka usia anda :"))
total_belanja =float(input("masukan total belanja anda :"))
member =input("apaka kamu punya member : iya/tidak")
if member == "iya":
    member == True
else:
    member == False

if usia < 18:
    print("maaf usia belum mencukupi")

else:
    diskon = 0
    if member:
        diskon+= 0.15
    if total_belanja > 500000:
        diskon+= 0.10

diskon_rupiah = total_belanja * diskon
total_bayar = total_belanja - diskon_rupiah

print("nama anda")
print("diskon yang anda dapatkan:",diskon*100,"%")
print("total harga sebelum diskon",total_belanja)
print("total harga anda:",total_bayar)
