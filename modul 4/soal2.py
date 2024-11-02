bilangan_desimal = int(input("masukkan bilangan desimal: "))

# variable hasil biner
biner = ''

# konversi dari desimal ke biner
while bilangan_desimal > 0:
    sisa = bilangan_desimal % 2
    biner = str(sisa) + biner
    bilangan_desimal //= 2

# menampilkan hasil biner
print("hasil konversi ke biner: ", biner)

# menampilkan pola segitiga
print("pola segitiga sama : ")
for i in range(1, len(biner) + 1):
    print(biner[:i]) #untuk mencetak i digit pertama dari biner