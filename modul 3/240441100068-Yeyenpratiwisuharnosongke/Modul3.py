# # # nomor 1
#Pola angka 0
# print()
# for i in range(7):
#     if (i == 0 or i == 6):
#         print("*" * 7)
#     elif (i > 0 and i < 6):
#         print("*" + " " * 5 + "*")
#POla angka 6
# print()                
# for i in range(7):
#     if(i== 0 or i == 3 or i == 6):
#         print("*" * 7)
#     elif (i < 3):
#         print("*" * 1)
#     else:
#         print("*" + " " * 5 + "*")
# #Pola angka 8
# print()
# for i in range(7):
#     if (i == 0 or i == 3 or i == 6):
#         print("*" * 7)
#     elif (i == 1 or i == 2 or i == 4 or i == 5):
#         print("*" + " " * 5 + "*")


# # #soal no 2
# bilangan_asli = int(input("Masukkan bilangan bulat: "))
# bilangan_terbalik = ""

# # Menggunakan loop untuk membalik bilangan
# while bilangan_asli > 0:
#     digit_terakhir = bilangan_asli % 10
#     bilangan_terbalik += str(digit_terakhir)
#     bilangan_asli //= 10

# # Menampilkan hasil
# print("Bilangan yang dibalik:", bilangan_terbalik)


# soal no 3
# while True:
#     hari_penyewaan = int(input("Masukkan hari keberapa anda mengembalikan DVD: "))
#     denda = 0
    
#     if hari_penyewaan > 5:
#         denda += (hari_penyewaan - 5) * 2500  
#     if hari_penyewaan > 5:
#         denda += ((hari_penyewaan - 5) // 5) * 5500  
    
#     if denda > 0:
#         print(f"Denda keterlambatan total adalah: Rp.{denda:,}")
#     else:
#         print("Tidak ada denda keterlambatan.")
    
#     respons = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
#     if respons != "ya":
#         print("Terima kasih!")
#         break