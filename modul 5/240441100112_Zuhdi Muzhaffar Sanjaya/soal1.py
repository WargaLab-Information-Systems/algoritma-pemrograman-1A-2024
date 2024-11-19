def calculate_discount(total_belanja, keanggotaan):
    # Inisialisasi diskon
    diskon = 0
    
    # Menentukan diskon berdasarkan jenis keanggotaan
    if keanggotaan == 'Gold':
        diskon = 0.15
    elif keanggotaan == 'Silver':
        diskon = 0.10
    elif keanggotaan == 'Bronze':
        diskon = 0.05
    else:
        diskon = 0.0

    # Cek apakah total belanja lebih dari 1 juta untuk tambahan diskon
    if total_belanja > 1000000:
        diskon += 0.05  # Tambahan diskon 5%

    # Menghitung jumlah diskon
    total_diskon = total_belanja * diskon
    return total_diskon

# Contoh penggunaan
total_belanja = 2000000
keanggotaan = ''
diskon = calculate_discount(total_belanja, keanggotaan)
print(f"Total belanja: Rp{total_belanja}")
print(f"Diskon yang didapat: {diskon}")
print(f"Keanggotaan: {keanggotaan}")