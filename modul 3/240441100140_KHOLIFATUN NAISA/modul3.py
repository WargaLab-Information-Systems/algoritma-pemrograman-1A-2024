
#soal no 1
# Buatlah program dengan bentuk angka NIM terakhir kalian , misalnya 036
#menampilkan angka 1
# for i in range (7):
#     if (i == 0 or i == 6):
#         print ("*" * 7) 
#     elif (i > 0 and i < 6):
#         print ("*" + " " * 5 + "*")
# print()
# #menampilkan angka 4
# for i in range(7):  
#     if (i == 0 or i == 1 or i == 2):
#         print("*" + " " * 5 + "*")  
#     elif (i == 3):   
#         print("*" * 7)                   
#     else:
#         print(" " * 6 + "*")                         
#     print()  
# #menampilkan angka 0
# for i in range(7):
#     if (i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6  ):
#         print(" " * 5 + "a")
# print ()


#soal no 2
# Sudarso ingin membuat program untuk membalikkan urutan dari sebuah angka
# bulat yang dimasukkan secara dinamis oleh pengguna. Bantulah ia dalam membuat
# program tersebut !

bilangan_bulat = int (input("masukkan bilangan bulat: "))
if bilangan_bulat < 0:
    print ("silahkan masukkan angka dengan benar")
else:
    bilangan_terbalik = " "
    while bilangan_bulat > 0:
        digit_terakhir = bilangan_bulat % 10
        bilangan_terbalik += str(digit_terakhir)
        bilangan_bulat //= 10
    print ("berikut hasil dari bilangan yang dibalik:", (bilangan_terbalik))

# #soal no 3
# # Juminten memiliki sebuah toko penyewaan DVD dengan syarat bahwa setiap
# # DVD hanya boleh dipinjam selama 5 hari. Apabila DVD tidak dikembalikan
# # sesuai waktu yang diberikan, penyewa akan dikenai denda sebesar Rp.2500/hari.
# # Selain itu apabila keterlambatan si penyewa mencapai lebih dari 10 hari, maka
# # penyewa akan dikenai denda tambahan Rp5500 untuk setiap 5 hari keterlambatan.
# # Bantulah Juminten dengan membuat program untuk menghitung total denda
# # keterlambatan berdasarkan lama waktu penyewaan dan saat perhitungan sudah
# # selesai, program akan menanyakan apakah user ingin menghitung kembali atau
# # tidak !

while True:
    lama_sewa = int(input("Masukkan lama waktu penyewaan: "))
    if lama_sewa <= 0:
        print("Maaf, anda salah penginputan.")
        break

    keterlambatan = lama_sewa - 5
    harga_sewa = 5000

    if keterlambatan < 0:
        print("Tidak ada denda keterlambatan.")
        print(f"Total yang harus anda bayar adalah: {harga_sewa}")
    else:
        denda_per_hari = 2500
        denda_tambahan = 0
        if keterlambatan > 10:
            denda_tambahan = (keterlambatan - 10) // 5 * 5500
        total_denda = keterlambatan * denda_per_hari + denda_tambahan
        print(f"Total harga sebelum denda: {harga_sewa}")
        print(f"Total denda keterlambatan: {total_denda}")
    
    jawab = input("Apakah ingin menghitung kembali? (ya/y atau tidak/n): ")
    if jawab == "y" or jawab == "ya":
        continue
    elif jawab == "t" or jawab == "tidak" :
        print("terimakasih")
        break
    else:
        print("invalid")   
        break
    # while True:
    #     lama_sewa = int(input("Masukkan lama waktu penyewaan: "))
    #     if lama_sewa <= 0:
    #         print("Maaf, anda salah penginputan.")
    #         break

    #     keterlambatan = lama_sewa - 5
    #     harga_sewa = 5000

    #     if keterlambatan < 0:
    #         print("Tidak ada denda keterlambatan.")
    #         print(f"Total yang harus anda bayar adalah: {harga_sewa}")
    #     else:
    #         denda_per_hari = 2500
    #         denda_tambahan = 0
    #         if keterlambatan > 10:
    #             denda_tambahan = (keterlambatan - 10) // 5 * 5500
    #         total_denda = keterlambatan * denda_per_hari + denda_tambahan
    #         print(f"Total harga sebelum denda: {harga_sewa}")
    #         print(f"Total denda keterlambatan: {total_denda}")
        
    #     jawab = input("Apakah ingin menghitung kembali? (ya/y atau tidak/n): ")
    #     if jawab == "y"
    #         print ("terimakasih")
    #         break
