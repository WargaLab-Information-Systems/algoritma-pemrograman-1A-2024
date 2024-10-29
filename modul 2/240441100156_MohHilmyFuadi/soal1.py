# Input data mahasiswa
nama = input("Masukan Nama: ")
nim = input("Masukan NIM: ")
nilai_uts = int(input("Masukan Nilai UTS: "))
nilai_uas = int(input("Masukan Nilai UAS: "))

# Menghitung nilai rata-rata
nilai_rata_rata = (nilai_uts + nilai_uas) / 2

# Menentukan grade berdasarkan nilai rata-rata
if 81 <= nilai_rata_rata <= 100:
    grade = "A"
    print(f"Masukan Nama: {nama}")
    print(f"Masukan NIM: {nim}")
    print(f"Nilai UTS: {nilai_uts}")
    print(f"Nilai UAS: {nilai_uas}")
    print(f"Nilai rata-rata anda: {nilai_rata_rata}")
    print(f"Anda Mendapatkan Nilai: {grade}")

elif 71 <= nilai_rata_rata <= 80:
    grade = "B"
    print(f"Masukan Nama: {nama}")
    print(f"Masukan NIM: {nim}")
    print(f"Nilai UTS: {nilai_uts}")
    print(f"Nilai UAS: {nilai_uas}")
    print(f"Nilai rata-rata anda: {nilai_rata_rata}")
    print(f"Anda Mendapatkan Nilai: {grade}")

elif 61 <= nilai_rata_rata <= 70:
    grade = "C"
    print(f"Masukan Nama: {nama}")
    print(f"Masukan NIM: {nim}")
    print(f"Nilai UTS: {nilai_uts}")
    print(f"Nilai UAS: {nilai_uas}")
    print(f"Nilai rata-rata anda: {nilai_rata_rata}")
    print(f"Anda Mendapatkan Nilai: {grade}")
elif 41 <= nilai_rata_rata <= 60:
    grade = "D"
    print(f"Masukan Nama: {nama}")
    print(f"Masukan NIM: {nim}")
    print(f"Nilai UTS: {nilai_uts}")
    print(f"Nilai UAS: {nilai_uas}")
    print(f"Nilai rata-rata anda: {nilai_rata_rata}")
    print(f"Anda Mendapatkan Nilai: {grade}")
elif nilai_rata_rata >100 :
    grade  = "gaada"
    print (f"nilai tidak valid")
else:
    grade = "E"
    print(f"Masukan Nama: {nama}")
    print(f"Masukan NIM: {nim}")
    print(f"Nilai UTS: {nilai_uts}")
    print(f"Nilai UAS: {nilai_uas}")
    print(f"Nilai rata-rata anda: {nilai_rata_rata}")
    print(f"Anda Mendapatkan Nilai: {grade}")
