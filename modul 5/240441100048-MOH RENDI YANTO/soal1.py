print("Selamat datang di supermarket")
kartu_member = input("Apakah anda memiliki keanggotaan? [ya/tidak] : "). lower()
diskon_member = 0
if kartu_member == "ya":
    diskon_member += 15 
elif kartu_member == "tidak":
    print('kamu tidak mendapatkan diskon')
def calculate_discount(total_spending, membership_type):
    if membership_type == "Gold":
        discount = 0.15
    elif membership_type == "Silver":
        discount = 0.10
    elif membership_type == "Bronze":
        discount = 0.05
    else:
        discount = 0.0  

    if total_spending > 1000000:
        discount += 0.05  

    total_discount = total_spending * discount
    return total_discount

total_belanja = int(input("masukkan total belanja : "))
jenis_keanggotaan = input("masukkan type membership: ")
diskon = calculate_discount(total_belanja, jenis_keanggotaan)
print(f"Diskon yang didapat:{diskon}")