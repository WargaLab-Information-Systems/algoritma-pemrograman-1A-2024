n=int(input("input angka: "))
def faktorial(n):
    if n>1:
        return n*faktorial(n-1)
    else:
        return 1
print(f"{n}!={faktorial(n)}")