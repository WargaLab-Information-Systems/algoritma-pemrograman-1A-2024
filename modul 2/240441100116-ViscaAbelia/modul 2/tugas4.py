#rumus tahun kabisat = angka tahun habis dibagi 400 dan
#angka tahun tidak habis dibagi 400 dan tidak habis dibagi 100 tetapi habis dibagi 4

angka_tahun = int(input("Masukkan angka tahun : "))

if angka_tahun % 400 == 0:
    print(f"tahun {angka_tahun} adalah tahun kabisat")
elif(angka_tahun % 400 != 0 and angka_tahun % 100 != 0 and angka_tahun % 4 == 0):
    print(f"tahun {angka_tahun} adalah tahun kabisat")
else:
    print(f"tahun {angka_tahun} bukan tahun kabisat")