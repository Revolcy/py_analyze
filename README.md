# 🚲 Bike Sharing Data Dashboard

Dashboard interaktif berbasis **Streamlit** untuk menganalisis data penyewaan sepeda (_Bike Sharing_).  
Proyek ini menampilkan tren penyewaan berdasarkan waktu, cuaca, suhu, musim, serta analisis lanjutan berupa **manual grouping** berdasarkan suhu dan tingkat penggunaan.

---

## 📊 Fitur Dashboard

1. **Statistik Umum**  
   Menampilkan total penyewaan, rata-rata harian, dan suhu rata-rata berdasarkan tahun yang dipilih.

2. **Tren Penyewaan per Bulan**  
   Visualisasi _line chart_ untuk melihat perubahan rata-rata penyewaan sepeda tiap bulan.

3. **Korelasi Faktor Lingkungan**  
   _Heatmap_ yang menunjukkan hubungan antara suhu, kelembapan, kecepatan angin, dan jumlah penyewaan.

4. **Pengaruh Musim dan Cuaca**  
   Analisis rata-rata penyewaan berdasarkan musim dan kondisi cuaca.

5. **Analisis Lanjutan (Manual Grouping)**  
   Pengelompokan data berdasarkan kategori suhu (Dingin, Sejuk, Hangat, Panas) dan tingkat penggunaan (Rendah, Sedang, Tinggi).

---

## 🧠 Insight Utama

- **Suhu** memiliki pengaruh paling kuat terhadap jumlah penyewaan sepeda.
- Aktivitas penyewaan meningkat pada **musim panas** dan **cuaca cerah**.
- Penyewaan cenderung rendah pada **musim dingin** dan **cuaca buruk (hujan/lebat)**.
- **Rekomendasi:** tambah armada saat musim panas dan adakan promosi pada musim hujan.

---

## ⚙️ Cara Menjalankan di Lokal

### 1️⃣ Clone Repository

Pastikan kamu sudah memiliki **Python 3.9+** dan **pip**.

```bash
git clone https://github.com/Revolcy/py_analyze.git
cd py_analyze
```

### 2️⃣ Buat Virtual Environment

```bash
python -m venv env
```

### 3️⃣ Aktifkan environment:

Windows :

```bash
venv\Scripts\activate
```

Linux/MacOS :

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependensi

```bash
pip install -r requirements.txt
```

### 5️⃣ Menjalankan Dashboard

```bash
streamlit run dashboard/dashboard.py
```
