import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi tampilan Streamlit
st.set_page_config(page_title="🚲 Bike Sharing Dashboard", layout="wide")

# Judul utama
st.title("🚲 Bike Sharing Data Dashboard")

# Load dataset
df = pd.read_csv('dashboard/main_data.csv')

# --- Perbaikan nilai tahun ---
df['year'] = df['year'].replace({0: 2011, 1: 2012})

# Pastikan kolom tanggal dalam format datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# ================================
# 🔧 SIDEBAR FILTER
# ================================
st.sidebar.header("Filter Data")

# Filter berdasarkan tahun
selected_year = st.sidebar.selectbox("Pilih Tahun:", sorted(df['year'].unique()))

# Filter berdasarkan tanggal (drill down)
st.sidebar.subheader("Filter Tanggal")
min_date = df['dteday'].min()
max_date = df['dteday'].max()

# Handle kalau user pilih cuma satu tanggal
date_input = st.sidebar.date_input(
    "Pilih Rentang Tanggal:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(date_input, tuple):
    start_date, end_date = date_input
else:
    start_date = end_date = date_input

# Konversi tanggal agar kompatibel
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Tambahkan jarak supaya popup kalender tidak ketutupan
st.sidebar.markdown("<br><br>", unsafe_allow_html=True)

# Terapkan filter
filtered_df = df[
    (df['year'] == selected_year) &
    (df['dteday'].between(start_date, end_date))
]

# ================================
# 📊 BAGIAN 1: STATISTIK UMUM
# ================================
st.subheader(f"📊 Statistik Umum Tahun {selected_year}")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", value=int(filtered_df['count'].sum()))
with col2:
    st.metric("Rata-rata Harian", value=round(filtered_df['count'].mean(), 2))
with col3:
    st.metric("Suhu Rata-rata (°C)", value=round(filtered_df['temp'].mean() * 41, 1))

# ================================
# 📅 BAGIAN 2: TREN PENYEWAAN PER BULAN
# ================================
st.subheader("📅 Tren Penyewaan Sepeda per Bulan")

monthly_avg = filtered_df.groupby('month')['count'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='month', y='count', data=monthly_avg, marker='o', color='teal')
plt.title('Rata-rata Penyewaan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Rata-rata Jumlah Sewa')
st.pyplot(fig)

# ================================
# 🌡️ BAGIAN 3: KORELASI FAKTOR LINGKUNGAN
# ================================
st.subheader("🌡️ Korelasi Faktor Lingkungan terhadap Jumlah Penyewaan")

fig, ax = plt.subplots(figsize=(7, 5))
corr = df[['temp', 'humidity', 'windspeed', 'count']].corr()
sns.heatmap(corr, annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('Korelasi Faktor Cuaca dan Jumlah Penyewaan')
st.pyplot(fig)

# ================================
# 🌦️ BAGIAN 4: PENGARUH MUSIM DAN CUACA
# ================================
st.subheader("🌦️ Pengaruh Musim dan Cuaca terhadap Penyewaan")

col4, col5 = st.columns(2)

with col4:
    season_avg = df.groupby('season')['count'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.barplot(x='season', y='count', data=season_avg, color='skyblue')
    plt.title('Rata-rata Penyewaan per Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Rata-rata')
    st.pyplot(fig)

with col5:
    weather_avg = df.groupby('weather')['count'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.barplot(x='weather', y='count', data=weather_avg, color='skyblue')
    plt.title('Rata-rata Penyewaan per Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Rata-rata')
    st.pyplot(fig)

# ================================
# 🔥 BAGIAN 5: ANALISIS LANJUTAN
# ================================
st.subheader("🔥 Analisis Lanjutan: Pengelompokan Berdasarkan Suhu dan Level Penggunaan")

# Kategori suhu
df['temp_category'] = pd.cut(df['temp'] * 41, bins=[0, 10, 20, 30, 40],
                             labels=['Dingin', 'Sejuk', 'Hangat', 'Panas'])
# Kategori penggunaan
df['usage_level'] = pd.qcut(df['count'], q=3, labels=['Rendah', 'Sedang', 'Tinggi'])

# Visualisasi
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(data=df, x='temp_category', hue='usage_level', palette='viridis')
plt.title("Distribusi Level Penyewaan Berdasarkan Kategori Suhu")
plt.xlabel("Kategori Suhu")
plt.ylabel("Jumlah Hari")
st.pyplot(fig)