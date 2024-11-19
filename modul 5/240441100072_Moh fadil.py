#SOAL NO 1
# def calculate_discount(total_spending, membership_type):
#     if membership_type == "Gold":
#         discount = 0.15
#     elif membership_type == "Silver":
#         discount = 0.10
#     elif membership_type == "Bronze":
#         discount = 0.05
#     else:
#         discount = 0.0  

#     if total_spending > 1000000:
#         discount += 0.05  

#     total_discount = total_spending * discount
#     return total_discount

# total_belanja = int(input("masukkan total belanja : "))
# jenis_keanggotaan = input("masukkan type membership: ")
# diskon = calculate_discount(total_belanja, jenis_keanggotaan)
# print(f"Diskon yang didapat:{diskon}")


#SOAL NO 2
# def fibonacci(n):
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     return fibonacci(n-1)+ fibonacci(n-2)

# n = int(input("masukkan angka yang ingin dihitung : "))
# print(f"hasilnya adalah {fibonacci(n)}")


#SOAL NO 3
# def faktorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * faktorial(n-1)

# n = int(input("Masukkan bilangan untuk menghitung faktorial: "))
# print(f"{n}! = {faktorial(n)}")


#SOAL NO 4
# def cek_palindrom(kata):
#     kata = kata.lower()
#     return kata == kata[::-1]

# kata = input("masukkan kata yang ingin cek : ")
# print(f"Apakah '{kata}' adalah palindrom? {cek_palindrom(kata)}")
