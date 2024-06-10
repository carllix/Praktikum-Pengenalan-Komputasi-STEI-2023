# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 21 September 2023
# Deskripsi : Program Menentukan Angka Spesial

# KAMUS
# num,a,b,c,d : integer

# ALGORITMA
# Input
num = int(input("Masukkan Angka: "))

# Proses
a = num//1000%10
b = num//100%10
c = num//10%10
d = num%10

if (a*d) % (b+c) == 0:
    print(f"Angka {num} adalah angka spesial.")
else:
    print(f"Angka {num} bukan angka spesial.")