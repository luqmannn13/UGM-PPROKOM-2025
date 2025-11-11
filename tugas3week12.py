daftar_mahasiswa = []

def tambah_data(nama, nim):
    mahasiswa = {
        "nama": nama,
        "nim": nim
    }
    daftar_mahasiswa.append(mahasiswa)
    print(f"Data mahasiswa {nama} berhasil ditambahkan.")

def tampilkan_data():
    if not daftar_mahasiswa:
        print("Belum ada data mahasiswa.")
        return
    print("\n=== Daftar Mahasiswa ===")
    for no, mhs in enumerate(daftar_mahasiswa, start=1):
        print(f"{no}. Nama: {mhs['nama']}, NIM: {mhs['nim']}")

import data_mhs

while True:
    print("=== Menu Data Mahasiswa ===")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM : ")
        data_mhs.tambah_data(nama, nim)
        print("Data berhasil ditambahkan!\n")

    elif pilihan == "2":
        data_mhs.tampilkan_data()

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.\n")
