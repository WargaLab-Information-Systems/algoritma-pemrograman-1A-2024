
# input total belanja
total_belanja = int (input("masukkan total belanja anda : "))
nama_pembeli = input("masukkan nama anda : ")
member = (input("apakah mempunyai member ?, (ya/tidak) : "))
usia_pembeli = int(input("masukkan usia anda : "))

diskon = 0

if member == "ya" :
    diskon += 15

if total_belanja > 500000:
    diskon += 10
total_harga_diskon = total_belanja - (diskon / 100 * total_belanja)

if (usia_pembeli < 18) :
    print ("maaf usia anda kurang")

else :
    print ("nama : ", nama_pembeli)
    print ("total belanja anda : ", total_belanja)
    print ("diskon yang anda dapatkan : ", diskon)
    print ("total harga setelah diskon : ", total_harga_diskon)


