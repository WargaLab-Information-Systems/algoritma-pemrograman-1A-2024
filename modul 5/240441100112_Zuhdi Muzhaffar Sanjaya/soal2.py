def fibonacci(n):
    # Kasus dasar
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Rekursi untuk menghitung bilangan Fibonacci
        return fibonacci(n - 1) + fibonacci(n - 2)

# Contoh penggunaan
n = 7
print(f"Bilangan Fibonacci ke-{n} adalah: {fibonacci(n)}")
