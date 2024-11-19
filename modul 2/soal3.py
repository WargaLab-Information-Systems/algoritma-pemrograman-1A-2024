
umur = int(input("masukkan umur anda : "))
if umur >= 18 :
    bb = int(input("masukkan berat badan anda : "))
    tb = int(input("masukkan tinggi badan anda : "))
    tb_meter = tb / 100
    bmi = bb / (tb_meter * tb_meter)
    if bmi <= 18 :
        print("anda kurus")
    elif bmi <= 24.9 :
        print("anda normal")
    elif bmi <= 29.9 :
        print ("anda gemuk")
    else :
        print ("anda obesitas")

    print ("hasil dari ", bmi)
else :
    print("maaf umur anda tidak mencukupi")