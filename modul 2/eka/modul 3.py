#input berat dan tinggi badan
berat_badan = float(input("masukkan berat badan pasien(kg): "))
tinggi_badan = float(input("masukkan tinggi badan pasian(meter): "))

#menghitung BMI
bmi = berat_badan / (tinggi_badan ** 2)

#menentukan kategori
if bmi < 18.5:
    kategori = "kurus"
elif bmi <= 24.9:
    kategori = "normal"
elif bmi <= 29.9:
    kategori = "gemuk"
else:
    kategori = "obesitas"

#menampilkan hasil
print(f"BMI pasien adalah {bmi} dan masuk pada kategori {kategori} ")