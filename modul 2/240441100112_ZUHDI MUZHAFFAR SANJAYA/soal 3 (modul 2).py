berat_badan = float(input("masukkan berat badan mu dalam kg: "))
tinggi_badan = float(input("masukkan tinggi badan mu dalam cm: "))
tinggi_badan = tinggi_badan/100
#rumus bmi adalah berat badan dibagi tinggi
bmi = berat_badan/(tinggi_badan**2)

if bmi < 18.5:
    print(f"oh kamu {bmi}kg kurus makan lagi sih")
elif bmi <= 24.9:
    print(f"oh kamu {bmi}kg normal")
elif bmi <=29.9:
    print(f"kamu {bmi}kg kegemukan jangan makan terus dong")
elif bmi >= 30:
    print(f"awokawok kamu obesitas {bmi}kg")