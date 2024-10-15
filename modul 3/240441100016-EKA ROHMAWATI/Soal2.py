#input angka
angka = input("masukkan angka bulat: ")
angka_balik=""
for digit in angka:
    angka_balik = digit + angka_balik

#menampilkan hasil
print("angka setelah dibalik: ",angka_balik)