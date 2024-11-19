nama_pembeli = input("masukkan nama anda: ")
usia = int(input("berapa usia anda: "))
member = 0.15
belanja_500k = 0.10

print("=======> diskon member <=======")
if usia < 10:
    print("maaf usia anda belum cukup")
else:
    print(input("apakah anda mempunyai kartu member => "))
    total_belanja = int(input("masukkan total belanja anda: "))
    print("selamat anda mendapatkan diskon sebesar 15% Dan cukup membayar", member * total_belanja)
    print("total belanja sebelum diskon", total_belanja)


    print("\n========> diskon belanja ")
    if usia < 18 :
        print("maaf usia anda belum cukup")
    else:
        print(input("apakah anda mempunyai member => yes/no: "))
        total_belanja = int(input("masukkan total belanja anda: "))
        print("selamat karena anda berbelanja lebih dari 500k, anda mendapatkan diskon 10% Cukup membayar", belanja_500k)
        print("total belanja sebelum diskon", total_belanja)