desimal = int(input("Masukkan desimal: "))
biner = ''

while desimal > 0:
    biner = str(desimal % 2) + biner
    desimal //= 2

print("Angka biner:", biner)
print()

n = 0
for a in biner:
    n += 1

for i in range(n + 1):
    for j in range(n - i):
        print('', end=' ')
    for k in range(i):
        print(biner[k], end=' ')
    print()