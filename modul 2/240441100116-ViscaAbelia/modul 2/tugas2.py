#jaka = score 1100 dan ipk 3,5
scorejaka = int(input("Masukkan score jaka :"))
ipkjaka = float(input("Masukkan ipk jaka :"))

#ida = score 1000 dan ipk 3,5
scoreida = 1000
ipkida = 3.5
if (scorejaka > 1100 and ipkjaka >= 3.0):
    print("Jaka lulus persyaratan beasiswa")
elif (scoreida > 1100 and ipkida >= 3.0):
     print("Ida lulus persyaratan beasiswa")
else:
    print("tidak lulus persyaratan beasiswa")