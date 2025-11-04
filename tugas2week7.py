stok_buku = {
"Harry Potter" : 10,
"Laskar Pelangi" : 15,
"Bumi Manusia" : 7,
"Dilan 1990" : 20,
}

for judul, jumlah in stok_buku.items():
    print(f"Buku : {judul} - Stok {jumlah}")

    stok_buku = {
"Harry Potter" : 10,
"Laskar Pelangi" : 15,
"Bumi Manusia" : 7,
"Dilan 1990" : 20,
}

for judul, jumlah in stok_buku.items():
    print(f"Buku : {judul} - Stok {jumlah}")

judul_baru = input("Masukkan judul buku:")
jumlah = int(input("Masukkan stok awal:"))
stok_buku[judul_baru] = jumlah
print(f"Buku {judul_baru} telah ditambahkan dengan stok {jumlah}")
print("Semua data buku:", stok_buku.items())