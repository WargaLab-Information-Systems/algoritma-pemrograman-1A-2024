usia = int(input("masukkan usia anda: "))
if usia < 18 :
    print("pak sumanto hanya memeriksa usia 18 tahun keatas")
else:
    tb = float(input ("silahkan masukkan tinggi badan anda: "))
    bb = float(input ("silahkan masukkan berat badan anda: "))
    bmi = bb//(tb*tb)
if  18.5 >= bmi >= 0 :
    print ("anda kurus")
elif 24.9 >= bmi >=17:
    print ("anda normal")
elif 29.9 >= bmi >=23.9:
    print ("anda gemuk")
elif 100 >= bmi >= 30:
    print("anda obesitas")
else:
    print("tidak terdaftar di bmi")
print (f"hasil bmi anda adalah {bmi}")
