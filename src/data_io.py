
def baca_data_nilai(nama_file):
    data_nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if baris == "":
                    continue

                bagian = baris.split(",")

                if len(bagian) != 2:
                    print("Format data tidak valid.")
                    continue

                nama = bagian[0].strip()

                try:
                    nilai = float(bagian[1].strip())
                except ValueError:
                    print("Nilai harus berupa angka.")
                    continue

                data_nilai.append({
                    "nama": nama,
                    "nilai": nilai
                })

    except FileNotFoundError:
        print("File tidak ditemukan.")

    return data_nilai


def simpan_hasil(nama_file, hasil):
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write(hasil)

        print("Hasil analisis berhasil disimpan.")

    except OSError:
        print("Hasil analisis gagal disimpan.")