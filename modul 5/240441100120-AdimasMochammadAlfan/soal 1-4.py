def menu():
    print()
    print('===== SOAL-SOAL MODUL 5 =====')
    print('1. soal 1')
    print('2. soal 2')
    print('3. soal 3')
    print('4. soal 4')
    print('5. Keluar')

    pilihan = input("masukkan pilihan anda : ")
    if pilihan == "1":
        soal_1()
    elif pilihan == "2":
        soal_2()
    elif pilihan == "3":
        soal_3()
    elif pilihan == "4":
        soal_4()
    elif pilihan == "5":
        print("terimakasih karena sudah mengecek Soal-Soal Modul 5")
    else:
        print("inputan yang anda masukkan kurang tepat")


def soal_1():
    keanggotaan = input("apakah anda memiliki keanggotaan ? : ")
    belanjaan = int(input("masukkan total belanjaan anda: "))

    def calculate_diskon():
        diskon = 0
        if keanggotaan == "y":
            keanggotaan1 = input("apa keanggotaan anda (gold,bronze,silver):")
            if keanggotaan1 == "gold" and belanjaan > 1000000:
                diskon += 20
            elif keanggotaan1 == "gold":
                diskon += 15
            elif keanggotaan1 == "bronze" and belanjaan > 1000000:
                diskon += 10
            elif keanggotaan1 == "bronze":
                diskon += 5
            elif keanggotaan1 == "silver" and belanjaan > 1000000:
                diskon += 15
            elif keanggotaan1 == "silver":
                diskon += 10
            else:
                diskon = 0
        elif keanggotaan == "n":
            keanggotaan1 = "anda tidak memiliki keanggotaan"
            if belanjaan > 1000000:
                diskon += 5
            else:
                diskon == 0

        print("keanggotaan anda adalah: ", keanggotaan1)
        print("total belanjaan sebelum diskon: ", belanjaan)
        setelah_diskon = belanjaan - (diskon/100 * belanjaan)
        print("total belanjaan setelah diskon: ", int(setelah_diskon))
    calculate_diskon()


def soal_2():
    def fibionacci (n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a = 0
            b = 1
            for i in range(2, n + 1): 
                a, b = b, a + b
            return b
    
    for i in range(0,11):
        print(fibionacci(i), end=" ")


def soal_3():
    def faktorial():
        hasil_akhirnya = 1
        angka = int(input("masukkan Angka : "))
        print()
        print(angka,"! = ", end= "")
        for i in range(1,angka + 1):
            print(i, end=" ")
            hasil_akhirnya = hasil_akhirnya * i
            if ( i != angka ) :
                print(" x ", end="")
        print(" = ", hasil_akhirnya)
        print()

    def main():
        print("Program python Sederhana\n")
        print("Menghitung faktorial")
        print()
        jumlah = input("Beberapa Jumlah Bilangan Faktorial yang ingin dihitung : ")
        i = 0
        while i < int(jumlah):
            faktorial()
            i += 1
    print(main())


def soal_4():
    x = input("masukkan kalimat: ")
    def cek_palindrome(kata):
        return kata == kata[::-1]

    if cek_palindrome(x) == True:
        print("palindrome")
    elif cek_palindrome(x) == False:
        print("bukan palindrome")
        
menu()
