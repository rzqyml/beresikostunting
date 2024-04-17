import streamlit as st
import pandas as pd
import pickle
#import plotly.express as px

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
        hasil = pd.DataFrame(kbst_prediction, columns=['hasil prediksi'])

        # Menampilkan DataFrame untuk hasil prediksi
        st.write('DataFrame Hasil Prediksi:')
        st.write(hasil)
 # Menggabungkan dataframe hasil prediksi dengan dataframe asli
        merged_df = pd.concat([df, hasil], axis=1)

        # Menampilkan dataframe gabungan
        st.write('DataFrame Final:')
        st.write(merged_df)

# Pie chart
#st.subheader('Pie Chart Hasil Prediksi')
#fig_pie = px.pie(hasil, names='Hasil Prediksi', title='Sebaran Hasil Prediksi')
#st.plotly_chart(fig_pie)
