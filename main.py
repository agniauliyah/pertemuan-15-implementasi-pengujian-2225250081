from src.analisis import (
    hitung_rata_rata,
    nilai_tertinggi,
    nilai_terendah,
    jumlah_siswa_lulus
)

from src.data_io import simpan_data, baca_data
from src.utilitas import input_nama, input_nilai


data_siswa = baca_data()


def tambah_data():
    """Menambahkan data siswa."""
    print("\n=== TAMBAH DATA SISWA ===")

    nama = input_nama()
    nilai = input_nilai()

    data_siswa.append({
        "nama": nama,
        "nilai": nilai
    })

    simpan_data(data_siswa)
    print("Data siswa berhasil ditambahkan!")


def tampilkan_data():
    """Menampilkan seluruh data siswa."""
    print("\n=== DATA NILAI SISWA ===")

    if not data_siswa:
        print("Belum ada data siswa.")
        return

    for nomor, siswa in enumerate(data_siswa, start=1):
        print(f"{nomor}. {siswa['nama']} - Nilai: {siswa['nilai']}")


def tampilkan_analisis():
    """Menampilkan hasil analisis nilai."""
    print("\n=== ANALISIS NILAI SISWA ===")

    if not data_siswa:
        print("Belum ada data untuk dianalisis.")
        return

    rata_rata = hitung_rata_rata(data_siswa)
    tertinggi = nilai_tertinggi(data_siswa)
    terendah = nilai_terendah(data_siswa)
    jumlah_lulus = jumlah_siswa_lulus(data_siswa)

    print(f"Jumlah siswa             : {len(data_siswa)}")
    print(f"Rata-rata nilai          : {rata_rata:.2f}")
    print(f"Nilai tertinggi          : {tertinggi}")
    print(f"Nilai terendah           : {terendah}")
    print(f"Jumlah siswa lulus       : {jumlah_lulus}")
    print(f"Jumlah siswa tidak lulus : {len(data_siswa) - jumlah_lulus}")


def menu_utama():
    """Menampilkan menu utama program."""
    while True:
        print("\n===== PROGRAM REKAP NILAI MATEMATIKA =====")
        print("1. Tambah Data Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Analisis Nilai")
        print("4. Simpan Data")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            tampilkan_analisis()
        elif pilihan == "4":
            simpan_data(data_siswa)
            print("Data berhasil disimpan!")
        elif pilihan == "5":
            simpan_data(data_siswa)
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-5.")


if __name__ == "__main__":
    menu_utama()