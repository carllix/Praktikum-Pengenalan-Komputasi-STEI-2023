# NIM/Nama: 19623005/Carlo Angkisan
# Tanggal: 13 September 2023
# Deskripsi: Program Menentukan Kelulusan Tuan Kil

# KAMUS
# ujian1 : float
# ujian2 : float
# ujian3 : float
# ujian4 : float
# rata_rata : float

# ALGORITMA

# Input
ujian1 = float(input("Masukkan niali ujian 1: "))
ujian2 = float(input("Masukkan niali ujian 2: "))
ujian3 = float(input("Masukkan niali ujian 3: "))
ujian4 = float(input("Masukkan niali ujian 4: "))

# Proses
rata_rata = (ujian1+ujian2+ujian3+ujian4)/4

if (ujian1 or ujian2 or ujian3 or ujian4) < 0 or (ujian1 or ujian2 or ujian3 or ujian4) > 100:
    print("Nilai yang dimasukan tidak valid")
else: # (ujian1 or ujian2 or ujian3 or ujian4) >= 0 and (ujian1 or ujian2 or ujian3 or ujian4) <= 100:
    if (ujian1 or ujian2 or ujian3 or ujian4) < 50:
        print("Tuan Kil tidak lulus kelas Tuan Leo.")
    else: # (ujian1 or ujian2 or ujian3 or ujian4) >= 50
        if rata_rata >= 70:
            print("Tuan Kil lulus kelas Tuan Leo.")
        else: # rata_rata < 70
            print("Tuan Kil tidak lulus kelas Tuan Leo.")
    

