def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Error: Tidak bisa modulo dengan nol"
    return a % b

def pangkat(a, b):
    return a ** b

import aritmatika

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("Hasil Penjumlahan: ", aritmatika.tambah(angka1, angka2))
print("Hasil Pengurangan:", aritmatika.kurang(angka1, angka2))
print("Hasil Perkalian:  ", aritmatika.kali(angka1, angka2))
print("Hasil Pembagian:  ", aritmatika.bagi(angka1, angka2))
print("Hasil Modulo:     ", aritmatika.modulo(angka1, angka2))
print("Hasil Pangkat:    ", aritmatika.pangkat(angka1, angka2))

import aritmatika

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("Hasil Penjumlahan: ", aritmatika.tambah(angka1, angka2))
print("Hasil Pengurangan:", aritmatika.kurang(angka1, angka2))
print("Hasil Perkalian:  ", aritmatika.kali(angka1, angka2))
print("Hasil Pembagian:  ", aritmatika.bagi(angka1, angka2))
print("Hasil Modulo:     ", aritmatika.modulo(angka1, angka2))
print("Hasil Pangkat:    ", aritmatika.pangkat(angka1, angka2))
