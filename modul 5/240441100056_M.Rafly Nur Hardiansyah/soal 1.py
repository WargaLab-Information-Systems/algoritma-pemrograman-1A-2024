def calculate_discount(member, total_belanja):
    total_diskon = 0
    total_belanja = 1000000
    
    # Menghitung diskon berdasarkan membership
    if member == "Gold":
        total_diskon += 0.15
    elif member == "Silver":
        total_diskon += 0.10 
    elif member == "Bronze":
        total_diskon += 0.05   

    # Menambahkan diskon tambahan jika total belanja > 1 juta
    if total_belanja > 1000000:
        total_diskon += 0.05  

    # Menghitung total yang harus dibayar
    nominal_diskon = int((total_diskon / 100) * total_belanja)
    return nominal_diskon

# Contoh penggunaan
print(f"Total diskon: Rp {calculate_discount('Gold', 500000)}") 
print(f"Total diskon: Rp {calculate_discount('Silver', 1500000)}")  
print(f"Total diskon: Rp {calculate_discount('Bronze', 750000)}") 
print(f"Total diskon: Rp {calculate_discount('', 2000000)}")
print(f"Total diskon: Rp {calculate_discount('', 20000)}")
