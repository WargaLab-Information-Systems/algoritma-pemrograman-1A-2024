def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("masukkan angka:"))
hasil = faktorial(n)
print(f"{n}! = {hasil}")
