# Input data pembeli
print("Selamat Datang di Bar kami")
nama = str(input("Masukkan nama anda : "))
umur = int(input("Masukkan usia anda : "))

# Pengkondisian jika belum cukup umur maka tidak boleh memesan
if umur <= 18:
    print("Mohon maaf, anda belum cukup umur")
else:

    total_belanja = int (input("Masukkan total belanja : Rp "))
    member = input("Apakah anda memiliki kartu member? (y/n): ") .lower()

diskon = 0
if member == 'y':
    diskon += 15
if total_belanja > 500000:
    diskon += 10

nominal_Diskon = total_belanja * diskon /100
total_setelah_diskon = total_belanja - nominal_Diskon

print("\nRincian Pembelian")
print(f"Nama Pembeli: {nama}")
print(f"Diskon yang didapatkan : {diskon}%")
print(f"Total harga sebelum diskon : Rp{total_belanja}")
print(f"Total harga setelah diskon : Rp{total_setelah_diskon}")