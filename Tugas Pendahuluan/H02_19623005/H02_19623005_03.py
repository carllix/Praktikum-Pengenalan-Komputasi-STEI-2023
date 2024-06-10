# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 27 September 2023
# Deskripsi : Program Menentukan Ketercapaian Bilangan N dari Perkalian Dua Bilangan A dan B Secara Bergantian

# KAMUS
# a, b, n, current_number : int

# ALGORITMA
# Input
a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
n = int(input("Masukkan bilangan N: "))

# Proses
current_number = 1
while current_number<n:
    current_number*=a
    if current_number<n:
        current_number*=b

if current_number == n:
    print(f"Bilangan {n} dapat dicapai.")
else: # current_number != n
    current_number = 1
    while current_number<n:
        current_number*=b
        if current_number<n:
            current_number*=a
    if current_number == n:
        print(f"Bilangan {n} dapat dicapai.")
    else: # current_number != n
        print(f"Bilangan {n} tidak dapat dicapai.") 