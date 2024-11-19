#1 
def calculate_discount(total_belanja, keanggotaan):
    diskon_persen = 0
    
    
    if keanggotaan.lower() == "gold":
        diskon_persen = 15
    elif keanggotaan.lower() == "silver":
        diskon_persen = 10
    elif keanggotaan.lower() == "bronze":
        diskon_persen = 5
    elif keanggotaan.lower() == "none":
        diskon_persen = 0
    
    if total_belanja > 1000000:
        diskon_persen += 5 
    
    jumlah_diskon = total_belanja * (diskon_persen / 100)
    total_setelah_diskon = total_belanja - jumlah_diskon

    return total_setelah_diskon, jumlah_diskon

total_belanja = int(input("Masukkan total belanja: "))
keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze/None): ")

total_akhir, diskon = calculate_discount(total_belanja, keanggotaan)
print(f"Total setelah diskon: Rp {total_akhir}")
print(f"Jumlah diskon yang didapat: Rp {diskon}")

# 2
def fibonacci(n):
    if n == 0:
        return 0  
    elif n == 1:
        return 1  
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Masukkan bilangan bulat non-negatif n: "))
if n < 0:
    print("Silakan masukkan bilangan bulat non-negatif.")
else:
    hasil = fibonacci(n)
    print(f"Fibonacci ke-{n} adalah {hasil}.")

#3
def factorial(n):
    if n < 0:
        return "Faktorial tidak terdefinisi untuk bilangan negatif."
    
    if n == 0:
        return 1 
    
    hasil = 1
    langkah_str = ""  
    for i in range(n, 0, -1):
        hasil *= i  
        langkah_str += str(i)  
        if i > 1:
            langkah_str += " x "  

    print(f"{n}! = {langkah_str} = {hasil}")

n = int(input("Masukkan bilangan bulat non-negatif untuk menghitung faktorial: "))
    
if n >= 0:
    factorial(n)
else:
    print("Faktorial tidak terdefinisi untuk bilangan negatif.")

# 4
def cek_palindrom(kata):
    return kata == kata[::-1]

kata = input("Masukkan sebuah kata: ")

if cek_palindrom(kata):
    print(f" kata ({kata}) adalah palindrom.")
else:
    print(f"kata ({kata}) bukan palindrom.")

