n = int(input("Masukkan ukuran sisi n: "))
bentuk = (input("Pilih bentuk (o/x): "))

if bentuk == "x":
    for i in range(n):
        for j in range(n, i, -1):
            print(" ", end = "")
        for j in range(2 * i + 1):
            print("x", end = "")
        print()

    for i in range(n, - 1, - 1,):
        for j in range(n, i, -1):
             print(" ", end = "")
        for j in range(2 * i + 1):
            print("x", end = "")
        print()
elif bentuk == "o":
    for i in range(n):
        for j in range(n, i, -1):
            print(" ", end = "")
        for j in range(2 * i + 1):
            print("o", end = "")
        print()

    for i in range(n, - 1, - 1,):
        for j in range(n, i, -1):
             print(" ", end = "")
        for j in range(2 * i + 1):
            print("o", end = "")
        print()
else:
    print("Bentuk yang anda pilih tidak sesuai")