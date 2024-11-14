# devops-JLV

## Introduction

Repository ini digunakan dalam **Project DevOps Semester 7** baik untuk proyek UTS maupun UAS. Perhatian : Repository ini akan ada banyak perubahan dari segi ide maupun desain sesuai dengan diskusi antar anggota. Dengan demikian, terima kasih. 

### Planning Phase
(19/10/2024) Setelah diskusi melalui media sosial, tim kita memutuskan untuk menggabungkan ide proyek dari kelas Deep Learning bertema "Deteksi Tingkat Kematangan Buah Mangga", lalu diimplementasikan ke website dengan framework Flask, yang mana framework tersebut berbasis Python yang memudahkan implemetasi selagi semester ini berfokus pada bahasa Python. Repository ini akan dibentuk tiga branches yang masing-masing untuk setiap anggota yang mana setiap update akan di-push ke branch dengan nama anggota sendiri. 

*Perhatian : Ide planning dapat berubah setiap saat ada kondisi yang perlu dipenuhi atau kehendak dari anggota tim.* 

# Aplikasi Pendeteksi Tingkat Kematangan Buah Mangga

Proyek ini adalah aplikasi untuk mendeteksi tingkat kematangan buah mangga menggunakan model pembelajaran mesin. Aplikasi ini dikembangkan dengan Flask sebagai framework web dan menggunakan dataset gambar yang dikelompokkan berdasarkan tingkat kematangan untuk melatih model.

## Struktur Proyek

```
.
├── Aplikasi Pendeteksi Tingkat Kematangan Buah Mangga
│   ├── app.py                # Script utama aplikasi Flask
│   ├── static/               # Folder untuk file statis (CSS, JavaScript, dll.)
│   ├── templates/            # Folder untuk template HTML
│   └── README.md             # Dokumentasi proyek (README ini)
└── Dataset Proyek
    ├── train/                # Dataset untuk pelatihan model
    ├── test/                 # Dataset untuk pengujian model
    └── valid/                # Dataset untuk validasi model
```

## Dataset

Dataset berisi gambar buah mangga yang telah diklasifikasikan berdasarkan tingkat kematangan. Dataset terbagi menjadi tiga bagian utama:
- **train**: Gambar untuk melatih model.
- **test**: Gambar untuk menguji model setelah pelatihan.
- **valid**: Gambar untuk memvalidasi kinerja model.

> **Catatan**: Pastikan dataset ini tersedia dalam struktur folder yang sama agar proses pelatihan model dapat berjalan dengan baik.

## Instalasi

1. **Clone repository** ini dan masuk ke direktori proyek:

   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. **Install dependencies** yang diperlukan:

   Pastikan Anda memiliki Python 3.x, kemudian instal pustaka yang dibutuhkan:

   ```bash
   pip install -r requirements.txt
   ```

   Jika tidak ada `requirements.txt`, berikut pustaka utama yang mungkin dibutuhkan:

   ```bash
   pip install Flask tensorflow numpy pandas
   ```

3. **Jalankan aplikasi**:

   Setelah semua dependensi terpasang, jalankan aplikasi dengan perintah berikut:

   ```bash
   python app.py
   ```

   Aplikasi akan berjalan di `http://127.0.0.1:5000/` dan dapat diakses melalui browser.

## Penggunaan

1. **Upload Gambar**: Pada halaman utama aplikasi, pengguna dapat mengunggah gambar buah mangga.
2. **Prediksi Tingkat Kematangan**: Aplikasi akan memproses gambar dan menampilkan hasil prediksi tingkat kematangan buah mangga.

## Pengembangan dan Pelatihan Model

Jika Anda ingin mengembangkan model atau melatih ulang, pastikan dataset berada dalam struktur folder yang sesuai (`train`, `test`, `valid`). Model ini kemungkinan menggunakan CNN (Convolutional Neural Network) untuk klasifikasi gambar.

## Kontribusi

Kontribusi sangat terbuka! Silakan fork repository ini, buat perubahan, dan kirimkan *pull request*. Pastikan untuk menulis dokumentasi yang jelas dan mengikuti panduan kode yang ada.

## Lisensi

Proyek ini dilisensikan di bawah lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.
