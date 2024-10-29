#mengkonversi angka desimal ke biner
angkadesimal = int(input("masukkan angka desimal: "))
biner = ""
while angkadesimal > 0:
    sisa = angkadesimal % 2
    biner = str (sisa) + biner
    print(biner)
    angkadesimal = angkadesimal // 2
print()
print("binernya adalah",biner)