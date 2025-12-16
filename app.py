import streamlit as st
import pandas as pd
import numpy as np
import math
from knn_kopi import KNearestNeighbor

st.set_page_config(
    page_title="KNN Sistem Rekomendasi Kopi",
    page_icon="☕",
    layout="wide"
)

st.title("☕ Sistem Rekomendasi Kopi untuk Penderita Gangguan Lambung")
st.markdown("Menggunakan Algoritma K-Nearest Neighbor (KNN)")

# Sidebar
with st.sidebar:
    st.header("📊 Informasi Project")
    st.info("""
    **K-Nearest Neighbor KNN**
    - Algoritma: KNN (k=3)
    - Dataset: 50 jenis kopi Indonesia
    - Fitur: Species, Processing Method, Acidity
    - Target: Aman untuk gangguan lambung
    """)

# Demo Data
st.header("📈 Demo Data Kopi Indonesia")

demo_data = {
    'No': [1, 2, 3, 4, 5],
    'Species': ['Arabica', 'Robusta', 'Arabica', 'Excelsa', 'Liberica'],
    'Region': ['Aceh', 'Lampung', 'Sumatra', 'Wonosalam', 'Jambi'],
    'Processing Method': ['Semi Washed', 'Natural', 'Washed', 'Washed', 'Honey'],
    'Acidity': [7.33, 7.9, 7.58, 7.1, 6.8],
    'Rekomendasi': ['✅ AMAN', '❌ TIDAK', '❌ TIDAK', '✅ AMAN', '✅ AMAN']
}

df_demo = pd.DataFrame(demo_data)
st.dataframe(df_demo, use_container_width=True)

st.write("**Keterangan**: Kopi aman jika Acidity < 7.5 dan Processing Method ≠ 'Dry'")

# Statistik
st.header("📊 Statistik Dataset")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Kopi", "50", "records")
with col2:
    st.metric("Kopi Aman", "21", "44.7%")
with col3:
    st.metric("Tidak Aman", "26", "55.3%")
with col4:
    st.metric("Features", "3", "Species, Processing, Acidity")

# Distribution
st.subheader("Distribusi Jenis Kopi")
col1, col2 = st.columns(2)

with col1:
    species_data = {'Arabica': 24, 'Robusta': 11, 'Liberica': 8, 'Excelsa': 4}
    st.bar_chart(species_data)
    
with col2:
    acidity_data = {'Min': 6.60, 'Mean': 7.44, 'Max': 8.20}
    st.bar_chart(acidity_data)

# Predictor
st.header("🔮 Predictor: Cek Apakah Kopi Aman?")

col1, col2, col3 = st.columns(3)

with col1:
    species = st.selectbox("Pilih Jenis Kopi", ["Arabica", "Robusta", "Liberica", "Excelsa"])
    
with col2:
    processing = st.selectbox("Metode Pemrosesan", ["Washed", "Natural", "Semi Washed", "Honey", "Other", "Dry"])
    
with col3:
    acidity = st.slider("Tingkat Keasaman (Acidity)", 6.0, 8.5, 7.5, 0.1)

if st.button("🔍 Cek Rekomendasi", use_container_width=True):
    # Kriteria keamanan
    is_safe_acidity = acidity < 7.5
    is_safe_processing = processing != 'Dry'
    is_safe = is_safe_acidity and is_safe_processing
    
    st.subheader("Hasil Analisis:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**Jenis**: {species}")
        st.write(f"**Metode**: {processing}")
        st.write(f"**Acidity**: {acidity:.2f}")
        st.write(f"\nThreshold Acidity: < 7.5")
        st.write(f"Acidity Check: {'✅ OK' if is_safe_acidity else '❌ TINGGI'}")
        st.write(f"Processing Check: {'✅ OK' if is_safe_processing else '❌ TIDAK COCOK'}")
    
    with col2:
        if is_safe:
            st.success("✅ AMAN DIKONSUMSI", icon="✔️")
            st.info("Kopi ini aman untuk penderita gangguan lambung karena acidity rendah dan metode pemrosesan tepat.")
        else:
            st.error("❌ TIDAK DIREKOMENDASIKAN", icon="❌")
            st.warning("Kopi ini tidak direkomendasikan karena acidity terlalu tinggi atau metode pemrosesan Dry.")

# Model Info
st.header("ℹ️ Informasi Model")

with st.expander("Tentang KNN Algorithm"):
    st.write("""
    **K-Nearest Neighbor (KNN)** adalah algoritma machine learning sederhana yang:
    1. Menyimpan semua data training
    2. Untuk prediksi baru, hitung jarak ke semua training data
    3. Ambil k tetangga terdekat
    4. Voting: gunakan label mayoritas
    
    **Keuntungan:**
    - Mudah dimengerti dan diimplementasikan
    - Efektif untuk dataset kecil
    - Tidak butuh training
    
    **Kekurangan:**
    - Lambat untuk dataset besar
    - Sensitif terhadap outliers
    - Memory intensive
    """)

with st.expander("Metodologi"):
    st.write("""
    **Preprocessing:**
    - Cleansing: Hapus missing values
    - Encoding: Convert categorical to numeric
    - Target: Acidity < 7.5 & Processing != 'Dry'
    
    **Data Split:**
    - Training: 80% (37 samples)
    - Testing: 20% (10 samples)
    
    **Distance Metric:**
    - Euclidean Distance: sqrt((x1-x2)² + (y1-y2)² + (z1-z2)²)
    
    **Parameters:**
    - k = 3 (3 nearest neighbors)
    - Voting: Majority vote
    """)

st.footer("KNN Sistem Rekomendasi Kopi Indonesia | Dec 2025")
