angka = float(input("masukkan angka untuk dikonversi ke biner: "))
biner = ""

#konversi angka ke biner
while angka > 0:
    angka //= 2
    biner = str(angka % 2) + biner

wadah_biner = ""
iterasi = 0
print("hasil", biner)

#output biner segitiga 
for i in biner:
    wadah_biner += i


    print(" " * (len(biner) - iterasi - 1), end="")


    for j in wadah_biner:
        print(j, end=" ")

    print()
    iterasi += 1