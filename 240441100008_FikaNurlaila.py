angka = int (input("masukkan beberapa angka:"))
def ganjil_genap (angka):
    if angka % 2 :
        print (f"angka genap ada ",angka,"huruf")
    else:
        print (f"angka ganjil ada", angka,"huruf")

    angka = ganjil_genap (angka-1)
    return angka % 2
ganjil_genap(angka)
