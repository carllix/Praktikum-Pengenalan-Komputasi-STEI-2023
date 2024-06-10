# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 25 Oktober 2023
# Deskripsi : Program Hitung Jumlah Bakteri Pengkombacter Setelah K Detik

# KAMUS GLOBAL
# n, k: int
# Fungsi hitung_Pengkombacter
def hitung_Pengkombacter(n,k):
    # Menghitung total Bakteri Pengkombacter setelah K detik

    # KAMUS LOKAL
    # total_bakteri, i : int

    # ALGORITMA
    total_bakteri = 0
    for i in range(k+1):
        total_bakteri+=n
        n*=2
    return total_bakteri
        
# ALGORITMA PROGRAM UTAMA
n = int(input("Masukkan N: "))
k = int(input("Masukkan K: "))

# Output
print(f"Terdapat {hitung_Pengkombacter(n,k)} Bakteri Pengkombacter.")