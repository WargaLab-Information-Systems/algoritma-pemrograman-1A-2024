def calculate_discount(total_belanja, kartu_member):
    diskon = 0

    if total_belanja > 1000000:
        diskon += 5

    if kartu_member == "ya":
        print("A. Gold")
        print("B. Silver")
        print("C. Bronze")
        jenis_kartu_member = input("Masukkan kartu member anda (A/B/C): ")
    else:
        kartu_member = "Tidak punya"

    if kartu_member == "A":
        diskon += 15
    elif kartu_member == "B":
        diskon += 10
    elif kartu_member == "C":
        diskon += 5
    else:
        diskon += 0
    
    total_diskon = total_belanja * (diskon / 100)
    total_belanja_diskon = total_belanja - total_diskon

    return total_diskon, total_belanja_diskon

total_belanja = int(input("Masukkan total belanja anda: "))
kartu_member = str(input("Apakah anda memiliki kartu member?: (ya/tidak)"))

total_diskon, total_belanja_diskon = calculate_discount(total_belanja, kartu_member)

print(f"Total diskon yang anda dapatkan: {total_diskon}")
print(f"Total belanja anda yang mendapatkan diskon: {total_belanja_diskon}")