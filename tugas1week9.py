A = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print("Elemen lapisan pertama:", A[0:1])

A = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print("Elemen kolom terakhir dari setiap baris dan lapisan:")
print("Lapisan 0, Baris 0 ->", A[0][0][2])
print("Lapisan 0, Baris 1 ->", A[0][1][2])
print("Lapisan 1, Baris 0 ->", A[1][0][2])
print("Lapisan 1, Baris 1 ->", A[1][1][2])
