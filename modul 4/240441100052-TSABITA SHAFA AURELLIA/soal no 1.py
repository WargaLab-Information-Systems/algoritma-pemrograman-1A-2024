
# menerima input dari pengguna
n = int(input("Masukkan ukuran sisi belah ketupat (n): "))
while True:
    karakter = input("Masukkan karakter (x / o): ")
    
    if karakter == "x" or karakter == "o":
        
        # atas belah ketupat
        for i in range(1, n + 1):
            print(' ' * (n - i), end='') #nyetak spasi
            print(karakter * (2 * i - 1)) #baris

        # bawah belah ketupat
        for j in range(n - 1, 0, -1):
            print(' ' * (n - j), end='')  
            print(karakter * (2 * j - 1))  
        break

    else:
        print("Input tidak valid! Silakan masukkan karakter (x / o)")