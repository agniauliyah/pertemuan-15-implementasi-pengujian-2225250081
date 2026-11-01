
from analisis import (
    hitung_rata_rata,
    cari_nilai_tertinggi,
    cari_nilai_terendah,
    hitung_jumlah_lulus,
    hitung_jumlah_tidak_lulus
)

from data_io import baca_data_nilai, simpan_hasil

from utilitas import (
    tentukan_predikat,
    tentukan_status,
    validasi_nilai
)


# Menampilkan data nilai mahasiswa
def tampilkan_data(data):
    if len(data) == 0:
        print("Belum ada data nilai.")
        return

    print("\nDAFTAR NILAI MAHASISWA")

    for siswa in data:
        nama = siswa["nama"]
        nilai = siswa["nilai"]

        print(
            f"Nama: {nama} | "
            f"Nilai: {nilai} | "
            f"Predikat: {tentukan_predikat(nilai)} | "
            f"Status: {tentukan_status(nilai)}"
        )


# Melakukan analisis data nilai
def analisis_data(data):
    if len(data) == 0:
        print("Tidak ada data yang dapat dianalisis.")
        return

    daftar_nilai = []

    for siswa in data:
        nilai = siswa["nilai"]

        if validasi_nilai(nilai):
            daftar_nilai.append(nilai)
        else:
            print(f"Nilai {nilai} tidak valid.")

    if len(daftar_nilai) == 0:
        print("Tidak ada nilai valid.")
        return

    rata_rata = hitung_rata_rata(daftar_nilai)
    tertinggi = cari_nilai_tertinggi(daftar_nilai)
    terendah = cari_nilai_terendah(daftar_nilai)
    jumlah_lulus = hitung_jumlah_lulus(daftar_nilai)
    jumlah_tidak_lulus = hitung_jumlah_tidak_lulus(daftar_nilai)

    hasil = (
        "HASIL ANALISIS NILAI MATEMATIKA\n"
        "================================\n"
        f"Jumlah data valid: {len(daftar_nilai)}\n"
        f"Rata-rata nilai: {rata_rata:.2f}\n"
        f"Nilai tertinggi: {tertinggi}\n"
        f"Nilai terendah: {terendah}\n"
        f"Jumlah lulus: {jumlah_lulus}\n"
        f"Jumlah tidak lulus: {jumlah_tidak_lulus}\n"
    )

    print("\n" + hasil)

    simpan_hasil("output/hasil_analisis.txt", hasil)


# Menu utama program
def main():
    data = []

    while True:
        print("\n===== PROGRAM ANALISIS NILAI MATEMATIKA =====")
        print("1. Baca data nilai")
        print("2. Tampilkan data nilai")
        print("3. Analisis nilai")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            data = baca_data_nilai("data/contoh_data.txt")

            if len(data) > 0:
                print("Data nilai berhasil dibaca.")
            else:
                print("Data nilai kosong atau tidak berhasil dibaca.")

        elif pilihan == "2":
            tampilkan_data(data)

        elif pilihan == "3":
            analisis_data(data)

        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1-4.")


if __name__ == "__main__":
    main()
