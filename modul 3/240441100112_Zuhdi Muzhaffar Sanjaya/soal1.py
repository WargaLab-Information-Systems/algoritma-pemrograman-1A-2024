size = int(input("Masukkan Size: "))  # Mengatur ukuran

# Bagian untuk menggambar angka 1
for i in range(size):
    if i == 0:
        print(" " * (size - 1) + "x")  # Baris pertama dengan 'x' di atas
    else:
        print(" " * (size - 1) + "x")  # Semua baris setelahnya juga 'x'
print()

# Bagian untuk menggambar angka 1 (ulang)
for i in range(size):
    if i == 0:
        print(" " * (size - 1) + "x")  # Baris pertama dengan 'x' di atas
    else:
        print(" " * (size - 1) + "x")  # Semua baris setelahnya juga 'x'
print()

# Bagian untuk menggambar angka 2
for i in range(size):
    if i == 0:  # Baris pertama
        print("x" * size)  # Baris atas
    elif i == size // 2:  # Baris tengah
        print("x" * size)  # Baris tengah
    elif i < size // 2:  # Baris kedua dan ketiga (setengah atas)
        print(" " * (size - 1) + "x")  # Hanya di kanan
    elif i > size // 2:  # Baris keempat dan seterusnya (setengah bawah)
        if i == size - 1:  # Baris terakhir
            print("x" * size)  # Baris bawah
        else:
            print("x")  # Hanya satu "x" di kiri