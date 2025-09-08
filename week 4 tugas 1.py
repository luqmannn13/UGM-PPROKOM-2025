# Program Persyaratan SIM
umur = int(input("Masukkan umur Anda"))
nilai = int(input("Masukkan nilai tes Anda"))
lulus = "Selamat Anda berhak mendapatkan SIM"
gagal = "Maaf, Anda tidak berhak mendapatkan SIM anda\nSilahkan coba lagi bulan depan atau tahun depan" 
if (umur > 17):
    if (nilai < 60):
        print()
        print(gagal)
    else:
        print()
        print(lulus)
else:
        print()
        print(gagal)    