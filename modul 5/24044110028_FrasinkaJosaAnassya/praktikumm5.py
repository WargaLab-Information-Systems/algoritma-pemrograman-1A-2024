# #soal no 1
# def super_market(total_belanja, member):
#     if member == "gold":
#         diskon_keanggotaan = 15
#     elif member == "silver":
#         diskon_keanggotaan = 10
#     elif member == "bronze":
#         diskon_keanggotaan = 5
#     else:
#         diskon_keanggotaan = 0

#     diskon_tambahan = 0
#     if total_belanja > 1000000:
#         diskon_tambahan = 5
#     total_diskon_persen = diskon_keanggotaan + diskon_tambahan
#     total_diskon = int(total_belanja * total_diskon_persen / 100)
#     total_bayar = int(total_belanja - total_diskon)
    
#     print("Diskon yang didapat:", total_diskon_persen, "%")
#     print("Total Diskon: Rp", total_diskon)
#     print("Harga Setelah Diskon: Rp", total_bayar)
    
#     return total_bayar
# total_belanja = int(input("Masukkan total belanja: "))
# member = input("Apa keanggotaan anda (gold/silver/bronze/tidak ada): ").lower()
# print(super_market(total_belanja, member))

# #soal no 2
# n = int(input("masukkan angka fibonacci : ")) 
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci (n - 1) + fibonacci(n - 2)
  
# print(f"fibonacci ke {n} adalah {fibonacci(n)}")

# #saol no 3
# def faktorial(i):
#     if i == 0:
#         return 1
#     else:
#         # return: i! = i * (i-1)!
#         return i * faktorial(i - 1)
# n = int(input("masukkan nilai dari n: "))
# print(f"{n}! ={faktorial(n)}")

#soal no 4
def cek_palindrom(kata):
    kata = kata
    return kata == kata[::-1]
    #mengambil elemen dari urutan dalam arah terbalik
kata_input = input("Masukkan kata: ")
if cek_palindrom(kata_input):
    print(f"'{kata_input}' adalah palindrom.")
else:
    print(f"'{kata_input}' bukan palindrom.")