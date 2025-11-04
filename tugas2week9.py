list_nama = []

for i in range(5):
    nama = input("Masukkan nama teman:")
    list_nama.append(nama)

print("Nama dengan indeksnya:")
for i, nama in enumerate(list_nama):
    print(f"Index {i+1}:{nama}")

index_user = int(input("Ingin mengganti nama teman pada indeks ke berapa?"))
index_python = index_user - 1

if index_python in range(len(list_nama)):
    nama_baru = input("Masukkan nama teman baru:")
    list_nama[index_python] = nama_baru
else:
    print("indeks tidak valid")

print("Daftar teman yang telah diperbarui:")
for i, nama in enumerate(list_nama):
    print(f"Index {i+1}:{nama}")