Nama = str(input("Masukkan nama anda:"))
#usia pasien sumanto >18 tahun
Usia = int(input("Masukkan usia anda:"))
tinggi = int(input("Masukkan tinggi anda:"))
berat_badan = int(input("Masukkan berat badan anda:"))
body_mass_index_pasien = berat_badan/tinggi*tinggi
if Usia <18 :
    print("Maaf Usia anda tidak mencukupi")
else:
    if body_mass_index_pasien < 18.5:
        print("Anda kurus")
    elif body_mass_index_pasien <= 24.9:
     print("Anda normal")
    elif body_mass_index_pasien <= 29.9:
        print("Anda gemuk")
    else:
        body_mass_index_pasien >= 30.0
        print("Anda obesitas")
