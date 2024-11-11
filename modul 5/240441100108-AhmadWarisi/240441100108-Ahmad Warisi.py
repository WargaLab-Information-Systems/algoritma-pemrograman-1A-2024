#Soal No 1
def calculate_discount(total_belanja, membership):
  
    if membership == "Gold":
        diskon = 15
    elif membership == "Silver":
        diskon = 10
    elif membership == "Bronze":
        diskon = 5
    else:
        diskon = 0
    
    # Tambahan diskon untuk pembelian di atas 1 juta
    if total_belanja > 1000000:
        diskon += 5
        
    return diskon

def hitung_total_setelah_diskon(total_belanja, membership):
    
    diskon_persen = calculate_discount(total_belanja, membership)
    total_diskon = total_belanja * (diskon_persen / 100)
    total_setelah_diskon = total_belanja - total_diskon
    
    return diskon_persen, total_diskon, total_setelah_diskon

# Input total belanja
print("=== Program Hitung Diskon Supermarket ===")
while True:
    total_belanja = float(input("Masukkan total belanja (Rp): "))
    if total_belanja < 0:
        print("Total belanja tidak boleh negatif!")
        continue
    break

# Input jenis membership
print("Jenis Membership:")
print("1. Gold")
print("2. Silver")
print("3. Bronze")
print("4. Tidak ada membership")

while True:
    pilihan = input("Pilih jenis membership (1-4): ")
    if pilihan == "1":
        membership = "Gold"
        break
    elif pilihan == "2":
        membership = "Silver"
        break
    elif pilihan == "3":
        membership = "Bronze"
        break
    elif pilihan == "4":
        membership = "Tidak ada Membership"
        break
    else:
        print("Pilihan tidak valid! Silakan pilih 1-4")

# Hitung diskon dan total
diskon_persen, total_diskon, total_setelah_diskon = hitung_total_setelah_diskon(total_belanja, membership)

# Hasil
print("=== Hasil Perhitungan ===")
print("Total Belanja: Rp : ",total_belanja)
print("Jenis Membership : ",membership)
print("Persentase Diskon : ",diskon_persen,"%")
print("Total Diskon: Rp :",total_diskon)
print("Total yang harus dibayar Rp : ",total_setelah_diskon)

#Soal No 2
def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

print("=== Program Fibonacci Rekursif ===")
print("Ketik angka negatif untuk mengakhiri program")
print()

while True:
    n = int(input("Masukkan nilai n: "))
    
    if n < 0:
        print("Terima kasih telah menggunakan program ini!")
        break

    hasil = fibonacci(n)
    
    # Tampilkan hasil
    print("Fibonacci ke-",n,"adalah",hasil)
    
    # Tampilkan deret hingga n
    print("Deret Fibonacci hingga ke-",n)
    for i in range(n + 1):
        if i == n:
            print(fibonacci(i))
        else:
            print(fibonacci(i), end=", ")
    print()

#Soal No 3
def hitung_faktorial(n):
   
    # Basis kasus faktorial 0 adalah 1
    if n == 0:
        return 1
        
    # Hitung faktorial
    hasil = 1
    for i in range(1, n + 1):
        hasil = hasil * i
        
    return hasil

# Program utama
print("=== Program Hitung Faktorial ===")
print("Ketik angka negatif untuk mengakhiri program")
print()

while True:
    angka = int(input("Masukkan angka: "))
    
    if angka < 0:
        print("Terima kasih telah menggunakan program ini!")
        break
        
    # Hitung faktorial
    hasil = hitung_faktorial(angka)
    
    # Tampilkan proses perhitungan
    print(angka,"! = ", end="")
    # Tampilkan perkalian
    for i in range(angka, 0, -1):
        if i == 1:
            print(i, end="")
        else:
            print(i," x ", end="")
            
    print(" = ",hasil)
    print()

#Soal No 4
def cek_palindrom(kata):
    # Balik kata secara manual
    kata_terbalik = ""
    for huruf in kata:
        kata_terbalik = huruf + kata_terbalik
    
    # Bandingkan kata asli dengan kata yang sudah dibalik
    return kata == kata_terbalik

# Program utama
print("=== Program Cek Palindrom ===")
print("Ketik 'selesai' untuk mengakhiri program")
print()

while True:
    kata = input("Masukkan kata: ")
    if kata == "selesai":
        print("Terima kasih telah menggunakan program ini!")
        break

    hasil = cek_palindrom(kata)
    
    # Tampilkan hasil
    if hasil:
        print(kata,"adalah palindrom")
    else:
        print(kata,"bukan palindrom")
    print()
