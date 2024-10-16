angka = input("Masukkan angka bulat: ")

angka_balik = ''
for i in angka:
    angka_balik = i + angka_balik

# hasil
print(f"Angka setelah dibalik: {angka_balik}")