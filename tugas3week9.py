from array import array

data_integer = array('i', [3, 6, 9, 12, 15])

panjang_array = len(data_integer)
print(f"Banyaknya elemen dalam array adalah {panjang_array}")

total_array = 0
for a in data_integer:
    total_array += a
print(f"Jumlah total semua elemen adalah {total_array}")

average_array = total_array / len(data_integer)
print(f"Rata-rata elemen array adalah {average_array}")
