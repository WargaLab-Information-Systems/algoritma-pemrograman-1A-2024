angka = int(input("Masukkan angka bulat: "))

angka_terbalik = 0
print(angka)
while angka != 0:
    digit = angka % 10 
    angka_terbalik = angka_terbalik * 10 + digit  
    angka = angka // 10 
    print("angka",angka)

    print("digit",digit)

print("Angka terbalik:", angka_terbalik)

