buah_buahan = {
"apel" : 15000,
"jeruk" : 10000,
"anggur" : 25000,
}
print("Harga jeruk adalah:", buah_buahan["jeruk"])
buah_buahan["mangga"] = 12000
print("Daftar harga buah buahan terbaru adalah:", buah_buahan)
buah_buahan["anggur"] = 20000
print("Daftar harga buah buahan terbaru adalah:", buah_buahan)
del buah_buahan["jeruk"]
print("Daftar harga buah buahan terbaru adalah:", buah_buahan)