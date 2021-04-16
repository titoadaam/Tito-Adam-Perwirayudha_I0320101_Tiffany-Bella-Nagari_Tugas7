nilai_siswa = input("Masukkan nilai siswa (dipisahkan dengan spasi) : ").split()

#Konversi menjadi tipe int
for i in range(len(nilai_siswa)):
    nilai_siswa[i] = int(nilai_siswa[i])

#Mencari rata-rata nilai
rerata = sum(nilai_siswa)/len(nilai_siswa)

print("Nilai yang diinput : ", nilai_siswa)
print('='*30)

import math
#Fungsi Numerik 1 = mencari nilai tertinggi
print("Nilai yang paling tinggi adalah ", max(nilai_siswa))

#Fungsi Numerik 2 = mencari nilai terendah
print("Nilai yang paling rendah adalah ", min(nilai_siswa))

print("Rata-rata nilai siswa adalah ", rerata)

#Fungsi Numerik 3 = pembulatan ke atas
print("Rata-rata nilai dengan pembulatan ke atas adalah ", math.ceil(rerata))

#Fungsi Numerik 4 = pembulatan ke bawah
print("Rata-rata nilai dengan pembulatan ke bawah adalah ", math.floor(rerata))
