def calculate_discount(total_belanja, jenis_keanggotaan): 
    diskon = 0

    if jenis_keanggotaan == "gold" and total_belanja > 1000000:
        diskon += 20
    elif jenis_keanggotaan == "gold"  and total_belanja < 1000000:
        diskon += 15
    elif jenis_keanggotaan == "silver" and total_belanja > 1000000: 
        diskon += 15
    elif jenis_keanggotaan == "silver" and total_belanja < 1000000:
        diskon += 10
    elif jenis_keanggotaan == "bronze" and total_belanja > 1000000: 
        diskon += 10
    elif jenis_keanggotaan == "bronze" and total_belanja < 1000000:
        diskon += 5
    elif jenis_keanggotaan == "tidak" and total_belanja > 1000000: 
        diskon += 5
    elif jenis_keanggotaan == "tidak" and total_belanja < 1000000:
        diskon += 0

    jumlah_diskon = total_belanja *(diskon/100) 
    total_setelah_diskon = total_belanja - jumlah_diskon

    return jumlah_diskon, total_setelah_diskon

jenis_keanggotaan = str(input("punya kartu anggota? (ya/tidak): ")) 
if jenis_keanggotaan == "ya": 
    jenis_keanggotaan = input("Masukkan jenis keanggotaan (Gold/Silver/Bronze): ") 
    total_belanja = int(input("Masukkan total belanja: ")) 
    calculate_discount(total_belanja, jenis_keanggotaan) 
elif jenis_keanggotaan == "tidak": 
    total_belanja = int(input("Masukkan total belanja: ")) 
    calculate_discount(total_belanja, jenis_keanggotaan)

jumlah_diskon, total_setelah_diskon = calculate_discount(total_belanja, 
jenis_keanggotaan) 

print(f"Jumlah diskon: Rp {jumlah_diskon:}") 
print(f"Total yang harus dibayar: Rp {total_setelah_diskon:}") 