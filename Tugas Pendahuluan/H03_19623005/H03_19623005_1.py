# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 114 Oktober 2023
# Deskripsi : Program menentukan nomor perwakilan yang tidak datang pada acara tahunan Kota Kompeng

# KAMUS
# is_hadir : array [0..n] of bool
# n, m, data, i, j : int

# ALGORITMA
# Input
n = int(input("Masukkan nilai N: "))
m = int(input("Masukkan nilai M: "))

# Deklarasi array berukuran n dengan isi False
is_hadir = [False for i in range(n)]

# Proses
for i in range(m):
    data = int(input(f"Masukkan data ke-{i+1}: "))
    for j in range(n):
        if data == j+1:
            is_hadir[j] = True
            
print("Nomor perwakilan yang tidak datang:", end=" ")
for i in range(n):
    if is_hadir[i] == False:
        print(i+1, end=" ")