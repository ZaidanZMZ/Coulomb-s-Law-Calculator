# Kalkulator Hukum Coulomb


Kalkulator Hukum Coulomb adalah aplikasi web interaktif yang memungkinkan pengguna menghitung gaya elektrostatis antara dua muatan listrik berdasarkan Hukum Coulomb. Aplikasi ini dirancang khusus untuk membantu siswa dan pendidik dalam memahami konsep elektrostatika dengan menyediakan visualisasi interaktif dan solusi langkah demi langkah.

## ✨ Fitur Utama

- **4 Mode Perhitungan**:
  - 🧮 Menghitung gaya elektrostatis (F)
  - ⚡ Menghitung muatan 1 (q₁)
  - ⚡ Menghitung muatan 2 (q₂)
  - 📏 Menghitung jarak antar muatan (r)

- **Visualisasi Interaktif**:
  - 🔴🔵 Representasi visual muatan positif/negatif
  - ↔️ Indikator arah gaya (tarik-menarik atau tolak-menolak)
  - 🎥 Animasi perubahan muatan dan jarak

- **Solusi Langkah Demi Langkah**:
  - 📝 Penjelasan rinci setiap langkah perhitungan
  - 🔢 Format "a × 10^b" untuk bilangan sangat besar/kecil
  - 📊 Hasil akhir dengan konversi satuan otomatis

- **Materi Pembelajaran**:
  - 📚 Penjelasan konsep Hukum Coulomb
  - 📊 Tabel konstanta untuk berbagai medium
  - 🎯 Contoh soal latihan bertingkat kesulitan

- **Antarmuka Modern**:
  - 💻📱 Desain responsif untuk desktop dan mobile
  - 🌙 Mode gelap dengan gradien warna elegan
  - ✨ Animasi dan interaksi halus

## 🛠 Teknologi Yang Digunakan

**Backend**:
- <img src="https://img.icons8.com/color/48/000000/python.png" width="16"/> Python 3
- <img src="https://img.icons8.com/ios/50/000000/flask.png" width="16"/> Flask (Web Framework)
- <img src="https://img.icons8.com/color/48/000000/json.png" width="16"/> JSON (Format Data)

**Frontend**:
- <img src="https://img.icons8.com/color/48/000000/html-5.png" width="16"/> HTML5 (Struktur Halaman)
- <img src="https://img.icons8.com/color/48/000000/css3.png" width="16"/> CSS3 (Tailwind CSS Framework)
- <img src="https://img.icons8.com/color/48/000000/javascript.png" width="16"/> JavaScript (Interaktivitas)
- <img src="https://img.icons8.com/color/48/000000/font-awesome.png" width="16"/> Font Awesome (Ikon)

## 🚀 Cara Menjalankan Aplikasi

### Prasyarat
- Python 3.x
- pip (Python package installer)

### 📥 Langkah-langkah Instalasi

1. Clone repository:
   ```bash
   git clone https://github.com/ZaidanZMZ/Coulomb-s-Law-Calculator.git
   cd Coulomb-s-Law-Calculator
   ```

2. Buat lingkungan virtual (opsional tapi disarankan):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate    # Windows
   ```

3. Install dependensi:
   ```bash
   pip install flask
   ```

4. Jalankan aplikasi:
   ```bash
   python app.py
   ```

5. Buka di browser:
   ```
   http://localhost:5000
   ```

## 📂 Struktur Proyek
```
Coulomb-s-Law-Calculator/
├── app.py                  # Backend Flask
├── templates/
│   └── index.html          # Halaman utama aplikasi
└── README.md               # Dokumentasi proyek
```

## 💡 Contoh Penggunaan

1. **Menghitung Gaya**:
   - Masukkan nilai muatan 1 (misal: 5 μC)
   - Masukkan nilai muatan 2 (misal: -3 μC)
   - Masukkan jarak (misal: 0.1 m)
   - Pilih konstanta Coulomb
   - Klik "Hitung Gaya"

2. **Menghitung Jarak**:
   - Pilih mode "Jarak"
   - Masukkan kedua muatan dan nilai gaya
   - Klik "Hitung Jarak"

3. **Mencoba Contoh Soal**:
   - Scroll ke bagian "Soal Latihan"
   - Pilih salah satu contoh soal
   - Klik "Hitung" untuk mengisi otomatis
   - Lihat solusi langkah demi langkah

## 👥 Kontributor

| Nama |
|------|
| [ ZAIDAN ZAKI MAKSUDI ] |
| [ M IZZA ANURA HAFIDZ ] |
| [ FRANSISKUS XAVERIUS KEVIN SUSANTO ] |
| [ MUHAMMAD RAFLIYANTO NUGROHO ] |
