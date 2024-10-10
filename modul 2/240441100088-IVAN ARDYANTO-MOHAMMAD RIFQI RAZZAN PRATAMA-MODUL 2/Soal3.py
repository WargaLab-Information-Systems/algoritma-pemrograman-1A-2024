umur = int(input("Masukkan umur: "))

if umur >= 18:
    bb = int(input("Masukkan berat badan (kg): "))
    tb = int(input("Masukkan tinggi badan (cm): "))
    
    # Rumus Konversi tinggi dari cm ke m yg ada di google
    tb_m = tb / 100
    
    # Rumus Hitung BMI yang ada di google
    bmi = bb / (tb_m * tb_m)
    
    
    if bmi < 18.5:
        kategori = "Kurus"
    elif bmi <= 24.9:
        kategori = "Normal"
    elif bmi <= 29.9:
        kategori = "Gemuk"
    else:
        kategori = "Obesitas"
    
    print("BMI = ", bmi)
    print(f"Kategori: {kategori}")
else:
    print("Maaf, dokter Sumanto hanya memeriksa pasien berusia 18 tahun ke atas")