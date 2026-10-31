def hitung_rata_rata(data_siswa):
    """Menghitung rata-rata nilai seluruh siswa."""
    if not data_siswa:
        return 0

    total_nilai = sum(siswa["nilai"] for siswa in data_siswa)
    return total_nilai / len(data_siswa)


def nilai_tertinggi(data_siswa):
    """Menentukan nilai tertinggi."""
    if not data_siswa:
        return 0

    return max(siswa["nilai"] for siswa in data_siswa)


def nilai_terendah(data_siswa):
    """Menentukan nilai terendah."""
    if not data_siswa:
        return 0

    return min(siswa["nilai"] for siswa in data_siswa)


def jumlah_siswa_lulus(data_siswa, batas_lulus=60):
    """Menghitung jumlah siswa yang lulus."""
    return sum(
        1
        for siswa in data_siswa
        if siswa["nilai"] >= batas_lulus
    )