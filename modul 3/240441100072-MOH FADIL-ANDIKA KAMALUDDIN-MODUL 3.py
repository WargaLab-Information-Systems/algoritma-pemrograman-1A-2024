#SOAL NO 1
# Input ukuran pola
size = int(input("Masukan Size : "))
# Pola angka 0
#print("Pola angka 0:")
for i in range(size):
    for j in range(size):
        if i == 0 or i == size-1 or j == 0 or j == size-1:
            print("x", end="")
        else:
            print(" ", end="")
    print()
print()
# Pola angka 7
#print("Pola angka 7:")
for i in range(size):
    for j in range(size):
        if i == 0 or j == size-1-i:
            print("h", end="")
        else:
            print(" ", end="")
    print()
print()
# Pola angka 2
#print("Pola angka 2:")
for i in range(size):
    for j in range(size):
        if i == 0 or i == size-1 or i == size//2 or (j == size-1 and i < size//2) or (j == 0 and i > size//2):
            print("x", end="")
        else:
            print(" ", end="")
    print()


#SOAL NO 2
print("Program Pembalikan Angka Bulat")

while True:
    num = int(input("Masukkan sebuah angka bulat: "))

    num_balik = 0
    num_asli = num

    while num > 0:
        digit = num % 10
        num_balik = num_balik * 10 + digit
        num //= 10

    print(f"Balikan dari {num_asli} adalah {num_balik}.")

    respons = input("Apakah Anda ingin membalikkan angka bulat lainnya? (ya/tidak): ")
    if respons.lower() != "ya":
        break


#SOAL NO 3
print("Kalkulator Denda Keterlambatan Penyewaan DVD")
while True:
    lama_sewa = int(input("Masukkan jumlah hari DVD disewa: "))
    lama_kembali = int(input("Masukkan jumlah hari DVD dikembalikan: "))
    if lama_kembali <= 5:
        denda = 0
    else:
        hari_keterlambatan = lama_kembali - 5
        denda = hari_keterlambatan * 2500
        if hari_keterlambatan > 10:
            denda_tambahan = (hari_keterlambatan - 10) // 5 * 5500
            denda += denda_tambahan

    print(f"Total denda: Rp.{denda:,}")

    respons = input("Apakah Anda ingin menghitung kembali? (ya/tidak): ")
    if respons.lower() != "ya":
        break