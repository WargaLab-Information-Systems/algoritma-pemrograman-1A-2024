# makan = input("apakah kamu sudah makan ? (ya/tidak) : ")
# mandi = input("apakah kamu sudah mandi ? (ya/tidak) : ")
# transportasi = input("berangkat pakai apa ? (jalan kaki/motor) : ")

# waktu = 0
# if makan == "ya":
#     waktu = 0 
# else:
#     waktu = 0 + 15
#     if mandi == "ya":
#         waktu = 0 
#     else:
#         waktu = 0 + 10
#         if transportasi == "jalan kaki":
#             waktu = 0 + 30
#         elif transportasi == "motor":
#             waktu = 0 + 15
#             if waktu < 60:
#                 print("kamu berangkat tepat waktu")
#             elif waktu > 61 :
#                 print("kamu terlambat")

# print("total waktu persiapan dan perjalanan : ", waktu)
        


def pecahkan_kode(kode_rahasia):
    hasil = ""
    for i in range(0, len(kode_rahasia), 2):
        pasangan_angka = kode_rahasia[i:i+2]
        angka = int(pasangan_angka)
        # Mengonversi angka menjadi huruf berdasarkan urutan alfabet terbalik
        huruf = chr(91 - angka)  # 91 adalah ASCII setelah Z (Z = 90)
        hasil += huruf
    return hasil

# Contoh penggunaan untuk Soal 1
kode_rahasia_1 = "1612091307"
print(pecahkan_kode(kode_rahasia_1))

# Contoh penggunaan untuk Soal 2
kode_rahasia_2 = "08260918_202613230614"
for kode in kode_rahasia_2.split("_"):
    print(pecahkan_kode(kode))

# Contoh penggunaan untuk Soal 3
kode_rahasia_3 = "162615221320_2522162608_2522162608_1726172613"
for kode in kode_rahasia_3.split("_"):
    print(pecahkan_kode(kode))

# Contoh penggunaan untuk Soal 4
kode_rahasia_4 = "0718080806_1622241815"
for kode in kode_rahasia_4.split("_"):
    print(pecahkan_kode(kode))

# Contoh penggunaan untuk Soal 5
kode_rahasia_5 = "141813022616_201209221320_2522162608"
for kode in kode_rahasia_5.split("_"):
    print(pecahkan_kode(kode))
