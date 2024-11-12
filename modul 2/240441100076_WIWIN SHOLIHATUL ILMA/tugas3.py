umur = int(input("Masukkan umur pasien: "))
if umur > 18 :
    # input data pasien
    berat = float(input("Masukkan berat badan pasien: "))
    tinggi = float(input("Masukkan tinggi badan pasien: "))
    tb_meter = tinggi / 100
    bmi = berat / (tb_meter * tb_meter)
    if bmi < 18.5:
        print("Tubuh Anda Kurus")
    elif 18.5 <= bmi <= 24.9:
        print("Tubuh Anda Normal")
    elif 25 <= bmi <= 29.9:
        print("Tubuh Anda Gemuk")
    else:
        print("Anda Obesitas",bmi)
else:
    print("Maaf umur anda tidak mencukupi")