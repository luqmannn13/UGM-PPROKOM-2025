#Nama : Luqmanul Faaiq
#NIM : 25/560221/SV/26407

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Tidak bisa dibagi dengan nol"

def pangkat(a, b):
    return a ** b

def akar_kuadrat(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Tidak bisa menghitung akar dari bilangan negatif!"

def show_menu():  # fungsi untuk menampilkan menu
    print("\n")
    print("--------- MENU ---------")
    print("[1] Penjumlahan")
    print("[2] Pengurangan")
    print("[3] Perkalian")
    print("[4] Pembagian")
    print("[5] Perpangkatan")
    print("[6] Akar Kuadrat")
    print("[7] Keluar")
    print("\n")

while True:
    show_menu()  # panggil fungsi dengan ()
    pilihan = input("Pilih salah satu menu: ")

    if pilihan == "7":
        print("Terima kasih telah menggunakan kalkulator!")
        break

    elif pilihan == "6":
        a = float(input("Masukkan angka: "))
        print("Hasil =", akar_kuadrat(a))

    else:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))

        if pilihan == "1":
            print("Hasil =", tambah(a, b))
        elif pilihan == "2":
            print("Hasil =", kurang(a, b))
        elif pilihan == "3":
            print("Hasil =", kali(a, b))
        elif pilihan == "4":
            print("Hasil =", bagi(a, b))
        elif pilihan == "5":
            print("Hasil =", pangkat(a, b))
        else:
            print("Pilihan tidak valid!")
