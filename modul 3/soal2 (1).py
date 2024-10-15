# masukkan angka
angka_input = input("masukkan angka bulat: ")

# variable kosong untuk menyimpan angka yang dibalik
angka_balik = ""

# loop
for digit in angka_input:
    angka_balik = digit + angka_balik

# menampilkan hasil
print("angka setelah dibalik:", angka_balik)