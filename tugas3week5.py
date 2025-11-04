jumlah_nilai = int(input("Masukkan jumlah nilai : "))

total = 0
for i in range(jumlah_nilai):
    nilai = float(input("Masukkan nilai ke-" + str(i + 1) + ": "))
    total += nilai

rata_rata = total / jumlah_nilai
print("rata rata nilainya adalah: ", rata_rata)