def print_0(size):
    for row in range(size):
        if row == 0 or row == size - 1:
            print("*" * size)  # cetak baris atas bawah
        else:
            print("*" + " " * (size - 2) + "*")  # cetak bagian tengah

def print_3(size):
    print("*" * size)  # cetak baris atas
    for _ in range(size // 2 - 1):
        print(" " * (size - 1) + "*")  # cetak sisi kanan atas 
    print("*" * size)  # cetak baris tengah
    for _ in range(size // 2 - 1):
        print(" " * (size - 1) + "*")  # cetak sisi kanan bagian bawah
    print("*" * size)  # cetak baris bawah

def print_6(size):
    for row in range(size):
        if row == 0 or row == size // 2 or row == size - 1:
            print("*" * size)  # cetak baris penuh
        elif row < size // 2:
            print("*")  # cetak bagian kiri atas
        else:
            print("*" + " " * (size - 2) + "*")  # cetak bagian bawah

def print_numbers(size):
    print_0(size)
    print_3(size)
    print_6(size)

# Input ukuran
size = int(input("Masukkan ukuran: "))
print_numbers(size)