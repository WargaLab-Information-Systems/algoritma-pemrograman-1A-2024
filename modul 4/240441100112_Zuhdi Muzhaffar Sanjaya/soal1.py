# Input dari pengguna
size = int(input("Masukkan ukuran sisi belah ketupat (size): "))
char = input("Masukkan karakter pilihan (x/o) : ")

# Menggambar bagian atas ketupat
for i in range(size):
    # Cetak spasi
    for j in range(size - i - 1):
        print(' ', end='')
    # Cetak karakter
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print(char, end='')
        else:
            print(' ', end='')
    print()  # Pindah ke baris berikutnya
for i in range( size- 2, -1, -1):
    # Cetak spasi
    for j in range(size - i - 1):
        print(' ', end='')
  
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print(char, end='')
        else:
            print(' ', end='')
print()