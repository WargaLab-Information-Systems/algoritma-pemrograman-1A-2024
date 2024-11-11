# soal nomer 2
n = int(input("Masukkan bilangan desimal: "))
konvers = n
biner = ""
# Mengonversi bilangan desimal ke biner
while n > 0:
    biner = str(n % 2) + biner
    n = n // 2
print("Hasil dari konversi bilangan desimal", konvers, "ke biner adalah", biner)
# pola segitiga
print("Pola segitiga:")
for i in range(1, len(biner) + 1):
    print(' ' * (len(biner) - i), end='')
    for j in range(i):
        print(biner[j], end=' ')
    print()  

