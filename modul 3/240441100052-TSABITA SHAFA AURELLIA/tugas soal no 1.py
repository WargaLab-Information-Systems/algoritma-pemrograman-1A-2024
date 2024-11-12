# soal 1
# Input ukuran pola dari pengguna
size = int(input("Masukkan ukuran pola angka: "))

# Pola untuk angka 0
print("")
for i in range(size):
    if i == 0 or i == size - 1:
        print("x" * size)
    else:
        print("x" + " " * (size - 2) + "x")

# Pola untuk angka 5
print("")
for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print("x" * size)
    elif i < size // 2:
        print("x")
    else:
        print(" " * (size - 1) + "x")

# Pola untuk angka 2
print("")
for i in range(size):
    if i == 0 or i == size - 1 or i == size // 2:
        print("x" * size)
    elif i < size // 2:
        print(" " * (size - 1) + "x")
    else:
        print("x")

