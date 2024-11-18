usia = int(input("Berapa usiamu? : "))

if usia >= 18:
    print("Kamu boleh periksa")
else:
    print("Mohon maaf, Kamu belum dewasa")
    exit (exit)

berat = int(input("Masukkan berat badanmu (kg) : "))
tinggi = int(input("Masukkan tinggi badanmu (cm) : "))

bmi = (berat / tinggi / tinggi) * 10000

if bmi < 18.5:
    print("Kamu kurus")
elif bmi <= 24.9:
    print("Kamu normal")
elif bmi <= 29.9:
    print("Kamu gemuk")
else:
    print("Kamu obesitas")
print (f"Berikut skor BMI anda : {bmi:.2f}")