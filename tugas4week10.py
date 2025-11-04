nilai = [
[85, 88, 90],
[78, 82, 88],
[92, 98, 94],
[70, 68, 72],
[88, 85, 84],
[60, 75, 70],
[95, 92, 98],
[74, 78, 76],
[81, 85, 83],
[69, 72, 70],
[90, 88, 92],
[76, 88, 79],
[84, 86, 90],
[79, 82, 85],
[67, 78, 68],
[91, 94, 93],
[73, 78, 75],
[87, 84, 89],
[65, 68, 70],
[93, 98, 95],
[77, 80, 78],
[82, 84, 88],
[89, 85, 90],
[71, 74, 76]
]

for b in range(len(nilai)):
    print(f"Mahasiswa ke-{b+1}:")
    for k in range(len(nilai[b])):
        if k == 0:
            print(f"\tNilai Tugas: {nilai[b][k]}")
        elif k == 1:
            print(f"\tNilai UTS  : {nilai[b][k]}")
        elif k == 2:
            print(f"\tNilai UAS  : {nilai[b][k]}")
    print()
    
import numpy as np

nilai = [
[85, 88, 90],
[78, 82, 88],
[92, 98, 94],
[70, 68, 72],
[88, 85, 84],
[60, 75, 70],
[95, 92, 98],
[74, 78, 76],
[81, 85, 83],
[69, 72, 70],
[90, 88, 92],
[76, 88, 79],
[84, 86, 90],
[79, 82, 85],
[67, 78, 68],
[91, 94, 93],
[73, 78, 75],
[87, 84, 89],
[65, 68, 70],
[93, 98, 95],
[77, 80, 78],
[82, 84, 88],
[89, 85, 90],
[71, 74, 76]
]

nilai_array = np.array(nilai)

rata_rata = np.mean(nilai_array)
nilai_tertinggi = np.max(nilai_array)
nilai_terendah = np.min(nilai_array)

print(f"Rata-rata keseluruhan nilai (np.mean(nilai)): {rata_rata:.2f}")
print(f"Nilai tertinggi (np.max(nilai)): {nilai_tertinggi}")
print(f"Nilai terendah (np.min(nilai)): {nilai_terendah}")