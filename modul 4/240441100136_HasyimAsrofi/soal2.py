# Meminta input bilangan desimal dari pengguna
bilangan_desimal = int(input("Masukkan bilangan desimal: "))

# Konversi desimal ke biner
bilangan_biner = ""
if bilangan_desimal == 0:
    bilangan_biner = "0"
else:
    while bilangan_desimal > 0:
        bilangan_biner = str(bilangan_desimal % 2) + bilangan_biner
        bilangan_desimal //= 2

# Menampilkan hasil konversi
print(f"Bilangan biner: {bilangan_biner}")

# Menampilkan pola segitiga
print("Pola Segitiga:")
for i in range(len(bilangan_biner)):
    print(bilangan_biner[:i + 1])  # Mencetak i+1 digit pertama dari bilangan_biner