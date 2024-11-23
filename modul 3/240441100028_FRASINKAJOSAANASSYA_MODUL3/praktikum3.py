# #soal no 1
# size = int(input("Masukkan angka size yang anda inginkan= "))
# #b=baris
# #k=kolom
# # angka 0
# for b in range (size):
#     for k in range (size):
#         if b == 0 or b == size - 1 or k == 0 or k == (size // 1) - 1 :
#             print("+", end="")
#         else:
#             print(" ", end="")
#     print()
# print() # spasi antar angka 

# #angka 2
# for b in range (size):
#     for k in range (size // 1):
#         if b == 0 or b == size // 2 or b == size - 1 or b == size // 1 or k == size // 1 - 1 and b < size // 2 or k == 0 and b > size // 2 :
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# # angka 8
# for b in range (size):
#     for k in range (size // 1):
#         if b == 0 or b == size - 1 or b == size // 2 or k == 0 or k == (size // 1) - 1 :
#             print("+", end="")
#         else:
#             print(" ", end="")
#     print()
# print() # spasi antar angka 



# # #soal no 2
# angka = input("masukkan angka bilangan bulat dinamis:")
# angka_balik=""
# for digit in angka:
#     angka_balik = digit + angka_balik
# #hasil
# print(f"angka telah dibalik:",angka_balik)



#soal 3
while True:
    try :
        hari_terlambat = int(input("masukkan hari keterlambatan : "))
        denda = 0

        if hari_terlambat > 5 :
            # denda lebih 5 hari kurang dari 10 hari
            if hari_terlambat <= 10 :
                denda = (hari_terlambat - 5) * 2500
            else :
                # denda normal 5 hari pertama (2500)
                denda = (10 - 5) * 2500

                # hitung denda tambahan untuk lebih 10 hari
                hari_tambahan = hari_terlambat - 10
                denda += hari_tambahan * 2500

                # denda tambahan setiap per 5 harinya 
                denda += (hari_tambahan // 5 ) * 5500
        print ("total denda keterlambatan : ", denda)
    except ValueError :
        print("Maaf input yang anda masukkan eror!!!")
    ulang = input("Ingin menghitung kembali? (ya/tidak): ".strip().lower())
    if ulang != "ya" :
        break





