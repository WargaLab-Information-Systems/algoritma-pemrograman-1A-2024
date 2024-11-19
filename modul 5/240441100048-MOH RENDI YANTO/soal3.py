def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

n = int(input("Masukkan bilangan untuk menghitung faktorial: "))
print(f"{n}! = {faktorial(n)}")