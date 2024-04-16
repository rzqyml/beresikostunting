import streamlit as st
import pandas as pd

# Judul web
st.title('Unggah File CSV dan Buat DataFrame')

# Upload file CSV
uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])

# DataFrame untuk data dari file CSV
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Menampilkan DataFrame
    st.write('DataFrame dari File CSV:')
    st.write(df)

    # Membuat DataFrame baru untuk hasil
    hasil = pd.DataFrame(columns=df.columns)

    # Menampilkan DataFrame untuk hasil
    st.write('DataFrame untuk Hasil:')
    st.write(hasil)
