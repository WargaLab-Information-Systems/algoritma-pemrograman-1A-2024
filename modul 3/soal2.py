# angka = int(input("Masukkan angka: "))
# angka_terbalik = str(angka) [::-1]
# print("Angka setelah dibalik:", angka_terbalik)

# while True:
#     angka = int(input("Masukkan angka: "))
    
#     if angka :
#         break
# angka_terbalik = str(angka)[::-1]
# print(f"Angka setelah dibalik: {angka_terbalik}")

angka = input("Masukkan angka bulat: ")

angka_balik = ''
for digit in angka:
    angka_balik = digit + angka_balik

# hasil
print(f"Angka setelah dibalik: {angka_balik}")