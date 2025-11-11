def c_to_f(c):
    return (c * 9/5) + 32

def c_to_k(c):
    return c + 273.15

def f_to_c(f):
    return (f - 32) * 5/9

def f_to_k(f):
    return (f - 32) * 5/9 + 273.15

def k_to_c(k):
    return k - 273.15

def k_to_f(k):
    return (k - 273.15) * 9/5 + 32

import konversi_suhu

nilai = float(input("Masukkan nilai suhu: "))
asal = input("Satuan asal (C/F/K): ").upper()
tujuan = input("Satuan tujuan (C/F/K): ").upper()

if asal == 'C':
    if tujuan == 'F':
        hasil = konversi_suhu.c_to_f(nilai)
    elif tujuan == 'K':
        hasil = konversi_suhu.c_to_k(nilai)
    else:
        hasil = nilai
elif asal == 'F':
    if tujuan == 'C':
        hasil = konversi_suhu.f_to_c(nilai)
    elif tujuan == 'K':
        hasil = konversi_suhu.f_to_k(nilai)
    else:
        hasil = nilai
elif asal == 'K':
    if tujuan == 'C':
        hasil = konversi_suhu.k_to_c(nilai)
    elif tujuan == 'F':
        hasil = konversi_suhu.k_to_f(nilai)
    else:
        hasil = nilai

print(f"{nilai}°{asal} = {hasil:.2f}°{tujuan}")
