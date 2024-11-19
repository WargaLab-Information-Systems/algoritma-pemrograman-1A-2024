def faktorial(n):
    
    if n == 0 or n == 1:
        return 1 #apabila mengimputkan nilai 0/1 akan muncul 1 karena memang hasilnya 1
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan bilangan: "))
print(f"hasil dari {n}! = {faktorial(n)}")