# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 27 September 2023
# Deskripsi : Program Menentukan Bilangan Perpangkatan K

# KAMUS
# n, k, current_n : int

# ALGORITMA
# Input
n = int(input("Masukkan bilangan N: "))
k = int(input("Masukkan nilai k: "))

# Proses
current_n = n

while current_n>1:
    current_n/=k

if current_n==1:
    print(f"{n} merupakan perpangkatan {k}.")
else: # current_n!=1
    print(f"{n} bukan merupakan perpangkatan {k}.")