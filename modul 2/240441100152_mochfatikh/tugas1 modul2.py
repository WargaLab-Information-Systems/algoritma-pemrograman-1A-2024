nama =input("masukan nama:")
nim =input("masukan nim:")
nilai_uts =int(input("masukan nilai uts:"))
nilai_uas =int(input("masukan nilai uas:"))
nilai_rata_rata=(nilai_uas+nilai_uts)
if nilai_rata_rata>=81:
    nilai="a"
elif nilai_rata_rata>=71:
    nilai="b"
elif nilai_rata_rata>=61:
    nilai="c"
elif nilai_rata_rata>=41:
    nilai="e"
else:
    nilai="e"
print("masukan nama",nama)
print("masukan",nim)
print("nilai rata rata anda",nilai_rata_rata)
print("anda mendapatkan",nilai)