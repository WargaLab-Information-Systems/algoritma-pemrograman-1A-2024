perawat ="sumanto"
print(f"selamat datang di program bmi{perawat}")
nama =input("masukan nama anda:")
usia =int(input("masukan usia anda:"))
if usia< 18:
    print("maaf anda belum dewasa")

bmi =float(input("masukan bmi anda:"))

if bmi<=18.5:
    print(f"{perawat}:{nama}anda kurus makanya makan")
elif bmi<=24.9:
    print(f"{perawat}bagus {nama}bmi kamu normal,pertanian")
elif bmi<=29.9:
    print(f"{perawat}:{nama}anda gemuk,diet dong")
elif bmi>=30:
    print(f"{perawat}:{nama} anda obesitas,diet,olaraga ya")        
