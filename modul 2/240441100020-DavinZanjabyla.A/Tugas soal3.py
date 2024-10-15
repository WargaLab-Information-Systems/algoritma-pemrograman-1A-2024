usia_pasien = int(input("Masukkan usia pasien: "))

if usia_pasien < 18:
    print("Maaf, usia Anda belum mencukupi.")
else:
    berat_pasien = float(input("Masukkan berat pasien : "))
    tinggi_pasien = float(input("Masukkan tinggi pasien : "))

    bmi = berat_pasien / (tinggi_pasien ** 2)
    print(f"BMI: {bmi:}")

    if bmi < 18.5:
        print("Anda tergolong KURUS.")
    elif bmi <= 24.9:
        print("Anda tergolong NORMAL.")
    elif bmi <= 29.9:
        print("Anda tergolong GEMUK.")
    else:
        print("Anda tergolong OBESITAS.")