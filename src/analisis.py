def hitung_rata_rata(data_nilai):
    if len(data_nilai) == 0:
        return 0

    total = sum(data_nilai)
    return total / len(data_nilai)


def cari_nilai_tertinggi(data_nilai):
    if len(data_nilai) == 0:
        return 0

    return max(data_nilai)


def cari_nilai_terendah(data_nilai):
    if len(data_nilai) == 0:
        return 0

    return min(data_nilai)


def hitung_jumlah_lulus(data_nilai, batas_kelulusan=60):
    jumlah_lulus = 0

    for nilai in data_nilai:
        if nilai >= batas_kelulusan:
            jumlah_lulus += 1

    return jumlah_lulus


def hitung_jumlah_tidak_lulus(data_nilai, batas_kelulusan=60):
    jumlah_tidak_lulus = 0

    for nilai in data_nilai:
        if nilai < batas_kelulusan:
            jumlah_tidak_lulus += 1

    return jumlah_tidak_lulus