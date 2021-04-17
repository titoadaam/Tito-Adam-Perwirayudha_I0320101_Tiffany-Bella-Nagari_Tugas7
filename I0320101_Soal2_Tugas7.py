import math

nilai_siswa = input("Input nilai siswa (dipisahkan dengan spasi) : ").split()
for i in range(len(nilai_siswa)):
    nilai_siswa[i] = int(nilai_siswa[i])
rerata = sum(nilai_siswa)/len(nilai_siswa)
print("Nilai yang diinput : ", nilai_siswa)
print('='*30)
print("Nilai yang paling tinggi ", max(nilai_siswa))
print("Nilai yang paling rendah ", min(nilai_siswa))
print("Rata-rata nilai siswa ", rerata)
print("Rata-rata nilai dengan pembulatan ke atas ", math.ceil(rerata))
print("Rata-rata nilai dengan pembulatan ke bawah  ", math.floor(rerata))
