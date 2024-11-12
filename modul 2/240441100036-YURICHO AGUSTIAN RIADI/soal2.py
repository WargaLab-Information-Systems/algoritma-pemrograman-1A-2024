# Data mahasiswa
nama ="jaka"
skor1 ="1100"
jaka_ipk ="3.5"

nama ="ida"
skor2 ="1000"
ida_ipk ="3.5"

# syarat beasiswa
skor_minimal ="1100"
ipk_minimal ="3.0"

# cek kelulusan jaka dan ida
if skor1 > skor_minimal and jaka_ipk >= ipk_minimal:
    print("jaka lulus syarat beasiswa")
else:
    print("jaka tidak lulus syarat beasiswa")
    
if skor2 > skor_minimal and ida_ipk >= ipk_minimal:
    print("ida lulus syarat beasiswa")
else:
    print("ida tidak lulus syarat beasiswa")
