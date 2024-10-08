berat_badan = float(input("masukkan berat badan mu dalam kg: "))
tinggi_badan = float(input("masukkan tinggi badan mu dalam cm: "))
tinggi_badan = tinggi_badan/100
#rumus bmi adalah berat badan dibagi tinggi
bmi = berat_badan/(tinggi_badan**2)

if 0 <= bmi < 18.5:
    print(f"kamu {bmi}kg kurus harus makan lebih banyak")
elif 18.5 <= bmi <= 24.9:
    print(f"kamu {bmi}kg normal")
elif 25 <= bmi <=29.9:
    print(f"kamu {bmi}kg kegemukan harus kurangi makan")
elif 30 <= bmi >= 100:
    print(f"berarti kamu obesitas {bmi}kg")
else:
    print("maaf inputan anda salah")