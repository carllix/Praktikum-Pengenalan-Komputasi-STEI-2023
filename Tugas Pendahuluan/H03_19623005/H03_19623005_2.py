# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 11 Oktober 2023
# Deskripsi : Program menentukan nilai terbesar ke-N Tuan Kil

# KAMUS
# list_data: array [0..data] of int
# data, n, temp, i, j: int

# ALGORITMA
# Input
data = int(input("Masukkan banyak data: "))
n = int(input("Masukkan nilai N: "))

# Deklarasi array berukuran data dengan isi 0
list_data = [0 for i in range(data)]

# Input data
for i in range(data):
    list_data[i] = int(input(f"Masukkan data ke-{i+1}: "))

# Mengurutkan elemen pada array dari terbesar hingga ke terkecil
for i in range(data):
    for j in range(i+1, data):
        if list_data[i]<list_data[j]:
            temp = list_data[i]
            list_data[i] = list_data[j]
            list_data[j] = temp

print(f"Nilai terbesar ke-{n} adalah {list_data[n-1]}")
