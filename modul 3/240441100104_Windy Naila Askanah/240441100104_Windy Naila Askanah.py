# nomor 1

size = int(input("masukkan size yang anda inginkan :"))

for i in range (size):
        print("*")

print()

for i in range (size):
    if i == 0 or i == size -1:
        print("******")
    else:
        print("*    *")

print()

for i in range(size):
    if i == size - 3:
        print("******")
    elif i == size-2 or i == size-1:
        print("     *")
    else:
        print("*    *")

# nomor 2

angka = input("Masukkan bilangan bulat yang anda inginkan : ")
angka_terbalik = ""
for i in angka:
    angka_terbalik += i  

angka_terbalik = angka_terbalik [::-1]

print("Bilangan bulat yang anda inginkan setelah dibalik : ", angka_terbalik)


# nomor 3

while True:
    lama_sewa_input = input("Masukkan lama sewa DVD yang akan anda pinjam dalam hari : ")
    if lama_sewa_input: 
        lama_sewa = int(lama_sewa_input)
        if lama_sewa == 0:
            print("Lama sewa harus lebih dari 0 hari!")
            continue
    else:
        print("Masukkan nilai dengan benar!")
        continue

    hari_keterlambatan= lama_sewa - 5
    denda_harian = 2500
    denda_tambahan = 5500
    total_denda = 0
    
    if hari_keterlambatan > 0:
        total_denda += hari_keterlambatan * denda_harian
        if hari_keterlambatan > 10:
            denda_5_hari = (hari_keterlambatan - 10) // 5
            total_denda += denda_5_hari * denda_tambahan
            
    print(f"Total denda keterlambatan: Rp {total_denda}")

    ulang = input("Apakah Anda ingin menghitung kembali? (yeah/not): ")
    if ulang != 'yeah':
        break