print("Membantu sumanto untuk memilih pasien dewasa dan menghitung BMI pasiennya")
umur = int(input("Masukkan umur anda : "))
if umur <18 :
    print ("umur anda tidak cukup")
else :
    bb = int(input("Masukkan Berat Badan anda : "))
    tb = int(input("Masukkan Tinggi Badan anda : "))

    tinggi_badan = tb/100
    bmi = (bb / (tinggi_badan**2))

    if bmi <18.5 :
        print ("anda kurus")
    elif bmi <= 24.9 :
        print ("anda normal")
    elif bmi <= 29.9 :
        print ("anda gemuk")
    else :
        print ("anda obesitas")
