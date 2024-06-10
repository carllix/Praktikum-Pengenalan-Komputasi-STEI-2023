# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 19 Oktober 2023
# Deskripsi : Program memeriksa kebenaran tulisan Komi

# KAMUS
# n_asli, n_ditulis, idx: integer
# i, j : integer
# kata_asli, kata_ditulis : string
# benar = boolean

# ALGORITMA
# Input
n_asli = int(input("Masukkan panjang kata asli: "))
kata_asli = input("Masukkan kata asli: ")
n_ditulis = int(input("Masukkan panjang kata yang ditulis: "))
kata_ditulis = input("Masukkan kata yang ditulis: ")

# Proses
benar = True
idx = 0
for i in range(n_asli):
    for j in range(i):
        if (kata_asli[j] != kata_ditulis[j+idx]):
            benar = False
    idx += i+1

if benar:
    print("\nTulisan Komi sudah benar.")
else:
    print("\nTulisan Komi masih salah.")