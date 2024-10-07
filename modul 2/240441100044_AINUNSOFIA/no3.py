#no3
nama=input("masukkan nama:")
umur=int(input("masukkan umur:"))
if umur<=18:
    print("maaf, umur anda tidak cukup untuk melakukan pemeriksaan")
else:
    print("untuk tahap selanjutnya masukkan data di bawah ini")
    bb=float(input("masukkan berat badan anda (kg):"))
    tb=float(input("masukkan tinggi badan anda(m):"))
    #menghitung bmi
    bmi = bb / (tb ** 2)
    if bmi <=18.5:
        print(f"halo {nama}, hasil BMI anda adalah {bmi}, anda tipe kurus")
    elif bmi <=24.9:
        print(f"halo {nama}, hasil BMI anda adalah {bmi}, anda tipe normal")
    elif bmi <=29.9:
        print(f"halo {nama}, hasil BMI anda adalah {bmi}, anda tipe gemuk")
    else:
        print(f"halo {nama}, hasil BMI anda adalah {bmi}, anda tipe obesitas")
 