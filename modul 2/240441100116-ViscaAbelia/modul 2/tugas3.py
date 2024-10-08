#rumus menghitung BMI = berat badan(kg)/(tinggi badan(m) kuadrat)

usia = int(input("Masukkan usia :"))
if usia <= 18:
    print("Maaf perawat hanya melayani pasien usia di atas 18 tahun")
    exit()

bb = int(input("Masukkan berat badan :"))
tb = float(input("Masukkan tinggi badan :"))
BMI = bb/(tb*tb)


if BMI < 18.5:
    print("kurus")
elif BMI <= 24.9:
    print("Normal")
elif BMI <=29.9:
    print("Gemuk")
elif BMI >= 30:
    print("Obesitas")
else:
    print()