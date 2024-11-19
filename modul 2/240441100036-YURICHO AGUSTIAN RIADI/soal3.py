nama =input("masukkan nama perawat: ")
umur =int(input("masukkan umur pasien: "))
berat =int(input("masukkan berat pasien: "))
tinggi =int(input("masukkan tinggi pasien: "))

# minimal umur pasien
if umur >=18:
    print("pasien dewasa")
    
# menghitung BMI
tinggi_m = tinggi / 100 
bmi = berat / tinggi_m **2

# menentukan kategori BMI
if bmi < 18.5:
    print =("kurus")
elif bmi <=24.9:
    print =("normal")
elif bmi <=29.9:
    print =("gemuk")
else:
    print("obesitas")