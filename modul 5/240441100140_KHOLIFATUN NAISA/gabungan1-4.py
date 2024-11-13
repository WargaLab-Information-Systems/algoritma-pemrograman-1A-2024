#soal no 1
def no1 ():
    def calculate_diskon():
    # total_belanja = 0
        belanja = int (input("masukkan total belanja anda: "))
        anggota = input("apakah anda mempunyai ke anggotaan? bronze/silver/gold/tidak: ")
        potongan = 0
    # bronze = 5
    # silver = 10
    # gold = 15   
        if belanja >= 1000000:
            if anggota == "bronze":
                print("selamat anda mendapatkan potongan sebesar 5% juga mendapat potongan 5%")
                potongan += 10
                print(f"total belanja anda sebelum diskon adalah: {belanja}")
                print(f"total belanja anda setelah diskon adalah: {belanja * (1-potongan/100)}")
            elif anggota == "silver":
                print("selamat anda mendapatkan potongan sebesar 10% juga mendapat potongan 5%")
                potongan += 15
                print(f"total belanja anda sebelum diskon adalah: {belanja}")
                print(f"total belanja anda setelah diskon adalah: {belanja * (1-potongan/100)}")
            elif anggota == "gold":
                print("selamat anda mendapatkan potongan sebesar 15% juga mendapat potongan 5%")
                potongan += 20
                print(f"total belanja anda sebelum diskon adalah: {belanja}")
                print(f"total belanja anda setelah diskon adalah: {belanja * (1-potongan/100)}") 
            else:
                print("selamat anda mendapatkan potongan sebesar 5%")
                print(f"total belanja anda sebelum diskon adalah: {belanja}")
                print(f"total belanja anda adalah: {belanja * (1- 5/100)}")
        else:
            if anggota == "bronze":
                print("selamat anda mendapatkan potongan sebesar 5%")
                print(f"total belanja anda sebelum diskon adalah: {belanja}")
                print(f"total belanja anda adalah: {belanja * (1- 5/100)}") 
            elif anggota == "silver":
                print("selamat anda mendapatkan potongan sebesar 10%")
                print(f"total belanja anda sebelum diskon adalah: {belanja}")
                print(f"total belanja anda adalah: {belanja * (1- 10/100)}") 
            elif anggota == "gold":
                print("selamat anda mendapatkan potongan sebesar 15%")
                print(f"total belanja anda sebelum diskon adalah: {belanja}")
                print(f"total belanja anda adalah: {belanja * (1- 15/100)}") 
            else:
                print("mohon maaf anda tidak mendapat potongan")
                print(f"total belanja anda adalah: {belanja}") 
    calculate_diskon()

# #soal no 2
def no2():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci (n - 1) + fibonacci (n - 2)
    n = int (input("masukkan angka: "))
    print(fibonacci(n)) 
# fibonacci menjumlahkan dua suku angka sebelumnya

#soal no 3
def no3():
    def faktorial (a):
        if a <= 1:
            return 1
        else:
            hasil = a * faktorial (a - 1)
            return hasil
    angka = int (input("masukkan angka faktorial: "))
    print(f"hasil faktorial dari {angka} adalah {faktorial(angka)}")

#soal no 4
def no4():
    input_kata = str(input("masukkan kata palindrom: "))
    def cek_palindrom (input_kata):
        if input_kata == input_kata [:-1]:
            print(f"{input_kata} adalah kata palindrom")
        else:
            print(f"{input_kata} bukan kata palindrom")
        return input_kata
    x = input_kata
    print(cek_palindrom(x))

while True :
    print("soal no 1")
    print("soal no 2")
    print("soal no 3")
    print("soal no 4")
    pilih = int(input("mau no berapa: "))
    if pilih == 1:
        no1()
    elif pilih == 2:
        no2()
    elif pilih == 3:
        no3()
    elif pilih == 4:
        no4()
    else:
        print("masukkan dengan benar")
        break
    jawab = input("apakah mau ulang? ya/tidak: ")
    if jawab != "ya":
        break
#fungsi [::-1] dan [:-1]
#[::-1] untuk membalikkan angka 
#[:-1] untuk menghilangkan 1 angka


























