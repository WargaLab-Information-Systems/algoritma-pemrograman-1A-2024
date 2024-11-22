# Variabel global untuk menyimpan hasil diskon
total_diskon = 0
total_setelah_diskon = 0

def calculate_discount(total_belanja, keanggotaan):
    global total_diskon, total_setelah_diskon  # Menggunakan variabel global

    # Menentukan diskon berdasarkan jenis keanggotaan
    if keanggotaan == "gold":
        diskon = 15  # Diskon dalam persen
    elif keanggotaan == "silver":
        diskon = 10
    elif keanggotaan == "bronze":
        diskon = 5
    else:
        diskon = 0

    # Tambahan diskon jika total belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 5

    # Hitung total diskon dan total setelah diskon
    total_diskon = total_belanja * diskon / 100
    total_setelah_diskon = total_belanja - total_diskon

# Input
total_belanja_input = input("Masukkan total belanja (dalam rupiah): ")
keanggotaan = input("Masukkan jenis keanggotaan (gold/silver/bronze/none): ")

# Validasi input total belanja 
if total_belanja_input.isdigit():  # Pastikan input hanya angka
    total_belanja = int(total_belanja_input)

    # Menghitung diskon
    calculate_discount(total_belanja, keanggotaan)

    # Hasil
    print("Total diskon:", int(total_diskon))
    print("Total setelah diskon:", int(total_setelah_diskon))
else:
    print("Input tidak valid.")
