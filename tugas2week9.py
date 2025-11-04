n = 4
Matriks_Identitas = [[1 if b == k else 0 for k in range(n)] for b in range(n)]
print(Matriks_Identitas)

n = int(input("Masukkan ukuran (bilangan bulat positif) untuk matriks identitas (n x n): "))

Matriks_Identitas = [[1 if b == k else 0 for k in range(n)] for b in range(n)]

print(f"Matriks Identitas berukuran {n} x {n} adalah:")
for b in Matriks_Identitas:
    print(b)