import streamlit as st
import pandas as pd
import pickle

# Judul web
st.title('Upload File Excel')

# Upload file Excel
uploaded_file = st.file_uploader("Unggah file Excel", type=["xlsx", "xls"])

# Memproses file setelah diupload
if uploaded_file is not None:
    # Membaca file Excel menjadi DataFrame
    df = pd.read_excel(uploaded_file)
    
    # Menampilkan data DataFrame
    st.write('Data yang diupload:')
    st.write(df)
