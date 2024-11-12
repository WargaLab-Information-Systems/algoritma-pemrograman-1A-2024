blok_code = {
    "0" : [
        " xxxxx  ",
        "x     x ",
        "x     x ",
        "x     x ",
        " xxxxx  "
    ],
    "1" : [
        "   xx   ",
        " x  x   ",
        "    x   ",
        "    x   ",
        "  xxxxx "
    ],
    "2" : [
        "xxxxx   ",
        "     x  ",
        " xxxx   ",
        "x       ",
        "xxxxxx  "
    ],
    "3" : [
        " xxxx   ",
        "     x  ",
        " xxxx   ",
        "     x  ",
        " xxxx   "
    ],
    "4" : [
        "x    x  ",
        "x    x  ",
        " xxxxx  ",
        "     x  ",
        "     x  "
    ],
    "5" : [
        " xxxx   ",
        "x       ",
        " xxxx   ",
        "     x  ",
        " xxxx   "
    ],
    "6" : [
        " xxxx   ",
        "x       ",
        " xxxx   ",
        "x    x  ",
        " xxxx   "
    ],
    "7" : [
        " xxxx   ",
        "     x  ",
        "    x   ",
        "   x    ",
        "  x     "
    ],
    "8" : [
        " xxxx   ",
        "x    x  ",
        " xxxx   ",
        "x    x  ",
        " xxxx   "
    ],
    "9" : [
        " xxxx   ",
        "x    x  ",
        " xxxx   ",
        "     x  ",
        " xxxx   "
    ]
}

ulang = "ya" 

while ulang == "ya":
    nim_terakhir = input("Masukkan NIM terakhir (misal NIM 001, 004, 120, dll) : ")
    print(" ")
    
    
    ada_minus = False
    digit_hitung = 0
    hanya_angka = True

    for x in nim_terakhir:
        digit_hitung += 1
        if x == '-':
            ada_minus = True
        if x < '0' or x > '9':
            hanya_angka = False

    if ada_minus:
        print("Maaf, nilai yang Anda masukkan tidak valid. Tidak boleh ada karakter minus (-).\n")
    elif digit_hitung > 3:
        print("Maaf, nilai yang Anda masukkan melebihi tiga digit.\n")
    elif hanya_angka == False:
        print("Maaf, nilai yang Anda masukkan tidak valid. Harap masukkan hanya angka.\n")
    else:
        for i in range(5):
            for digit in nim_terakhir:
                print(blok_code[digit][i], end="  ")
            print()

    print(" ")
    ulang = input("Apakah Anda ingin memasukkan NIM yang berbeda? (ya/tidak): ")

print("Program selesai.")