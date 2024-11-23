def faktorial(n): 
    if n < 0:
        return "Faktorial tidak didefinisikan untuk bilangan negatif"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1) #n - 1 digunakan untuk menghitung faktorial secara bertahap dari n hingga kondisi dasar, di mana hasil bisa dihitung mundur dan dikembalikan.

n=int(input("masukkan nilai n:"))
print(f"{n}! = {faktorial(n)}")