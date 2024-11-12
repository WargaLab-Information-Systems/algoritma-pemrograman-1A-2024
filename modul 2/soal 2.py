# input nama dan nilai
jaka = 1100 and 3.5
ida = 1000 and 3.5
print("siapakah yang lulus?")

# penyeleksian kondisi (jaka) menggunakan if - else
lulus = int(input("Berapa skor jaka? "))
if lulus > 1100 and lulus >= 3.0 and lulus < 4.0:
    print(f"jaka lulus persyaratan")
else:
    print(f"jaka tidak lulus persyaratan")

# penyeleksian kondisi (ida) menggunakan if - else
lulus1 = int(input("Berapa skor ida? "))
if lulus > 1100 and lulus >= 3.0 and lulus < 4.0:
    print(f"ida lulus persyaratan")
else:
    print(f"ida tidak lulus persyaratan")