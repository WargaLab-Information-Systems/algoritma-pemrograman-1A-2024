# soal nomer 1
def calculate_discount(total_belanja, jenis_keanggotaan):
    diskon = 0
    if total_belanja > 1000000:
        diskon += 5
    if jenis_keanggotaan.lower() == "gold":
        diskon = 15
    elif jenis_keanggotaan.lower() == "silver":
        diskon = 10
    elif jenis_keanggotaan.lower() == "bronze":
        diskon = 5

    jumlah_diskon = total_belanja *(diskon/100)
    total_setelah_diskon = total_belanja - jumlah_diskon

    return jumlah_diskon, total_setelah_diskon

jenis_keanggotaan = str(input("punya kartu anggota? (punya/tidak)"))
if jenis_keanggotaan == "punya":
    jenis_keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze): ")
    total_belanja = int(input("Masukkan total belanja: "))
    calculate_discount(total_belanja, jenis_keanggotaan)

elif jenis_keanggotaan == "tidak":
    jenis_keanggotaan == "tidak"
    total_belanja = int(input("Masukkan total belanja: "))
    calculate_discount(total_belanja, jenis_keanggotaan)

jumlah_diskon, total_setelah_diskon = calculate_discount(total_belanja, jenis_keanggotaan) 

print(f"Jumlah diskon: Rp {jumlah_diskon:}")
print(f"Total yang harus dibayar: Rp {total_setelah_diskon:}")

# soal nomer 2 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci (n-1) + fibonacci(n-2)
n = int(input("masukkan angka yang ingin di hitung : "))
print(f"hasilnya adalah {fibonacci(n)}")

def fibonacci(angka):
    "fungsi fibonacci"
    pertama = 0
    print(pertama, end=" ")
    kedua = 1
    print(kedua, end=" ")
    
    i = 3
    while i <= angka + 1:
        selanjutnya = pertama + kedua
        print(selanjutnya, end=" ")
        pertama = kedua
        kedua = selanjutnya
        i = i + 1
angka = int(input("kalo mw tw caranya : "))
fibonacci(angka)
print()

# soal nomer 3
def faktorial(angka):
    "fungsi faktorial"
    faktorial = 1
    for i in range (1, angka + 1):
        faktorial *= i
    return faktorial

angka = int(input("masukkan angka: "))

print(f"{angka}! =", end=" ")
for i in range (angka, 0, -1):
    print(i, end= " x " if i > 1 else " = ")
print(faktorial(angka))


# soal nomer 4
def palindrom(kata):
    kata = kata.replace(" ", "")  
    return kata == kata[::-1]  

while True:
    input_kata = input("Masukkan kata untuk memeriksa apakah itu palindrom: ")
    
    if input_kata.isdigit():
        print("Input tidak valid. Silakan masukkan kata, bukan angka.")
    elif isinstance(input_kata, str):  
        if palindrom(input_kata):
            print(f"'{input_kata}' adalah palindrom.")
        else:
            print(f"'{input_kata}' bukan palindrom.")
        break
    else:
        print("Input tidak valid. Silakan masukkan kata.")