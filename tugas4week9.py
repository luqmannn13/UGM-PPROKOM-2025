nilai = [
 [85, 80, 90],
 [78, 82, 88],
 [92, 90, 94],
 [70, 68, 72],
 [88, 85, 84],
 [60, 75, 70],
 [95, 92, 98],
 [74, 70, 76],
 [81, 85, 83],
 [69, 72, 70],
 [90, 88, 92],
 [76, 80, 79],
 [84, 86, 90],
 [79, 82, 85],
 [67, 70, 68],
 [91, 94, 93],
 [73, 78, 75],
 [87, 84, 89],
 [65, 68, 70],
 [93, 90, 95],
 [77, 80, 78],
 [82, 84, 88],
 [89, 85, 90],
 [71, 74, 76]
]

for b in range(len(nilai)): 
    print(f"Mahasiswa ke-{b+1}:")
    for k in range(len(nilai[b])):  
        if k == 0:
            print(f"  Nilai Tugas: {nilai[b][k]}")
        elif k == 1:
            print(f"  Nilai UTS  : {nilai[b][k]}")
        elif k == 2:
            print(f"  Nilai UAS  : {nilai[b][k]}")
    print() 