desimal = int(input("masukkan bilangan desimal anda : "))

# mengkonversi
bil_biner = ""
while desimal > 0:
    sisa = desimal % 2
    bil_biner = str(sisa) + bil_biner
    desimal = desimal // 2

print(f"bilangan biner : {bil_biner}")

# Membuat pola segitiga
for i in range(len(bil_biner)):
    print(bil_biner[:i + 1])