# Tugas 4
tahun = int(input("Masukkan Tahun: "))

if tahun % 4 != 0:
    print(f" {tahun}  Bukan Tahun kabisat") 
elif tahun % 100 != 0:
    print(f" {tahun} Adalah Tahun kabisat") 
elif tahun % 400 != 0 :
    print(f" {tahun}  Bukan Tahun kabisat") 
else:
    print(f" {tahun} Adalah Tahun kabisat")
    
