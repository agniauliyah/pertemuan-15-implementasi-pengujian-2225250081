
# Proposal Project
## Program Analisis Nilai Matematika

### 1. Latar Belakang

Pengolahan nilai merupakan salah satu kegiatan yang dilakukan untuk mengetahui hasil belajar siswa. Proses pengolahan nilai secara manual membutuhkan waktu dan berisiko terjadi kesalahan dalam perhitungan.

Oleh karena itu, dibuatlah Program Analisis Nilai Matematika menggunakan bahasa pemrograman Python. Program ini diharapkan dapat membantu proses pengolahan dan analisis nilai siswa secara sederhana, cepat, dan tepat.

### 2. Tujuan

Tujuan pembuatan program ini adalah:
1. Mengolah data nilai siswa menggunakan Python.
2. Menghitung rata-rata nilai siswa.
3. Menentukan nilai tertinggi dan nilai terendah.
4. Menghitung jumlah siswa yang lulus dan tidak lulus.
5. Menerapkan konsep implementasi program dan pengujian perangkat lunak.

### 3. Deskripsi Program

Program Analisis Nilai Matematika merupakan aplikasi berbasis terminal yang digunakan untuk membaca data nilai siswa dari file, menampilkan data, melakukan analisis nilai, dan menyimpan hasil analisis ke dalam file.

Data siswa terdiri atas nama dan nilai. Batas kelulusan yang digunakan adalah 60.

### 4. Fitur Program

Fitur yang terdapat dalam program ini meliputi:
- Membaca data nilai siswa dari file.
- Menampilkan data nilai siswa.
- Menghitung rata-rata nilai.
- Menentukan nilai tertinggi dan terendah.
- Menghitung jumlah siswa lulus dan tidak lulus.
- Menentukan predikat nilai.
- Memvalidasi nilai.
- Menyimpan hasil analisis ke dalam file.
- Menangani data yang tidak valid dan file yang tidak ditemukan.

### 5. Teknologi yang Digunakan

- Bahasa pemrograman: Python
- Editor kode: Visual Studio Code
- Pengelolaan versi: Git dan GitHub
- Pengujian: Pengujian fungsional menggunakan test case

### 6. Struktur Project

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
└── proposal.md
```

### 7. Rencana Pengujian

Pengujian dilakukan untuk memastikan setiap fitur program berjalan sesuai dengan yang diharapkan. Pengujian mencakup:
1. Pengujian pembacaan data.
2. Pengujian perhitungan rata-rata.
3. Pengujian nilai tertinggi dan terendah.
4. Pengujian batas kelulusan.
5. Pengujian data kosong.
6. Pengujian input bukan angka.
7. Pengujian nilai di luar rentang 0–100.
8. Pengujian file yang tidak ditemukan.

### 8. Penutup

Program Analisis Nilai Matematika dibuat sebagai penerapan konsep pemrograman Python dalam pengolahan data. Melalui project ini, diharapkan dapat meningkatkan pemahaman mengenai penggunaan fungsi, pengolahan file, validasi data, serta implementasi dan pengujian program.