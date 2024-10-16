umur = int(input("masukkan umur anda : "))
if umur <= 18:
    print("maaf umur anda tidak cukup")
else:
    berat_badan = int(input("masukkan berat badan (kg) : "))
    tinggi_badan = float(input("masukkan tinggi badan (m) : "))

    bmi = berat_badan / (tinggi_badan**2)
    
    
    if 0 <= bmi < 18.5:
        kategori = "kurus" 
    elif 19 <= bmi <= 24.9:
        kategori = "normal"
    elif 25 <= bmi <= 29.9:
        kategori = "gemuk"
    elif 30 <= bmi <= 100:
        kategori = "obesitas"
    else:
        kategori = "masukkan inputan yang jelas"
    
    print("Nilai Bmi = ", bmi)
    print("kategori Bmi = ", kategori)
    


