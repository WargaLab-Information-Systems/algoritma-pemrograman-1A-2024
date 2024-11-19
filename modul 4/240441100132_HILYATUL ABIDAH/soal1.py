n = int(input("Masukkan ukuran sisi belah ketupat: ")) #sisi tengah belah ketupat
char1 = input("Masukkan karakter (X or O)): ") #berisi karakter yang akan diisikan dalam bentuk belah ketupat


for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ") 
    for j in range(2 * i + 1): #2 * i + 1, yang berarti jumlah karakter akan bertambah seiring barisnya meningkat.
        print(char1, end = " ")
    print()

for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")  
    for j in range(2 * i + 1):
        print(char1, end = " ")
    print()  