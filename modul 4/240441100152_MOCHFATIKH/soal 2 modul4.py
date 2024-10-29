angka = int(input("masukkan angka desimal:"))
biner = ''

while angka > 0:
    sisa = angka % 2
    angka //= 2
    biner = str(sisa) + biner

print('')
print(f"Konversi dari bilangan binernya adalah {biner}")
print("untuk bentuk segitiganya adalah")
print('')

for i in range(1,len(biner)+1):
   print(biner[:i])
