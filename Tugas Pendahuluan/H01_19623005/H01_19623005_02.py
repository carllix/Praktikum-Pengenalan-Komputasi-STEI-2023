# NIM/Nama: 19623005/Carlo Angkisan
# Tanggal: 13 September 2023
# Deskripsi: Program Menentukan Jenis Garis

# KAMUS
# x1 : float
# x2 : float
# y1 : float
# y2 : float
# gradien : float

# ALGORITMA

# Input
x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))
x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))

# Proses
if x1 == x2: 
    print("Garis tersebut merupakan garis vertikal.")
elif y1 == y2: 
    print("Garis tersebut merupakan garis horizontal.")
else: # x1!=x2 and y1!=y2
    gradien = (y2-y1)/(x2-x1) 
    print(f"Garis tersebut memiliki gradien {gradien}.")

