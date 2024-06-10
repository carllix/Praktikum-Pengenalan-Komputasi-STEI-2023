# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 25 Oktober 2023
# Deskripsi : Program Menghitung Kapal Musuh Nona Sal

# KAMUS
# map : matriks of integer
# map_string = str
# n, m, count, col, row, i, j : int

# ALGORITMA

# Input
n = int(input("Masukkan N: "))
m = int(input("Masukkan M: "))

# Deklarasi matriks berukuran (n+1)x(m+1) berisi integer 0
map = [[0 for i in range(m+1)] for i in range(n+1)]

# Proses
print("Masukkan peta: ")

# Input dalam bentuk string lalu convert ke integer dan masukkan ke dalam matriks map
for i in range(n):
    map_string = input()
    for j in range(m):
        map[i][j] = int(map_string[j])

# Deklarasi variabel count bernilai 0 untuk menampung jumlah kapal musuh
count = 0

for i in range(n):
    for j in range(m):
        if map[i][j]==1: # Jika betemu dengan 1 maka diubah menjadi 0 agar tidak terhitung lagi
            map[i][j] = 0
            count+=1

            # cek arah horizontal (kanan)
            if map[i][j+1]==1:
                col = j+1
                while map[i][col]==1:
                    map[i][col] = 0
                    col+=1

            # cek arah vertikal (bawah)
            if map[i+1][j]==1:
                row = i+1
                while map[row][j]==1:
                    map[row][j] = 0
                    row+=1
                    
# Output
if count==0:
    print("Tidak terdapat kapal musuh pada peta")
else: # count!=0
    print(f"Terdapat {count} kapal musuh pada peta")