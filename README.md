# 🚲 Bike Sharing Data Dashboard

Dashboard interaktif berbasis **Streamlit** untuk menganalisis data penyewaan sepeda.  
Menampilkan tren penyewaan berdasarkan waktu, cuaca, suhu, serta hasil *RFM Analysis* sederhana.

---

## 📊 Fitur Dashboard

1. **Statistik Umum**  
   Menampilkan total penyewaan, rata-rata harian, dan suhu rata-rata berdasarkan tahun.

2. **Tren Penyewaan per Bulan**  
   Visualisasi *line chart* untuk melihat perubahan rata-rata penyewaan sepeda tiap bulan.

3. **Korelasi Faktor Lingkungan**  
   *Heatmap* hubungan antara suhu, kelembapan, kecepatan angin, dan jumlah penyewaan.

4. **Pengaruh Musim dan Cuaca**  
   Analisis rata-rata penyewaan berdasarkan musim dan kondisi cuaca.

5. **RFM Analysis (Recency, Frequency, Monetary)**  
   Visualisasi aktivitas penyewaan berdasarkan dimensi RFM.

---

## 🧠 Insight Utama

- **Temperatur** adalah faktor paling berpengaruh terhadap jumlah penyewaan.  
- Aktivitas penyewaan meningkat pada **musim panas dan cuaca cerah**.  
- **Recency rendah** menunjukkan peningkatan aktivitas terbaru.  
- **Rekomendasi:** tambah sepeda & promosi di musim panas, lakukan maintenance saat musim hujan.

---

## ⚙️ Cara Menjalankan di Lokal

### 1️⃣ Clone repository
```bash
git clone https://github.com/USERNAME/bike-sharing-dashboard.git
cd bike-sharing-dashboard
