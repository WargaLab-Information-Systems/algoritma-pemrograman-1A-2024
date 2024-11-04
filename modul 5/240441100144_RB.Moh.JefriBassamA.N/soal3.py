print("---Selamat Datang di Perhitungan Faktorial---")
# n = int(input("masukkan angka yang mau anda hitung: "))
# def faktorial(n):
#     if n == 0:
#         return 1
#     elif n > 0:
#         return n*faktorial(n - 1)

# print(f"{n}! = {faktorial(n)}")



n = int(input("masukkan angka yang mau anda hitung: "))

def faktorial(n):
    faktor = 1
    if n == 0:
        return 1
    elif n > 0:
        for i in range (1, n + 1):
            faktor = faktor * i
        return faktor
print(f"{n}! = {faktorial(n)}")