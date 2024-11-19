tanya = input("Apakah anda ingin menghitung ? (ya/tidak) : ")
pilihan = ()

def kalkulator():
    
    while True:
        if tanya == "ya":
            pilihan = str(input("Pilih operasi : "))
            if pilihan == "tambah":
                angka1 = int(input("Masukkan angka pertama : "))
                angka2 = int(input("Masukkan angka kedua : "))
                penjumlahan = angka1 + angka2
                print (f"Hasil dari {angka1} + {angka2} = {penjumlahan} ")


kalkulator()

