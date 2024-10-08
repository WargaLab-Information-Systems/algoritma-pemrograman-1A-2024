# input usia pasien sumanto 
usia_pasien_sumanto = int(input("masukkan usia pasien: "))
berat = 100
tinggi = 187

# penyeleksian kondisi menggunakan if bersarang
if usia_pasien_sumanto > 18 :
    print(f"usia pasien sumanto siap diperiksa")
    bmi = berat / tinggi **2
    if bmi < 18.5:
        print(f"bmi kurus")
    elif bmi <= 24.9:
        print(f"usia pasien sumanto bmi normal")
    elif bmi <=29.9:
        print(f"usia pasien sumanto bmi gemuk")
    elif bmi >=30:
        print(f"usia pasien sumanto bmi obesitas")   
else: 
    print(f"usia pasien sumanto tidak siap diperiksa")