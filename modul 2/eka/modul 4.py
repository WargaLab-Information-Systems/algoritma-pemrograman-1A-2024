#rumus tahun kabisat:
#jika angka "Tahun" yang habis dibagi 4 dan tidak habis dibagi 100 atau habis dibagi 400
#input tahun
tahun = int(input("masukkan tahun: "))

#menentukan tahun
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")