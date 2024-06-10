# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 21 September 2023
# Deskripsi : Program Menentukan Pilihan Mata Uang Tuan Kil

# KAMUS
# banyak_peng : integer
# banyak_kom : integer
# konversi_peng : integer
# konversi_kom : integer
# uang_kom : integer
# uang_peng : integer

# ALGORITMA

# Input
banyak_peng = int(input("Banyak uang Peng yang ditawarkan: "))
banyak_kom = int(input("Banyak uang Kom yang ditawarkan: "))
konversi_peng = int(input("Konversi mata uang Peng ke rupiah: "))
konversi_kom = int(input("Konversi mata uang Kom ke rupiah: "))

# Proses
uang_peng = banyak_peng*konversi_peng
uang_kom = banyak_kom*konversi_kom

if uang_peng>uang_kom:
    print("Adik Tuan Kil memilih uang Peng.")
elif uang_peng==uang_kom:
    print("Uang Peng dan Kom sama besar.")
else: #uang_peng<uang_kom
    print("Adik Tuan Kil memilih uang Kom.")