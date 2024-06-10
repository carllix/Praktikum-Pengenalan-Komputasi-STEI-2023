# NIM/Nama : 19623005/Carlo Angkisan
# Tanggal : 19 Oktober 2023
# Deskripsi : Program menentukan banyak potongan list dengan total bilangan merupakan bilangan prima

# KAMUS
# n,current_sum : int
# i, j : int
# is_prime : boolean
# arr_num : array [0...n-1] of int

# ALGORITMA
n = int(input("Masukkan nilai N: "))
arr_num = [int(input(f"Masukkan bilangan ke {i + 1}: ")) for i in range(n)]

count = 0

for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += arr_num[j]

        # Cek apakah current_sum adalah bilangan prima
        if current_sum > 1:
            is_prime = True
            for k in range(2, current_sum):
                if (current_sum % k) == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1

if count==0:
    print("Tidak ada potongan list yang jumlahnya prima.")
else:
    print(f"Terdapat {count} potongan list yang jumlahnya prima.")