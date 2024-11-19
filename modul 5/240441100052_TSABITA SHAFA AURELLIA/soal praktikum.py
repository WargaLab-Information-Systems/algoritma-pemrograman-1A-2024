# soal 1
# def calculate_discount(total_belanja, keanggotaan):
    
#     diskon = 0  # Inisialisasi diskon 

#     # Diskon tambahan jika total belanja lebih dari 1 juta
#     if total_belanja > 1000000:
#         diskon += 0.05  # Tambahan diskon 5%

#     # Diskon berdasarkan jenis keanggotaan
#     if keanggotaan == "gold":
#         diskon += 0.15  # Diskon 15% untuk Gold
#     elif keanggotaan == "silver":
#         diskon += 0.10  # Diskon 10% untuk Silver
#     elif keanggotaan == "bronze":
#         diskon += 0.05  # Diskon 5% untuk Bronze
#     else:
#         diskon += 0.0  # Tidak ada diskon untuk yang tidak punya keanggotaan

#     # Menghitung total diskon
#     total_diskon = total_belanja * diskon
#     total_setelah_diskon = total_belanja - total_diskon

#     return total_diskon, total_setelah_diskon

# # Input dari pengguna
# total_belanja = float(input("Masukkan total harga belanja: "))
# keanggotaan = input("Apa jenis keanggotaan Anda (gold/silver/bronze/tidak): ")

# # Menghitung diskon
# total_diskon, total_setelah_diskon = calculate_discount(total_belanja, keanggotaan)

# # Menampilkan hasil
# print(f"Total diskon: {total_diskon}")
# print(f"Total yang harus dibayar: {total_setelah_diskon}")


#  soal 2
# def fibonacci(n):
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     return fibonacci(n-1)+ fibonacci(n-2)

# n = int(input("masukkan angka yang ingin dihitung : "))
# print(f"hasilnya adalah {fibonacci(n)}")
  


# soal 3
# n = int(input("masukan angka yang dihitung :"))
# def factorial(n):
#     if n == 0:
#       return 1
#     else:
#       return n * factorial(n-1)
# print("hasil dari",n,"factorial adalah",factorial(n))


# soal NO 4
#input dari pengguna
# kata = input("Masukkan kata yang ingin diperiksa: ")
# def palindrom(kata):
#     # Memeriksa apakah kata adalah palindrom
#     if kata == kata[::-1]: # slicing mengembalikan string
#         return True  # Jika kata sama dengan kebalikannya
#     else:
#         return False  # Jika tidak sama

# if palindrom(kata): # Menampilkan hasil pengecekan
#     print(f"{kata} adalah palindrom.")
# else:
#     print(f"{kata} bukan palindrom.")





# # print(factorial(5))
# print(factorial(3))
# print(factorial(2))
# print(factorial(0))
