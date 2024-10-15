print("004")
a = int(input("masukan ukuran angka yang anda inginkan: "))


for i in range(1, a + 1, 1):
    if i == 1:
        print("x" * a)
    if i < a:
        print("x" + " " * (a - 2) + "x")
    if i == a:
        print("x" * a)
# untuk simbol angka 0
print()
#() untuk ngasih jeda antar print
for p in range(1, a + 1, 1):
    if p == 1:
        print("x" * a)
    if p < a:
        print("x" + " " * (a - 2) + "x")
    if p == a:
        print("x" * a)
# untuk simbol angka 0
print()

for o in range(1, a + 1, 1):
    if o <= a // 2:
        print("x" + " " * (a - 2) + "x")
    if o == a // 2:
        print("x" * a)
    if o >= a // 2:
        print(" " * (a - 1) + "x")
# untuk simbol angka 4