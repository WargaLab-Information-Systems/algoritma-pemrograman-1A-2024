# Tugas 5
print("Selamat datang di Bar Bita's !!")

nama_pembeli = str(input("masukkan nama pembeli: "))
usia_pembeli = int(input("masukkan usia pembeli: "))

if usia_pembeli < 18:
    print("lu masih bocil kocakk, pulang!!")
else:
    total_belanja = float(input("masukkan total belanja: "))
    kartu_member = str(input("punya kartu member kak? (punya/ngga hehe)"))
    
    diskon = 0
    if kartu_member == "punya":
        diskon += 15 
    if total_belanja > 500000:
        diskon += 10

total_kalau_dapat_diskon = total_belanja * (1 - diskon )
kalaw_sudah_diskon = total_belanja - total_kalau_dapat_diskon

print(f"nama pembeli : {nama_pembeli}" )
print(f"dapet diskon nichh : {diskon}%" )
print(f"total harga sesyudahhh diskon: {kalaw_sudah_diskon}")