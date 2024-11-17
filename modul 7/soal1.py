# a. Hari pertama Ia meminjam 2 alat pengukur tekanan darah dan 3 termometer
# b. Hari kedua Ia meminjam 4 alat pengukur kadar gula darah
# c. Setelah semingggu Heni mengembalikan 1 alat pengukur tekanan darah dan 2
# termometer,kemudian menukar 3 alat pengukur tekanan darah dengan 2 pengukur
# tensi.
barang = {
    "alat pengukur tekanan darah" : 2, 
    "termometer" : 3,
    "setoskop" : 4,
    "pengukur inhealer" : 2,
}
def peminjaman_barang(alat,jumlah):
    if alat in barang:
        barang[alat] += jumlah
        if barang[alat] <= 0:
            barang.pop(alat)
peminjaman_barang("alat pengukur tekanan darah", -1)
peminjaman_barang("termometer", -2)
print("alat kesehatan yang dipinjam oleh heni saat ini adalah: ")
for alat,jumlah in barang.items():
    print(f"{alat}: {jumlah} buah")

# nama = {
#     "wawan" : 5,
#     "dina" : 4,
#     "lina" : 6,
# }

# # nama.pop("wawan")
# # print(nama)
# # del nama ["wawan"]
# # print(nama)

# nama.clear()
# print(nama)


