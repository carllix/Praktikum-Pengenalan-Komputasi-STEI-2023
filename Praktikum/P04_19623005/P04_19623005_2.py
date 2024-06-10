# NIMA/NAMA : 19623005/Carlo Angkisan
# TANGGAL : 2 November 2023
# DESKRIPSI : Matriks baru Nona Deb dengan menggantikan setiap elemen dalam matriks sebelumnya dengan jumlah elemen-elemen yang berada di sekitarnya secara horizontal dan vertikal

# KAMUS
# m,n,i,j : int
# matriks, matriks_baru : matriks of int

# ALGORITMA
# Input
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

# Deklarasi matriks ukuran (m+2)x(n+2)
# Matriks dilebihkan 2 baris dan 2 kolom agar nantinya untuk penjumlahan disekitar elemen tersebut tidak keluar dari range index
matriks = [[0 for j in range(n+2)] for i in range(m+2)]

# Input elemen matriks
# Untuk baris 0, baris m+2, kolom 0, baris n+2 dibirakan bernilai 0 agar nantinya untuk elemen yang berada dipinggir dapat tetap dijumlahkan dengan 0 agar tidak keluar dari range index
for i in range(1,m+1):
    for j in range(1,n+1):
        matriks[i][j] = int(input(f"Masukkan elemen matriks baris {i} kolom {j}: "))

# Deklarasi matriks_baru ukuran mxn untuk menampung nilai baru
matriks_baru = [[0 for j in range(n)] for i in range(m)]

# Proses
for i in range(m):
    for j in range(n):
        matriks_baru[i][j] = matriks[i][j+1]+matriks[i+2][j+1]+matriks[i+1][j]+matriks[i+1][j+2]

# Output
print("Matriks baru: ")
for i in range(m):
    for j in range(n):
        print(matriks_baru[i][j], end=" ")
    print()
