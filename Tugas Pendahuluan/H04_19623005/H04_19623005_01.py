# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 25 Oktober 2023
# Deskripsi : Program Mentukan Jumlah Maksimum Submatriks 2x2 Yang Memiliki Elemen Ganjil Dari Matriks mxn

# KAMUS
# matriks : matriks of integer
# m, n, maksimum, sum, i, j : int

# ALGORITMA

# Input
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

# Deklarasi matriks berukuran mxn berisi integer 0
matriks = [[0 for j in range(n)] for i in range(m)]

# Input elemen matriks dari user
for i in range(m):
    for j in range(n):
        matriks[i][j] = int(input(f"Masukkan elemen matriks baris {i+1} kolom {j+1}: "))

# Deklarasi variabel maksimum bernilai 0 untuk menampung jumlah maksimum dari submatriks 2x2 yang memiliki elemen ganjil
maksimum = 0

# Proses
for i in range(m-1):
    for j in range(n-1):
        if matriks[i][j]%2==1 or matriks[i][j+1]%2==1 or matriks[i+1][j]%2==1 or matriks[i+1][j+1]%2==1:
            sum = matriks[i][j]+matriks[i][j+1]+matriks[i+1][j]+matriks[i+1][j+1]
            if sum>maksimum:
                maksimum = sum

# Output
if maksimum == 0:
    print("Tidak ada submatriks 2x2 yang memenuhi syarat")
else:
    print(f"Jumlah maksimum submatriks berukuran 2x2 yang memiliki elemen ganjil adalah {maksimum}")
