# soal no 1
# ukuran = int (input("masukkan ukuran yang anda inginkan: "))
# huruf = str (input("masukkan huruf x/o: "))
# for i in range(ukuran):
#     for j in range (ukuran-i-1):
#         print(" ", end=" ")
#     for y in range (2*i+1):
#         print (huruf, end= " ")
#     print()

# for i in range (ukuran-2,-1,-1):
#     for j in range (ukuran-i-1):
#         print(" ", end= " ")
#     for y in range (2*i+1):
#         print (huruf, end= " ")
#     print()

#soal no 2
# desimal = int(input("masukkan angka desimal: "))
# biner = " "
# while desimal > 0:
#     sisa = desimal % 2
#     biner = str(sisa) + " " + biner 
#     desimal = desimal // 2
# print(f"bilangan binernya adalah: {biner}")

# soal no 3
# kerja 12 jam setiap hari
# gaji harian 100.000
# lembur maksimal 8 jam jika lebih akan muncul oeringatan lembur melebihi batas,tidak dihitung
# lembur dalam satu minggu mencapai atau melebihi 40 jam, lembur akan dihentikan
# 4 jam lembur mendapat 100.000, 6 jam 200.000 8 jam 300.000, lembur kurang dari 4 jam (1-3 jam) 25.000
# hitunglah total gaji selama 1 minggu gaji reguler dan lembur
# program mencetak embur perharinya, total lembur selama satu minggu, total gaji lembur. total gaji mingguan tanpa lembur. total gaji mingguan termasuk lembur.

# total_gaji = 0
# total_lembur = 0
# gaji_harian = 100000
# for hari in range(1, 8):
#     lembur = int(input(f"Anda lembur selama berapa jam di hari ke-{hari}?: "))
#     if total_lembur >= 40:
#         print("Lembur Anda sudah mencapai batas maksimum 40 jam dalam seminggu, lembur dihentikan.")
#         gaji_lembur = 0
#     else:
#         if total_lembur + lembur > 40:
#             lembur = 40 - total_lembur
#             print(f"Jam lembur hari ke-{hari} dibatasi hingga {lembur} jam.")
#         if lembur == 4:
#             gaji_lembur = 100000
#         elif lembur == 5:
#             gaji_lembur = 150000
#         elif lembur == 6:
#             gaji_lembur = 200000
#         elif lembur == 7:
#             gaji_lembur = 250000
#         elif lembur == 8:
#             gaji_lembur = 300000
#         elif lembur < 4:
#             gaji_lembur = 25000 * lembur
#         else:
#             gaji_lembur = 300000
#             print("Mohon maaf, lembur Anda melebihi batas, dan tidak akan dihitung.")
#         total_lembur += lembur
#     total_gaji += gaji_harian + gaji_lembur
#     print(f"Total gaji lembur yang Anda dapat pada hari ke-{hari} adalah: {gaji_lembur}")
# print()
# print("Total lembur selama satu minggu adalah:", total_lembur)
# print("Total gaji lembur selama satu minggu adalah:", total_gaji - (gaji_harian * 7))
# print("Total gaji mingguan tanpa lembur adalah:", gaji_harian * 7)
# print(f"Total gaji Anda selama 1 minggu termasuk lembur adalah: {total_gaji}")

