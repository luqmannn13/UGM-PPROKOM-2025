daftar_produk = {
    "Bola Futsal": 150000,
    "Jersey Original": 300000,
    "Sepatu Futsal": 250000,
    "Sarung Tangan Kiper": 90000,
    "Kaos Kaki Futsal": 20000,
    "Rompi Latihan": 15000
}

def tampilkan_produk():
    """Menampilkan daftar produk dan harga."""
    print("=== Daftar Produk Peralatan Sepak Bola ===")
    for nama, harga in daftar_produk.items():
        print(f"- {nama}: Rp{harga}")
    print()

def hitung_total(harga, jumlah):
    """Menghitung total harga sebelum diskon."""
    return harga * jumlah

def hitung_diskon(total):
    """Menghitung diskon berdasarkan total belanja."""
    if total >= 50000:
        return total * 0.10   # Diskon 10%
    elif total >= 20000:
        return total * 0.05   # Diskon 5%
    else:
        return 0
    
import produk
import transaksi

def main():
    produk.tampilkan_produk()

    nama_produk = input("Masukkan nama produk yang ingin dibeli: ").title())
    if nama_produk not in produk.daftar_produk:
        print("Produk tidak tersedia.")
        return

    jumlah = int(input("Masukkan jumlah pembelian: "))

    harga = produk.daftar_produk[nama_produk]
    
    total = transaksi.hitung_total(harga, jumlah)
    diskon = transaksi.hitung_diskon(total)
    total_bayar = total - diskon

    print("\n=== Struk Pembayaran ===")
    print(f"Produk      : {nama_produk}")
    print(f"Jumlah      : {jumlah}")
    print(f"Total Awal  : Rp{int(total)}")
    print(f"Diskon      : Rp{int(diskon)}")
    print(f"Total Bayar : Rp{int(total_bayar)}")
    print("========================")


if __name__ == "__main__":

    main()
