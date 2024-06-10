# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 11 Oktober 2023
# Deskripsi: Program menentukan rute kereta yang mengunjungi stasiun terbanyak berdasarkan uang yang dimiliki Tuan Leo

# KAMUS
# arr_harga, arr, kunjungan : array [0..jumlah_stasiun] of int
# uang, jumlah_stasiun, recent_uang, n, i, j, jumlah_kunjungan, stasiun : int

# ALGORITMA
# Input
uang = int(input("Masukkan uang yang dibawa Tuan Leo: "))
jumlah_stasiun = int(input("Masukkan jumlah stasiun: "))

# Deklarasi array berukuran jumlah_stasiun dengan tipe integer
arr_harga = [0 for i in range(jumlah_stasiun)]
arr_kunjungan = [-1 for i in range(jumlah_stasiun)]

# Input harga setiap stasiun
for i in range(jumlah_stasiun):
    arr_harga[i] = int(input(f"Masukkan harga stasiun ke-{i+1}: "))

# Menghitung banyak stasiun yang dapat dikunjungi dari setiap stasiun keberangkatan
for i in range(jumlah_stasiun):
    recent_uang = uang
    n = i
    while recent_uang >= 0 and arr_kunjungan[i]<jumlah_stasiun:
        recent_uang-=arr_harga[n%jumlah_stasiun]
        n+=1
        arr_kunjungan[i]+=1

jumlah_kunjungan = 0
stasiun = 0

# Mencari stasiun keberangkatan yang menghasilkan kunjungan stasiun terbanyak
for i in range(jumlah_stasiun):
    if arr_kunjungan[i]>jumlah_kunjungan:
        jumlah_kunjungan = arr_kunjungan[i]
        stasiun = i+1

if jumlah_kunjungan>0:
    print(f"Tuan Leo dapat mengunjungi {jumlah_kunjungan} stasiun dimulai dari stasiun ke-{stasiun}.")
else:
    print("Tuan Leo kekurangan uang.")