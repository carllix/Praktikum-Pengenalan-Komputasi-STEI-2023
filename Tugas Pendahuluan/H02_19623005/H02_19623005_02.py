# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 27 September 2023
# Deskripsi : Program Membuat Segitiga Istimewa Kembar Tuan Leo

# KAMUS
# h, current_number : int

# ALGORITMA
# Input
h = int(input("Masukkan nilai H: "))

# Proses
current_number = 0
for i in range(1,h+1):
    if i<=h/2:
        for j in range(i):
            current_number+=1
            print(current_number, end=" ")
    else:
        for j in range(h-i, -1, -1):
            current_number+=1
            print(current_number, end=" ")
    print()