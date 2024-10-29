desimal = float(input("masukkan bilangan desimal : "))
biner = ""
while desimal > 0:
    desimal //= 2
    biner = str(desimal % 2) + biner

for i in range(len(biner)):
    for j in range(i + 1):
        print(biner[j], end = " ")
    print()
