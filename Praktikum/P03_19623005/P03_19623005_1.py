# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 19 Oktober 2023
# Deskripsi : Program Pembayaran Minimal Tuan Kil Jika Makan 3 Jam Tanpa Henti

# KAMUS
# arr_harga : array[0...n-1] of int
# arr_total : array[0...n-3] of int
# n, harga_minimal, i: int

# ALGORITMA
# Input
n = int(input("Masukkan nilai N: "))

# Deklarasi array dan variabel
arr_harga = [0 for i in range(n)]
arr_total = [0 for i in range(n-2)]
harga_minimal = 0

# Proses
if n<3:
    print("n harus lebih dari sama dengan 3.")
else: # n>=3
    # Input harga setiap jam ke dalam arr_harga
    for i in range(n):
        arr_harga[i] = int(input(f"Masukkan harga jam ke-{i+1}: "))
    
    # Menghitung total harga makan 3 jam berturut
    for i in range(n-2):
        arr_total[i]+=arr_harga[i]+arr_harga[i+1]+arr_harga[i+2]

    # Mencari harga minimum
    harga_minimal = arr_total[0]
    for i in range(1, n-2):
        if arr_total[i]<harga_minimal:
            harga_minimal = arr_total[i]
    print(f"Total harga yang harus dibayar adalah {harga_minimal}.")


