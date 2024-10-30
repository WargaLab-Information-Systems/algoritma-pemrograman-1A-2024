# Menerima input bilangan desimal dari pengguna
desimal = int(input("Masukkan bilangan desimal: "))

# Konversi desimal ke biner (tanpa fungsi bin())
biner = ''
n = desimal
while n > 0:
    biner = str(n % 2) + biner
    n = n // 2

# Menampilkan pola segitiga dari bilangan biner
for i in range(1, len(biner) + 1):
    print(biner[:i])