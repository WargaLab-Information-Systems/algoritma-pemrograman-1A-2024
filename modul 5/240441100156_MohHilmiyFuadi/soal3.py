def faktorial(n):
    # Basis kasus
    if n == 0:
        return 1
    else:
        # Rekursi untuk menghitung faktorial
        return n * faktorial(n - 1)


print("0! =", faktorial(0)) 
print("2! =", faktorial(2))  
print("3! =", faktorial(3))  
print("5! =", faktorial(5))  