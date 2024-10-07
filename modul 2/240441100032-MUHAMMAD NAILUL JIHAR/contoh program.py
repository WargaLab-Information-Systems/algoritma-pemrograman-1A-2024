# nama = "python"
# if nama == "python":
#     print ("Hallo " + nama)

# Kunci = "Python"
# password = input ("Masukkan Password : ")
# if password == Kunci:
#     print ("Password Benar")
# else:
#     print ("Password Salah")

# Program perintah if-elif-else
# angka = int(input("Masukkan sebuah bilangan : "))
# if angka > 0:
#     print("Angka merupakan bilangan positif")
# elif angka <0:
#     print("Angka merupakan bilangan negatif")
# else:
#     print("Angka merupakan bilangan 0")

# Program if bersarang
# x = int(input("Masukkan nilai x= "))
# y = int(input("Masukkan nilai y= "))
# if x == y:
#     print("nilai", x , "dan", y, "mempunyai nilai yang sama")
# else:
#     if x > y:
#         print (x, "lebih besar dari", y)
#     if x < y:
#         print (x, "lebih kecil dari", y)

# Latihan 1 Penyeleksi Kondisi 
# nomor_acak = 7
# print ("Tebak nomor acak dari 1 - 10")
# tebakan = int(input("Tebakan anda (bil bulat) : "))
# if tebakan == nomor_acak:
#     print ("Selamat! tebakan anda benar")
#     print ("tapi tidak ada hadiah untuk anda :")
# elif tebakan < nomor_acak:
#     print ("Tebakan anda terlalu kecil")
# else:
#     print ("Tebakan anda terlalu besar")
#     print ("selesai")

# # Latihan 2 Penyeleksi Kondisi
# a=int(input("Masukkan umur : "))
# if a <= 15:
#     print("Muda")
# elif a <= 20:
#     print("Remaja")
# else:
#     print("Tua")

# Latihan 3 Penyeleksi Kondisi Menentukan Ganjil Genap
# nilai = int(input("Masukkan Angka : "))
# if nilai % 2:
#     print("Bilangan Ganjil")
# else:
#     print("Bilangan Genap")

# Latihan 4 If Elif Else
a = int(input("masukkan angak (0-9) : "))
if a == 0:
    print("angka anda nol")
elif a == 1:
    print("angka anda satu")
elif a == 2:
    print("angka anda dua")
elif a == 3:
    print("angka anda tiga")
elif a == 4:
    print("angka anda empat")
elif a == 5:
    print("angka anda lima")
elif a == 6:
    print("angka anda enam")
elif a == 7:
    print("angka anda tujuh")
elif a == 8:
    print("angka anda delapan")
elif a == 9:
    print("angka anda sembilan")
else:
    print("angka anda not found")