# NIM/Nama: 19623005/Carlo Angkisan
# Tanggal: 13 September 2023
# Deskripsi: Program Menentukan Kelas dan Harga Tiket Tuan Kil

# KAMUS
# nomor : integer
# posisi : string
# ada_kursi : boolean
# jenis : string
# harga : string

# ALGORITMA

# Input
nomor = int(input("Tentukan Nomor Kursi: "))
posisi = input("Tentukan Posisi Kursi: ")

# Proses
if (nomor>=1 and nomor<=20) or (nomor>=51 and nomor<=60):
    ada_kursi = True
    jenis = "Hot Seat"
    if posisi=="A" or posisi=="a" or posisi=="F" or posisi=="f":
        harga = "1600000"
    elif posisi=="B" or posisi=="b" or posisi=="E" or posisi=="e":
        harga = "1550000"
    elif posisi=="C" or posisi=="c" or posisi=="D" or posisi=="d":
        harga = "1500000"
    else:
        ada_kursi = False
elif (nomor>=21 and nomor<=50) or (nomor>=61 and nomor<=100):
    ada_kursi = True
    jenis = "Regular"
    if posisi=="A" or posisi=="a" or posisi=="F" or posisi=="f":
        harga = "1000000"
    elif posisi=="B" or posisi=="b" or posisi=="E" or posisi=="e":
        harga = "950000"
    elif posisi=="C" or posisi=="c" or posisi=="D" or posisi=="d":
        harga = "900000"
    else:
        ada_kursi = False
else: # nomor<1 or nomor>100
    ada_kursi = False

if ada_kursi == False:
    print("Kursi tidak tersedia.")
else: # ada_kursi == True
    print(f"Tuan Kil memilih kursi {jenis} dengan harga {harga}.")