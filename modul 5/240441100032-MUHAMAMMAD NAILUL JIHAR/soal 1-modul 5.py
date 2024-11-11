def calculate_discount(total_belanja, keanggotaan):
    diskon = 0

    if tanya == "ya":
        if keanggotaan == "gold":
            diskon += 15
        elif keanggotaan == "silver":
            diskon += 10
        elif keanggotaan == "bronze":
            diskon += 5
        if total_belanja > 1000000:
            diskon += 5

    if tanya == "tidak":
        if keanggotaan == "none":
            diskon += 0
        if total_belanja > 1000000:
            diskon += 5

    nominal_diskon = total_belanja * diskon/100
    total_setelah_diskon = total_belanja - nominal_diskon
    
    return nominal_diskon, total_setelah_diskon

total_belanja = int(input("Berapa total belanja anda? : "))
tanya = input("Apakah anda memiliki kartu keanggotaan? (ya/tidak) : ")
keanggotaan = input("Kartu keanggotaan apa yang anda miliki ? (gold/silver/bronze/none) : ")

nominal_diskon, total_setelah_diskon = calculate_discount(total_belanja, keanggotaan)

print("\nRincian Belanja")
print(f"Total belanja anda adalah : Rp {total_belanja:.0f}")
print(f"Anda sebagai keanggotaan : ({keanggotaan}) maka akan mendapat total diskon sebesar : Rp {nominal_diskon:.0f}")
print(f"Total belanja anda setelah diskon adalah : Rp {total_setelah_diskon:.0f}")