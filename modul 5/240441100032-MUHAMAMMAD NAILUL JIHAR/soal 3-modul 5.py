def fa(n):
    if n < 0:
        return "Angka harus positif"
    elif n == 0 or n == 1:
        return 1
    else:
        hasil = 1
        for i in range(2, n + 1):
            hasil *= i
        return hasil

print(f"Hasil dari perhitungan bilangan faktorial 5! = 5 x 4 x 3 x 2 x 1 = {fa(5)}")
print(f"Hasil dari perhitungan bilangan faktorial 3! = 3 x 2 x 1 = {fa(3)}")
print(f"Hasil dari perhitungan bilangan faktorial 2! = 2 x 1 = {fa(2)}")
print(f"Hasil dari perhitungan bilangan faktorial 0! = 1 {fa(0)}")