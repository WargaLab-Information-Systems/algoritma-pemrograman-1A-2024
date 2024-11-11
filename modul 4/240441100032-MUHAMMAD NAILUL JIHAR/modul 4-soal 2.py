desimal = int(input("Masukkan angka Desimal : "))
biner = ""

while desimal > 0:
    sisa = desimal % 2
    biner = str(sisa) + biner
    desimal = desimal // 2
    print(" ", biner) 
