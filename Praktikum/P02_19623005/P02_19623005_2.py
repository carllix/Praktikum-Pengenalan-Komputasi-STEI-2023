# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 5 Oktober 2023
# Deskripsi : Program barisan bilangan Nona Deb sebanyak X dan ketika bertemu kelipatan Y akan menurun hingga mencapai angka 1

# KAMUS
# x, y, current_number, n, k : integer

# ALGORITMA
# Input
x = int(input("Masukkan X: "))
y = int(input("Masukkan Y: "))

# Proses
current_number = 1
n = 1
k = 1

while n<=x:
    if current_number%(y*k)==0:
        k+=1
        while current_number>1 and n<=x:
            n+=1
            print(current_number, end=" ")
            current_number-=1
    else:
        n+=1
        print(current_number, end=" ")
        current_number+=1