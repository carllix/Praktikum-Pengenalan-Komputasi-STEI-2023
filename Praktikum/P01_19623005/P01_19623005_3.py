# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 21 September 2023
# Deskripsi : Program Menentukan Jumlah Baju Yang Dapat Dibuat Nona Deb

# KAMUS
# jumlah_kain : float
# jumlah_pita : float
# jumlah_l : integer
# jumlah_m : integer
# jumlah_s : integer

# ALGORITMA
# Input
jumlah_kain = float(input("Jumlah Kain: "))
jumlah_pita = float(input("Jumlah Pita: "))

# Proses
if jumlah_kain<4.7 or jumlah_pita<3.1:
    print("Bahan tidak cukup untuk membuat baju.")
else:
    jumlah_kain -= 4.7
    jumlah_pita -= 3.1
    jumlah_l = 1
    jumlah_m = 1
    jumlah_s = 1

    # Ukuran L
    if jumlah_kain>=2 and jumlah_pita>=1.3:
        # Ambil minimum antara kain dan pita
        if (jumlah_kain//2) <= (jumlah_pita//1.3):
            jumlah_l += int(jumlah_kain//2)
            jumlah_kain = jumlah_kain%2
            jumlah_pita = jumlah_pita%2
        else:
            jumlah_l += int(jumlah_kain//1.3)
            jumlah_kain = jumlah_kain%1.3
            jumlah_pita = jumlah_pita%1.3
    
    # Ukuran M (Jika Masih Ada Sisa)
    if jumlah_kain>=1.5 and jumlah_pita>=1:
        # Ambil minimum antara kain dan pita
        if (jumlah_kain//1.5) <= (jumlah_pita//1):
            jumlah_m += int(jumlah_kain//1.5)
            jumlah_kain = jumlah_kain%1.5
            jumlah_pita = jumlah_pita%1.5
        else:
            jumlah_m += int(jumlah_kain//1)
            jumlah_kain = jumlah_kain%1
            jumlah_pita = jumlah_pita%1
    
    # Ukuran L (Jika Masih Ada Sisa)
    if jumlah_kain>=1.2 and jumlah_pita>=0.8:
        # Ambil minimum antara kain dan pita
        if (jumlah_kain//1.2) <= (jumlah_pita//0.8):
            jumlah_s += int(jumlah_kain//1.2)
            jumlah_kain = jumlah_kain%1.2
            jumlah_pita = jumlah_pita%1.2
        else:
            jumlah_s += int(jumlah_kain//0.8)
            jumlah_kain = jumlah_kain%0.8
            jumlah_pita = jumlah_pita%0.8

    print(f"Nona Deb dapat membuat {jumlah_s} ukuran S, {jumlah_m} ukuran M, {jumlah_l} ukuran L.")