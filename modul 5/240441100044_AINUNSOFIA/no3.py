def faktorial(n):
    if n == 0:
        return 1
    else:
        hasil= n * faktorial(n - 1)
    return hasil

n = int (input('masukkan angka yang ingin dihitung: '))
print("hasil dari ", n," faktorial adalah ", faktorial(n))

for i in range(n,0,-1):
    print(i, end='x') if i > 1 else  print(i, '=',faktorial(n))