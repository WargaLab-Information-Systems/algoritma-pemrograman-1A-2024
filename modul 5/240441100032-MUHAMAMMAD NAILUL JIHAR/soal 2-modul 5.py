def fibonacci(n):
    if n == 0:
        return [n]
    
    angka = fibonacci(n-1)
    indeks = len(angka)

    angka1 = angka[-2] if indeks > 2 else 0
    angka2 = angka[-1] if indeks > 2 else 1
    
    return angka + [angka1 + angka2]

angka = int(input("Masukkan angka : "))
print("Fibonacci ke-", angka, "adalah", fibonacci(angka))   