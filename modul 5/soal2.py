def fibonacci(n):
    # Basis kasus
    if n == 0:
        return 0  # Mencetak hasil untuk n = 0
    elif n == 1:
        return 1  # Mencetak hasil untuk n = 1
    else:
        # Rekursi untuk menghitung bilangan Fibonacci
        return fibonacci(n - 1) + fibonacci(n - 2)  # Kembali hasil tanpa mencetak di sini

# Input dari pengguna
n = int(input("Masukkan bilangan bulat non-negatif n: "))

# Validasi input
if n < 0:
    print("Silakan masukkan bilangan bulat non-negatif.")
else:
    # Menghitung dan mencetak hasil
    hasil = fibonacci(n)
    print(f"Bilangan Fibonacci ke-{n} adalah: {hasil}")
