while True:
    n = int(input("masukkan ukuran (n) yang anda mau untuk setengah tinggi ketupat : "))
    k = str(input("masukkan karakter yang anda mau (misal X atau O) : "))

    # Mencetak pola bagian atas ketupat
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for y in range(2 * i + 1):
            print(k, end=" ")
        print()

    # Mencetak pola bagian bawah ketupat
    for i in range(n - 1, -1, -1):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for y in range(2 * i + 1):
            print(k, end=" ")
        print()

    ulang = str(input("apakah anda ingin mengulang? [y/n] : "))
    if ulang == "y":
        continue
    elif ulang == "n":
        break
    else:
        print("inputan anda invalid")
        break