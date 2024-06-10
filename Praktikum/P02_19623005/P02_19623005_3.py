# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 5 Oktober 2023
# Deskripsi : Program Membuat Piramida Nona Deb

# KAMUS
# panjang, selisih, a : integer
# i, j : integer

# ALGORITMA
# Input
panjang = int(input("Masukkan panjang piramida : "))
selisih = int(input("Masukkan selisih piramida : "))
a = 1

# Proses
if panjang%2==0:
    panjang -= 1

if panjang % 2 != 0 and panjang <=75:
    for i in range (1, (panjang//2)+2):
        for j in range (panjang//2, i-1, -1): # membentuk X sebelum angka
            print("X", end="")
        for j in range (1, i+1):
            print(a, end="")
        for j in range(5, i+4):
            print(a, end="")
        a += selisih
        if a > 10:
            a = a%10
        for j in range (panjang//2, i-1, -1): # membentuk X sesudah angka
            print("X", end="")
        print()