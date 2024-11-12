desimal = float(input("Masukkan bilangan desimal: "))
biner = ""

while desimal > 0: 
    desimal //= 2
    biner = str(desimal % 2) + biner

print(f"Hasil konversi dari bilangan biner: ", biner)

print("Bentuk pola segitiga: ")
for i in range(len(biner)):
    for j in range(i +1):
        print(biner[j], end = " ")
    print()