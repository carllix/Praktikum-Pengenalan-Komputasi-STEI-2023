# NIMA/NAMA : 19623005/Carlo Angkisan
# TANGGAL : 2 November 2023
# DESKRIPSI : Program nilai tugas praktikum Tuan Kil yang terdiri dari dua buah suprogram

# KAMUS GLOBAL
# a,b,c,soal1,soal2,soal3 : float
def cekvalid(a,b,c): # Subprogram ini adalah fungsi
    # Fungsi untuk mengecek apakah bobot valid

    # KAMUS LOKAL
    # cek_valid : bool

    # ALGORITMA
    if a<0 or b<0 or c<0:
        cek_valid = False
    else:
        if a+b+c != 1:
            cek_valid = False
        else:
            cek_valid = True
    return cek_valid # mengeluarkan cek_valid

def hitung(a,b,c,soal1,soal2,soal3): # Subprogram ini adalah prosedur
    # Prosedur untuk menghitung nilai tugas praktikum 

    # KAMUS LOKAL
    # nilai : float

    # ALGORITMA
    cekvalid(a,b,c) # memanggil fungsi cekvalid
    if cekvalid(a,b,c)==True:
        nilai = a*soal1+b*soal2+c*soal3
        print("Nilai tugas praktikum adalah", nilai)
    else: # cekvalid(a,b,c)==False
        print("bobot tidak valid")

# ALGORITMA PROGRAM UTAMA
# Input
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))
soal1 = float(input("Masukkan nilai soal 1: "))
soal2 = float(input("Masukkan nilai soal 2: "))
soal3 = float(input("Masukkan nilai soal 3: "))

# Memanggil prosedur hitung
hitung(a,b,c,soal1,soal2,soal3)