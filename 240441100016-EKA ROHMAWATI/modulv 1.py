#input angka
n = int(input("Masukkan ukuran: "))
k = input("Masukkan karakter(X atau O): ")

#membuat perulangan 
if k == "O":
    for i in range(n): 
        for j in range(n - i - 1): 
            print(" ", end="")
        for y in range(i + 1): 
            print("O", end=" ") 
        print()
    for i in range(n - 1): 
        for j in range(i + 1): 
            print(" ", end="") 
        for y in range(n - i - 1): 
            print("O", end=" ")
        print()
elif k == "X":
    for i in range(n): 
        for j in range(n - i - 1): 
            print(" ", end="")
        for y in range(i + 1): 
            print("X", end=" ") 
        print()
    for i in range(n - 1): 
        for j in range(i + 1): 
            print(" ", end="") 
        for y in range(n - i - 1): 
            print("X", end=" ")
        print()
else:
    print("bukan termasuk  karakter")