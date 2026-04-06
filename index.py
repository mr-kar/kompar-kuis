import multiprocessing
import time
import os

def hitung_penjualan(data_kota):
    pid = os.getpid()
    nama_kota = data_kota[0]
    penjualan = data_kota[1]

    print(f"Proses ID {pid} sedang menghitung penjualan Kota {nama_kota}")
    print(f"Data penjualan Kota {nama_kota}: {penjualan}")

    time.sleep(1)  # simulasi proses

    total = sum(penjualan)

    print(f"Total penjualan Kota {nama_kota} = {total}")
    print("-------------------------------------")

    return total


if __name__ == "__main__":
    data_penjualan = [
        ("Bandung", [200000, 150000, 300000]),
        ("Jakarta", [500000, 450000, 400000]),
        ("Surabaya", [300000, 250000, 200000]),
        ("Medan", [150000, 180000, 170000]),
        ("Bali", [220000, 210000, 230000]),
        ("Yogyakarta", [190000, 200000, 210000])
    ]

    print("=== Perhitungan Total Penjualan per Kota (Data Parallelism) ===\n")

    start = time.time()

    with multiprocessing.Pool(processes=3) as pool:
        hasil = pool.map(hitung_penjualan, data_penjualan)

    end = time.time()

    print("\nSemua perhitungan selesai")
    print("Total penjualan semua kota:", hasil)
    print("Waktu eksekusi:", end - start)