# ALAT PENGHITUNG ANGKA GANJIL DAN GENAP

# 1. MEMBUAT FUNGSI DEF
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return f"Angka {angka} Termasuk Bilangan Genap"
    else:
        return f"Angka {angka} Termasuk Bilangan Ganjil"

# 2. PERULANGAN UTAMA
while True:
    print("\n=== PENGECEKAN GANJIL / GENAP ===")
    print("Ketik 'q' untuk keluar dari program.")

    X = input("Masukkan Angka : ")

    # Tombol keluar
    if X.lower() == "q":
        print("Program selesai. Terima kasih!")
        break

    # Memastikan input berupa angka
    try:
        X = int(X)

        # MEMANGGIL FUNGSI DEF UNTUK LOGIKA PENGHITUNGAN
        hasil = cek_ganjil_genap(X)
        print(hasil)

    except ValueError:
        print("Input tidak valid! Masukkan angka atau 'q' untuk keluar.")
