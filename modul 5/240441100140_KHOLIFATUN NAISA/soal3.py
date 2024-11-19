def faktorial (a):
    if a <= 1:
        return 1
    else:
        hasil = a * faktorial (a - 1)
        return hasil
angka = int (input("masukkan angka faktorial: "))
print(f"hasil faktorial dari {angka} adalah {faktorial(angka)}")