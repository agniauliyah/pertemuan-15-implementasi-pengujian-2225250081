
# Program Analisis Nilai Matematika

## Deskripsi Project

Program Analisis Nilai Matematika merupakan aplikasi berbasis terminal yang dibuat menggunakan bahasa pemrograman Python. Program ini digunakan untuk membaca, mengolah, dan menganalisis data nilai siswa secara sederhana.

Project ini dibuat sebagai penerapan materi implementasi dan pengujian program pada mata kuliah Algoritma dan Pemrograman.

## Tujuan

- Mengolah data nilai siswa menggunakan Python.
- Menghitung rata-rata nilai.
- Menentukan nilai tertinggi dan terendah.
- Menghitung jumlah siswa yang lulus dan tidak lulus.
- Menerapkan validasi data dan pengolahan file.
- Melakukan pengujian terhadap fitur program.

## Fitur Program

1. Membaca data nilai siswa dari file.
2. Menampilkan data nilai siswa.
3. Menghitung rata-rata nilai.
4. Menentukan nilai tertinggi dan terendah.
5. Menghitung jumlah siswa lulus dan tidak lulus.
6. Menentukan predikat nilai.
7. Memvalidasi nilai.
8. Menyimpan hasil analisis ke dalam file.
9. Menangani data tidak valid dan file yang tidak ditemukan.

## Teknologi yang Digunakan

- Python
- Visual Studio Code
- Git
- GitHub

## Struktur Project

```text
pertemuan-15-implementasi-pengujian-2225250081/
├── data/
│   └── contoh_data.txt
├── output/
│   └── hasil_analisis.txt
├── src/
│   ├── __init__.py
│   ├── analisis.py
│   ├── data_io.py
│   ├── main.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
├── docs/
├── .gitignore
├── proposal.md
└── README.md
```

## Contoh Data

Data nilai siswa disimpan dalam file `data/contoh_data.txt`.

```text
Andi,80
Budi,70
Citra,90
Dina,85
Eka,75
```

Format data terdiri dari nama siswa dan nilai yang dipisahkan dengan tanda koma.

## Cara Menjalankan Program

1. Buka folder project di Visual Studio Code.
2. Buka terminal pada folder utama project.
3. Jalankan perintah berikut:

```powershell
py src/main.py
```

4. Pilih menu yang tersedia pada program.