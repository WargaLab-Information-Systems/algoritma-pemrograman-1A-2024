print ("jadi alat kesehatan yang dipinjam heni saat ini setelah semua proses peminjaman dan pengembalian dilakukan yaitu")

alat_kesehatan = {
    'glukometer': 0,
    'termometer': 0,
    'sphygmomanometer': 0,
    'inhaler': 0
} 

def pinjam_alat(alat, jumlah):
    """Fungsi untuk meminjam alat kesehatan."""
    if alat in alat_kesehatan:
        alat_kesehatan[alat] += jumlah
    else:
        print(f"{alat} tidak tersedia untuk dipinjam.")

def kembalikan_alat(alat, jumlah):
    """Fungsi untuk mengembalikan alat kesehatan."""
    if alat in alat_kesehatan and alat_kesehatan[alat] >= jumlah:
        alat_kesehatan[alat] -= jumlah
    else:
        print(f"Tidak dapat mengembalikan {jumlah} {alat}. Jumlah saat ini: {alat_kesehatan[alat]}")

def tukar_alat(alat_dikembalikan, jumlah_dikembalikan, alat_ditukar, jumlah_ditukar):
    """Fungsi untuk menukar alat kesehatan."""
    kembalikan_alat(alat_dikembalikan, jumlah_dikembalikan)
    pinjam_alat(alat_ditukar, jumlah_ditukar)


pinjam_alat('glukometer', 2)     
pinjam_alat('termometer', 3)      
pinjam_alat('sphygmomanometer', 4)  

kembalikan_alat('glukometer', 1)
kembalikan_alat('termometer', 2)

tukar_alat('sphygmomanometer', 3, 'inhaler', 2)


print("Alat kesehatan yang dipinjam Heni saat ini:")
for alat, jumlah in alat_kesehatan.items():
    if jumlah > 0:
        print(f"{alat}: {jumlah}")