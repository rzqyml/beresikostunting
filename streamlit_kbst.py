
import streamlit as st
import pandas as pd

# Judul web
st.title('Unggah File Excel dan Buat DataFrame')

# Unggah file Excel
uploaded_file = st.file_uploader("Unggah file Excel", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Membaca file Excel dan membuat DataFrame
    df = pd.read_excel(uploaded_file)

    # Menampilkan DataFrame yang dibuat
    st.write("DataFrame dari File Excel:")
    st.write(df)

    # Membuat DataFrame baru dengan data kosong
    hasil = pd.DataFrame(columns=df.columns)

    # Menampilkan DataFrame baru
    st.write("DataFrame Baru (Hasil):")
    st.write(hasil)
