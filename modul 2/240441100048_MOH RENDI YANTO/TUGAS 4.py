tahun = int(input("masukkan tahun: "))

# perintah if bersarang
if tahun % 400 == 0:
    print(f"Tahun {tahun} adalah Tahun kabisat")
else:
    if tahun % 100 == 0:
        print(f"Tahun {tahun} bukan Tahun kabisat")
    else:
        if tahun % 4 == 0:
            print(f"Tahun {tahun} adalah Tahun kabisat")
        else:
            print(f"Tahun {tahun} bukan  Tahun kabisat")
            