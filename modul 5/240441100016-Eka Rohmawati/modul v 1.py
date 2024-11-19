#input data
def calculate_discount(total_belanja, anggota):
    diskon = 0  
    if total_belanja > 1000000:
        diskon += 5
        
    if anggota == 'gold':
        diskon += 15
    elif anggota == 'silver':
        diskon += 10
    elif anggota == 'bronze':
        diskon += 5
    else:
        print("tidak memiliki member")

    # Menghitung total diskon
    total_diskon = (diskon / 100) * total_belanja
    total_setelah_diskon = total_belanja - total_diskon

    return diskon, total_diskon, total_setelah_diskon

#input mengulang
while True:
#input data
    total_belanja = int(input("Masukkan total harga belanja: "))
    anggota = input("Apa member Anda(gold/silver/bronze/no): ").lower()

    # Menghitung diskon
    diskon, total_diskon, total_setelah_diskon = calculate_discount(total_belanja, anggota)

    # Menampilkan hasil
    print("Total belanja:", total_belanja)
    print(f"Diskon yang didapatkan: {diskon}%")
    print("Total setelah diskon:", total_setelah_diskon)

    #input jika ingin mengulang
    ulang = input("apakah ingin menghitung ulang kembali?(ya,no): ")
    if ulang != 'ya':
        print("terimakasi")
        break