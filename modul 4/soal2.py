desimal = int(input("Masukkan bilangan desimal: "))

biner = ''
n = desimal
while n > 0:
    biner = str(n % 2) + biner
    n = n // 2

for i in range(1, len(biner) + 1):
    print(biner[:i])