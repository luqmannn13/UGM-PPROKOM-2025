import numpy as np

A = np.array([[2,4,6],[1,3,5]])
B = np.array([[1,1,1],[2,2,2]])

Penjumlahan = A + B

print("Hasil penjumlahan matriks adalah:",Penjumlahan)

B_Transpose = B.T
Perkalian = A @ B_Transpose

print("Hasil perkalian kedua matriks:",Perkalian)

