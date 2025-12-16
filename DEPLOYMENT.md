# Panduan Deployment

## Deployment ke Streamlit Cloud (Recommended)

### Langkah-langkah:

1. **Persiapan Repository**
   - Pastikan semua file sudah committed di GitHub
   - Ini termasuk: `app.py`, `requirements.txt`, `knn_kopi.py`, dan data CSV jika ada

2. **Sign Up di Streamlit Cloud**
   - Kunjungi https://streamlit.io/cloud
   - Login dengan akun GitHub Anda
   - Klik "New app"

3. **Deploy Aplikasi**
   - Pilih repository: `dhafafh/tugas-SPK`
   - Main branch: `main`
   - File path: `app.py`
   - Klik "Deploy"

4. **Akses Aplikasi**
   - Aplikasi akan tersedia di URL seperti: `https://tugas-spk.streamlit.app`

## Menjalankan Lokal di VS Code

### Instalasi dan Setup:

```bash
# Clone repository
git clone https://github.com/dhafafh/tugas-SPK.git
cd tugas-SPK

# Buat virtual environment (optional tapi recommended)
python -m venv venv

# Aktivasi virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Menjalankan Aplikasi:

```bash
streamlit run app.py
```

Aplikasi akan membuka di browser pada `http://localhost:8501`

## Fitur Aplikasi

- **Input Coffee Type & Symptoms**: Pilih jenis kopi dan gejala yang dialami
- **KNN Classification**: Sistem akan merekomendasikan kopi yang aman dikonsumsi
- **Result**: Menampilkan rekomendasi dan penjelasan

## Troubleshooting

### Streamlit Cloud errors:
- Pastikan `requirements.txt` lengkap dengan semua dependencies
- Check bahwa `app.py` tidak menggunakan local file paths yang absolute

### Local errors:
- Pastikan Python 3.7+ sudah terinstall
- Jika ada error import, jalankan `pip install -r requirements.txt` lagi
- Pastikan virtual environment sudah diaktifkan
