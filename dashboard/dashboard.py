import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi tampilan Streamlit
st.set_page_config(page_title="🚲 Bike Sharing Dashboard", layout="wide")

# Judul
st.title("🚲 Bike Sharing Data Dashboard")

# Load data
df = pd.read_csv('dashboard/main_data.csv')

# --- Perbaikan nilai tahun ---
# Di dataset, 0 = 2011 dan 1 = 2012
df['year'] = df['year'].replace({0: 2011, 1: 2012})

# Sidebar filter
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun:", sorted(df['year'].unique()))
filtered_df = df[df['year'] == selected_year]

# Bagian 1: Statistik Umum
st.subheader(f"📊 Statistik Umum Tahun {selected_year}")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Penyewaan", value=int(filtered_df['count'].sum()))
with col2:
    st.metric("Rata-rata Harian", value=round(filtered_df['count'].mean(), 2))
with col3:
    st.metric("Suhu Rata-rata (°C)", value=round(filtered_df['temp'].mean() * 41, 1))  # Skala asli 0–1 (≈41°C)

# Bagian 2: Tren Penyewaan per Bulan
st.subheader("📅 Tren Penyewaan Sepeda per Bulan")
monthly_avg = filtered_df.groupby('month')['count'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='month', y='count', data=monthly_avg, marker='o', color='teal')
plt.title('Rata-rata Penyewaan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Rata-rata Jumlah Sewa')
st.pyplot(fig)

# Bagian 3: Korelasi Faktor Lingkungan
st.subheader("🌡️ Korelasi Faktor Lingkungan terhadap Jumlah Penyewaan")
fig, ax = plt.subplots(figsize=(7, 5))
corr = df[['temp', 'humidity', 'windspeed', 'count']].corr()
sns.heatmap(corr, annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('Korelasi Faktor Cuaca dan Jumlah Penyewaan')
st.pyplot(fig)

# Bagian 4: Pengaruh Musim dan Cuaca
st.subheader("🌦️ Pengaruh Musim dan Cuaca terhadap Penyewaan")

col4, col5 = st.columns(2)

with col4:
    season_avg = df.groupby('season')['count'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.barplot(x='season', y='count', hue='season', data=season_avg, palette='viridis', legend=False)
    plt.title('Rata-rata Penyewaan per Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Rata-rata')
    st.pyplot(fig)

with col5:
    weather_avg = df.groupby('weather')['count'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.barplot(x='weather', y='count', hue='weather', data=weather_avg, palette='cool', legend=False)
    plt.title('Rata-rata Penyewaan per Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Rata-rata')
    st.pyplot(fig)

# Bagian 5: RFM Analysis (simplified)
st.subheader("🧮 RFM Analysis (Recency, Frequency, Monetary)")
df['dteday'] = pd.to_datetime(df['dteday'])
reference_date = df['dteday'].max()

rfm = df.groupby('dteday').agg({'count': ['sum', 'mean']}).reset_index()
rfm.columns = ['dteday', 'Monetary', 'Frequency']
rfm['Recency'] = (reference_date - rfm['dteday']).dt.days

fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(x='Recency', y='Monetary', size='Frequency', data=rfm, alpha=0.6, legend=False, color='royalblue')
plt.title('RFM Analysis Scatter Plot')
plt.xlabel('Recency (hari sejak terakhir)')
plt.ylabel('Monetary (total sewa)')
st.pyplot(fig)