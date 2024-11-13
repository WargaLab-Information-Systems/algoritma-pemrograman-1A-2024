print("Pilih jenis keanggotaan:")
print("1. Gold")
print("2. Silver")
print("3. Bronze")
print("4. Tidak ada keanggotaan")

pilihan_keanggotaan = int(input("Masukkan pilihan keanggotaan (1-4): "))
total_belanja = float(input("Masukkan total belanja: "))

def calculate_discount(total_belanja, pilihan_keanggotaan):
    # Tentukan diskon berdasarkan pilihan keanggotaan
    if pilihan_keanggotaan == 1:
        diskon_keanggotaan = 0.15  
    elif pilihan_keanggotaan == 2:
        diskon_keanggotaan = 0.10  
    elif pilihan_keanggotaan == 3:
        diskon_keanggotaan = 0.05  
    else:
        diskon_keanggotaan = 0.0  

    # Hitung diskon awal berdasarkan keanggotaan
    diskon_awal = total_belanja * diskon_keanggotaan
    
    # Cek apakah belanja lebih dari 1 juta untuk diskon tambahan
    diskon_tambahan = total_belanja * 0.05 if total_belanja > 1000000 else 0.0

    # Total diskon adalah diskon awal + diskon tambahan
    total_diskon = diskon_awal + diskon_tambahan

    # Hitung total setelah diskon
    total_setelah_diskon = total_belanja - total_diskon
    
    return total_diskon, total_setelah_diskon

# Menghitung diskon
diskon, total_setelah_diskon = calculate_discount(total_belanja, pilihan_keanggotaan)

# Menampilkan hasil
print(f"Total Diskon: {diskon}")
print(f"Total Setelah Diskon: {total_setelah_diskon}")