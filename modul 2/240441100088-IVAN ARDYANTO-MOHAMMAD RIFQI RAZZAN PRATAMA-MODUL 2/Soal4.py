tahun = int(input("Masukkan tahun: "))

"""
    Rumus tahun kabisat:
    Jika "tahun" tidak habis dibagi angka 100 atau angka 400,
    tetapi habis dibagi dengan angka 4 maka tahun tersebut adalah
    tahun kabisat.
"""


if (tahun % 100 != 0 or tahun % 400 != 0) and tahun % 4 == 0:
    print(f"Tahun {tahun} adalah tahun kabisat")
else:
    print(f"Tahun {tahun} bukanlah tahun kabisat")