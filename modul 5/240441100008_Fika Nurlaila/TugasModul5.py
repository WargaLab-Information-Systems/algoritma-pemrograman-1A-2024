
# 1. membuat calculate discount
def calculate_discount(total_belanja, jenis_anggota):
    diskon = 0
    
    # Kondisi jika belanja lebih dari 1 juta
    if total_belanja > 1000000:
        diskon += 5    
    
    if jenis_anggota.lower() == "y":
        print(" JENIS KEANGGOTAAN ")
        print("1. Gold")
        print("2. Silver")
        print("3. Bronze")
        keanggotaan = input("Jenis keanggotaan apa yang kamu miliki? (1/2/3): ")

        # Kondisi opsi keanggotaan
        if keanggotaan == "1":
            diskon += 15
        elif keanggotaan == "2":
            diskon += 10
        elif keanggotaan == "3":
            diskon += 5
        else:
            print("Bukan pilihan jenis keanggotaan.")
    else:
        print("Anda tidak memiliki keanggotaan.")

    # Menghitung total diskon dan total belanja setelah diskon
    total_belanja_diskon = total_belanja * (1 - (diskon / 100))

    print("===== STRUKTUR BELANJA =====")
    print("Anda mendapatkan diskon sebesar:", diskon, "%")
    print("Total belanja anda setelah diskon:", total_belanja_diskon)
    print("Total belanja anda sebelum diskon:", total_belanja)

input_total_belanja = int(input("Berapa total belanja kamu?: "))
input_jenis_anggota = input("Apakah kamu memiliki keanggotaan? (y/n): ")

calculate_discount(input_total_belanja, input_jenis_anggota)



# 2. membuat program fobonacci menggunakan fungsi rekursif ( memanggil dirinya sendiri untuk membuat 
#    perulangan tanpa memakai for atau while )
n = int(input("Masukkan batas bilangan: "))
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1,1]

    angka = fibonacci(n-1)
    
    # Menambahkan angka berikutnya ke deret
    angka_selanjutnya = angka[-1] + angka[-2]
    return angka + [angka_selanjutnya]
# menampilkan hasil dari fungsi
print("bilangan fibonaccinya adalah: ",fibonacci(n))


# 3. membuat fungsi untuk menghasilkan bilangan faktorial
n = int (input ("masukkan angka:"))
def faktorial (n,angka=""):     # parameter
    if n <= 1 :
        angka += "1"
        return 1,angka
    angka += str (n) + " X "
    angka_baru,angka= faktorial (n-1,angka)
    return angka_baru * n,angka
hasil,angka = faktorial(n)
print (n,"! =",angka,"=",hasil)



# 4. membuat fungsi yang menentukan kata palindrom
kata = str (input("masukkan kata : "))
def cek_palindrom(kata):
    kata_dibalik = ""
    kata_dibalik += kata [-1]
    kata = kata [:1]
    return kata == kata_dibalik

if cek_palindrom(kata):
    print(f"kata {kata}, adalah palindrom")
else :
    print(f"kata {kata}, bukan palingdrom")

