# pasien_sumanto = "usia > 18 tahun"
nama_pasien = input("masukkan nama pasien: ")
usia_pasien_sumanto = int(input("masukkan usia pasien: "))
berat_badan = int(input("masukkan berat badan pasien: "))
tinggi_badan = int(input("masukkan tinggi badan pasien: "))

# rumus menghitung bmi
bmi = (berat_badan / tinggi_badan)



if bmi < 18.5:
    print(f"bmi kurus")
elif bmi <= 24.9:
    print(f"bmi normal")
elif bmi <= 29.9:
    print(f"bmi gemuk")
elif bmi >= 30:
    print(f"bmi obesitas")
else:
    print("bmi tidak diketahui")