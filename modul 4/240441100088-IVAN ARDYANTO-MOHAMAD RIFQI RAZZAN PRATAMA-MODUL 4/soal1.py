ukuran_sisi = int(input("masukan ukuran karakter sisi: "))
karakter = input("masukan karakter checkerboard (x dan o): ")

if karakter.lower() == "x":
    for i in range(ukuran_sisi):
        print(" " * (ukuran_sisi - i), end="")

        for j in range( i + 1):
            print(karakter, end=" ")

        print(" " * (ukuran_sisi - i), end=" ")
        print()

    for i in range(ukuran_sisi - 1, 0, -1):
        print(" " * (ukuran_sisi - (i - 1)),end="")

        for j in range(i):
            print(karakter , end=" ")

        print(" " * (ukuran_sisi - (i - 1)), end="")
        print()

elif karakter.lower() == "o":
    for i in range(ukuran_sisi):
        print(" " * (ukuran_sisi - i), end="")

        for j in range( i + 1):
            print(karakter, end=" ")

        print(" " * (ukuran_sisi - i), end=" ")
        print()

    for i in range(ukuran_sisi - 1, 0, -1):
        print(" " * (ukuran_sisi - (i - 1)),end="")

        for j in range(i):
            print(karakter , end=" ")

        print(" " * (ukuran_sisi - (i - 1)), end="")
        print()
else:
    print("maaf huruf harus (x dan o)")