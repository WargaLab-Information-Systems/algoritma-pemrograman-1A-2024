n = int(input("masukkan angka : "))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Bilangan Fibonacci dari {n} adalah {fibonacci(n)}")

