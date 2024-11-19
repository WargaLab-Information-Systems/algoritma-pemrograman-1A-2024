#soal No 1
# total_belanja = int(input("Masukkan total belanja Anda: "))
# member_ship = input("Apakah Anda mempunyai keanggotaan? silver/bronze/gold/tidak: ")

# def calculate_diskon(total_belanja, member_ship):
#     diskon = 0
#     if total_belanja > 1000000:
#         diskon += 5
#     if member_ship == "gold":
#         diskon += 15
#     elif member_ship == "silver":
#         diskon += 10
#     elif member_ship == "bronze":
#         diskon = 5
#     else:
#         diskon += 0
    
#     total_diskon = total_belanja * (diskon / 100)
#     total_setelah_diskon = total_belanja - total_diskon
#     print(f"Total diskon: {total_diskon}")
#     print(f"Total yang harus dibayar: {total_setelah_diskon}")

# calculate_diskon(total_belanja, member_ship)


# # # #soal no 2
# n = int(input("masukkan angka yang ingin dihitung : "))
# def fibonacci(n):
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#         fn=fibonacci(n-1)+ fibonacci(n-2)
#         return fn
# print(fibonacci(n))

# a,b = 0,1
# for i in range (n):
#     a,b =b, a+b 
#     print(a, end="")





#  soal no 3
# n = int(input("Masukkan bilangan: "))
# def faktorial(x):
#     hasil = 1
#     deret = ""
#     for i in range(x, 0, -1):  
#         hasil *= i
#         deret += str(i) + " × " if i > 1 else str(i) 
#     return deret + f" = {hasil}"  

# print(f"{n}! = {faktorial(n)}")
    

# soal no 4
def cek_palindrom(kata):
    if kata == kata[::-1]:
        print(kata[::-1])
        return 'true,merupakan palindrom'
    else:
        print(kata[::-1])
        return 'false,bukan palindrom'
while True:    
    kata = str(input("masukkan kata yang akan anda cek: "))
    if kata.isalpha():
        print(cek_palindrom(kata))
        break
    else:
        print('masukan huruf')
        