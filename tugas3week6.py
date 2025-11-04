set_A = {20, 30, 40, 50, 60}
set_B = {25, 30, 35, 40, 45}
set_C = {30, 40, 50, 70, 80}
set_D = {40, 50, 60, 90, 100}

irisan_1 = set_A & set_C & set_D
print(irisan_1)

gabungan = set_A | set_B
selisih = gabungan - set_D
print(selisih)

gabungan_set_A_dan_set_B = set_A | set_B
gabungan_set_C_dan_set_D = set_C | set_D
irisan_2 = gabungan_set_A_dan_set_B & gabungan_set_C_dan_set_D
print(irisan_2)

selisih_simetris = set_B ^ set_C
print(selisih_simetris)