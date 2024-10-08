tahun = int(input("Masukkan tahun yang anda inginkan:"))
# % habis dibagi
if tahun %4 == 0 and tahun %400 == 0:
    print(f"Tahun {tahun} termasuk tahun kabisat")
elif tahun % 100 == 0:
    print(f"Tahun {tahun} bukan tahun kabisat")
else:
    print(f"{tahun} Bukan tahun kabisat")