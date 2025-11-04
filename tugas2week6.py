nilai = set({3, 6, 9, 2, 5, 7})
nilai_baru = {1, 4, 8, 10}
nilai.update(nilai_baru)
print(nilai)

nilai = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
nilai.discard(1)
nilai.discard(3)
nilai.discard(4)
nilai.discard(5)
nilai.discard(7)
nilai.discard(8)
nilai.discard(10)
print(nilai)