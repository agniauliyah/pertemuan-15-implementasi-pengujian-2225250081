
def tentukan_predikat(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"


def tentukan_status(nilai, batas_kelulusan=60):
    if nilai >= batas_kelulusan:
        return "Lulus"
    else:
        return "Tidak Lulus"


def validasi_nilai(nilai):
    return 0 <= nilai <= 100
