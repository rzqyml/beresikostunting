import streamlit as st
import pandas as pd
import pickle

# Membaca model
kbst_model = pickle.load(open('kbst_model.sav', 'rb'))

# Judul web
st.title('SISTEM PREDIKSI KELUARGA BERESIKO STUNTING')

# Upload file CSV
uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])

# DataFrame untuk data dari file CSV
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=';')

    # Menampilkan DataFrame
    st.write('DataFrame dari File CSV:')
    st.write(df)

    # Tombol untuk prediksi
    if st.button('Lakukan Prediksi'):
        # Menggunakan model untuk melakukan prediksi
        kbst_prediction = kbst_model.predict(df)

        # Menyimpan hasil prediksi ke dalam DataFrame hasil
        hasil = pd.DataFrame(kbst_prediction, columns=['Hasil Prediksi'])

        # Menampilkan DataFrame untuk hasil prediksi
        st.write('DataFrame untuk Hasil Prediksi:')
        st.write(hasil)
"""
# Fungsi untuk membuat pie chart
def create_pie_chart(df):
    fig = px.pie(df, names=df.index, values='Hasil', title='Pie Chart Hasil Prediksi')
    st.plotly_chart(fig)

# Membaca dataframe "hasil" dari file CSV
nama_file_csv = 'hasil.csv'  # Ganti dengan nama file CSV yang sesuai
hasil_df = pd.read_csv(nama_file_csv)

# Menampilkan tombol visualisasi
if st.button('Visualisasi Pie Chart'):
    create_pie_chart(hasil_df)
"""
