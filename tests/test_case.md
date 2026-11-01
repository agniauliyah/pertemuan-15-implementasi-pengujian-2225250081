# Dokumentasi Pengujian Program

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan Program Analisis Nilai Matematika berjalan sesuai dengan fungsi yang telah dibuat. Pengujian mencakup kondisi normal, batas, input tidak valid, dan kondisi data kosong.

## 2. Data Pengujian

| No | Nama Mahasiswa | Nilai |
|---|---|---:|
| 1 | Andi | 80 |
| 2 | Budi | 70 |
| 3 | Citra | 90 |
| 4 | Dina | 85 |
| 5 | Eka | 75 |

## 3. Test Case

| ID | Fitur | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Membaca data nilai | File berisi 5 data mahasiswa | 5 data berhasil dibaca | 5 data berhasil dibaca | PASS |
| TC02 | Menghitung rata-rata | 80, 70, 90, 85, 75 | Rata-rata 80.00 | Rata-rata 80.00 | PASS |
| TC03 | Nilai tertinggi | 80, 70, 90, 85, 75 | Nilai tertinggi 90 | Nilai tertinggi 90.0 | PASS |
| TC04 | Nilai terendah | 80, 70, 90, 85, 75 | Nilai terendah 70 | Nilai terendah 70.0 | PASS |
| TC05 | Kelulusan normal | Nilai 70 | Lulus | Lulus | PASS |
| TC06 | Batas kelulusan | Nilai 60 | Lulus | Belum diuji | Belum diuji |
| TC07 | Data kosong | List kosong | Rata-rata, tertinggi, dan terendah menghasilkan 0 | Belum diuji | Belum diuji |
| TC08 | Input bukan angka | Nilai "abc" | Pesan kesalahan yang jelas | Belum diuji | Belum diuji |
| TC09 | Nilai di luar rentang | Nilai 110 | Nilai ditolak oleh validasi | Belum diuji | Belum diuji |
| TC10 | File tidak ditemukan | Nama file yang tidak tersedia | Pesan file tidak ditemukan | Belum diuji | Belum diuji |

## 4. Kesimpulan

Pengujian awal menunjukkan bahwa fitur utama Program Analisis Nilai Matematika telah berjalan sesuai hasil yang diharapkan. Pengujian kondisi batas, input tidak valid, dan kondisi khusus dilanjutkan untuk memastikan program lebih andal.