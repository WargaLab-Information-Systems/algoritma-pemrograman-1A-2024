
perawat = "Sumanto"

print(f"Selamat Datang di program BMI {perawat}")
print("-------------------------------------")

nama = input("masukkan nama anda : ")
usia = int(input("masukkan usia anda : "))

# perintah if 
if usia < 18:
    print("maaf anda belum dewasa")
    exit()
    
berat_badan = float(input("Masukkan berat badan anda (kg) : "))
tinggi_badan = float(input("Masukkan tinggi badan anda (m) : "))
BMI = berat_badan / (tinggi_badan**2)
    

# perintah if elif
if BMI <= 18.5:
    print(f"{perawat}: {nama} kamu kurus, banyakin makan makanan berprotein  yaa!")
elif BMI <= 24.9:
    print(f"{perawat}: alhamdulillah {nama} BMI kamu masih normal, jaga kesehatan terus yaa!")
elif BMI <= 29.9:
    print(f"{perawat}: {nama} kamu udah gemuk, kurangin dulu makan daging sama diet dulu yaa!")
elif BMI >= 30:
    print(f"{perawat}: {nama} kamu obesitas, kamu harus sering olahraga + diet dulu yaa!")
    