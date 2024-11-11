# # Soal No !
# size = int(input("Masukkan size: "))
# for i in range(size):
#     if (i == 0 or i == 6):
#         print("0000000")
#     elif (i == 1 or i == 2 or i == 3 or i == 4 or i == 5):
#         print("0     0")
# print()
# for i in range(size):
#     if (i == 0 or i == 3 or i == 6):
#         print("6666666")
#     elif (i == 1 or i == 2):
#         print("6      ")
#     elif (i == 4 or i == 5):
#         print("6     6")
# print()
# for i in range(size):
#     if i == 0 or i == 1 or i == 2:   
#         print("4     4")
#     elif i == 3:
#         print("4444444")
#     elif i == 4 or i == 5 or i == 6:
#         print("      4")


# soal no 2
# bilangan_asli = int(input("Masukkan bilangan bulat: "))
# bilangan_terbalik = ""

# while bilangan_asli > 0:
#     digit_terakhir = bilangan_asli % 10
#     bilangan_terbalik += str(digit_terakhir)
#     bilangan_asli //= 10

# print("Bilangan yang dibalik:", bilangan_terbalik)



# # soal no 3
# while True:
#     hari_penyewaan = int(input("Masukkan hari keberapa anda mengembalikan DVD: "))
#     denda = 0
    
#     if hari_penyewaan >= 5:
#         denda += (hari_penyewaan - 5) * 2500  
#     if hari_penyewaan > 10:
#         denda += ((hari_penyewaan - 5) // 5) * 5500
    
#     if denda > 0:
#         print(f"Denda keterlambatan total adalah: Rp.{denda:,}")
#     else:
#         print("Tidak ada denda keterlambatan.")
    
#     respons = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
#     if respons != "ya":
#         print("Terima kasih!")
#         break