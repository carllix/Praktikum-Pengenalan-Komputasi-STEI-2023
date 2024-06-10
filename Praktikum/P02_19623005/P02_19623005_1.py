# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 5 Oktober 2023
# Deskripsi : Program menentukan banyak kegiatan pada Gedung A dan Gedung B berdasarkan kapasitas dan inputan n

# KAMUS
# kegiatan_a, kegiatan_b, kegiatan, banyak_peserta : int

# ALGORITMA
# Input
n = int(input("Masukkan nilai N: "))

# Proses
kegiatan_a = 0
kegiatan_b = 0
kegiatan = 1

while kegiatan_b < 3:
    banyak_peserta = int(input(f"Masukkan peserta kegiatan ke-{kegiatan}: "))

    if banyak_peserta < n:
        if kegiatan_a<5:
            kegiatan_a+=1
        else:
            kegiatan_b+=1
    else:
        kegiatan_b+=1
    
    kegiatan+=1

# Output
print(f"Terdapat {kegiatan_a} kegiatan di gedung A dan {kegiatan_b} kegiatan di gedung B.")