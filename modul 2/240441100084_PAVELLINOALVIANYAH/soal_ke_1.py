# soal 1
nama = input(" masukan nama : ")
nim = input("masukan nim : ")
uts = int(input("masukan nilai UTS : "))
uas = int(input("masukan nilai UAS : "))

nilai_rata_rata = (uts + uas) / 2
if nilai_rata_rata >= 81 and nilai_rata_rata <100:
    hasil_seleksi = "A"
elif nilai_rata_rata >= 71 and nilai_rata_rata < 80:
    hasil_seleksi = "B"
elif nilai_rata_rata >= 61 and nilai_rata_rata < 70:
    hasil_seleksi = "C"
elif nilai_rata_rata >= 41 and nilai_rata_rata < 60:
    hasil_seleksi = "D"
elif nilai_rata_rata >= 0 and nilai_rata_rata < 40:
    hasil_seleksi = "E"
else:
    hasil_seleksi = "tidak ada nilai"

print(f"masukan nama {nama}")
print(f"nim anda: {nim}")
print(f"nilai rata rata nilai anda {nilai_rata_rata} anda mendapat kan nilai {hasil_seleksi}") 

# soal 2
def cek_peryaratan (skors, ipk):
    if skors > 1100 and ipk >= 3.0:
        return True
    else:
        return False

jaka_skors = 1100
jaka_ipk = 3.5
ida_skors = 1000
ida_ipk = 3.5

jaka_lulus = cek_peryaratan(jaka_skors, jaka_ipk)
ida_lulus = cek_peryaratan(ida_skors, ida_ipk)

if jaka_lulus:
    print("jaka lulus persyaratan beasiswa")
else:
    print("jaka tidak lulus persyaratan beasiswa")
if ida_lulus:
    print("ida lulus persyaratan beasiswa")
else:
    print("ida tidak lulus persyaratan beasiswa")

soal 3
nama = input("masukkan nama pasien: ")
age = int(input("masukakan usia pasien: "))
weight = float(input("masukkan berat badan pasien (kg): "))
height = float(input("masukan tinggi badan pasien (m): "))

if age < 18:
    print("maaf usia anda belum mencukupi")
else:
    bmi = (weight / height / height) * 10000
    if bmi < 18.5:
        bmi_category = "kurus"
    elif bmi <= 24.9:
        bmi_category = "normal"
    elif bmi <= 29.9:
        bmi_category = "gemuk"
    else:
        bmi_category = "obesitas"
    
    print(f"nama pasien: {nama}")
    print(f"BMI: {bmi}")
    print(f"kategori BMI: {bmi_category}")

# soal 4
tahun = int(input("masukkan tahun : "))
if tahun % 4 == 0:
    print("tahun kabisat")
else:
    if tahun % 100 == 0:
        print("bukan tahun kabisat")
    else:
        if tahun % 400 == 0:
            print("tahun kabisat")
        else:
            print("bukan tahun kabisat")

# soal 5
nama = input (" masukan nama pembeli : ")
age = int(input("masukkan usia pembeli : "))
is_mamber = input("apakah pembeli memiliki kartu member? (iya/tidak): ")
total_price = float(input("masukkan total harga belanja: "))
if age < 18:
    print("maaf usia anda belum mencukupi")
else:
    discount = 0
    if is_mamber.lower() == 'y':
        discount += 0.15
    if total_price > 500000:
        discount += 0.10

    original_price = total_price
    discounted_price = total_price * (1 - discount)

    print("nama pembeli:", nama)
    print("diskon yang di dapat kan:", discount * 100, "%")
    print("total harga sebelum diskon:", original_price)
    print("total harga setelah diskon:", discounted_price)

