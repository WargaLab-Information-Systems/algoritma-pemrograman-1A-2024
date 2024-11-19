# Tugas 3
# BMI (Body Massa Index)
# umur_pasien = 18
# kurus = 18.5
# normal = 24.9
# gemuk = 29.9
# obesitas = 30

umur = int(input("masukkan umur Anda: "))
berat_badan = int(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (meter): "))

bmi = berat_badan / (tinggi_badan ** 2)

if bmi <= 18.5:
    kategori = "Kurus"
elif bmi <= 24.9:
    kategori = "Normal"
elif bmi <= 29.9:
    kategori = "Gemuk"
else:
    kategori = "Obesitas"

print(f"BMI: {bmi}, Kategori: {kategori}")
