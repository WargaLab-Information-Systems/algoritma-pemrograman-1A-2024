desimal = int(input("masukkan angka desimal: "))
biner = " "
while desimal > 0:
    sisa = desimal % 2
    biner = str(sisa) + " " + biner 
    desimal = desimal // 2
print(f"bilangan binernya adalah: {biner}")