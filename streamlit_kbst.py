import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

# Membaca model
kbst_model = pickle.load(open('kbst_model.sav', 'rb'))

# Judul web
st.title('SISTEM PREDIKSI KELUARGA BERESIKO STUNTING')

# Upload file CSV
uploaded_file = st.file_uploader("Unggah file xlsx", type=["xlsx","xls"])

# DataFrame untuk data dari file CSV
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    # Membaca file CSV dengan koma sebagai pemisah
    #df_comma = pd.read_csv(uploaded_file, sep=',')

    # Membaca file CSV dengan titik koma sebagai pemisah
   # df_semicolon = pd.read_csv(uploaded_file, sep=';')


    # Menampilkan DataFrame
    st.write('DataFrame dari File xlsx:')
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
 # Generate pie chart
        prediction_counts = df['Beresiko Stunting'].value_counts()
        prediction_counts.index = ['Tidak Beresiko Stunting' if idx == 0 else 'Beresiko Stunting' for idx in prediction_counts.index]
        fig = px.pie(prediction_counts, values=prediction_counts.values, names=prediction_counts.index,
                     title='Prediction Distribution')
        st.plotly_chart(fig)
# Pie chart
    # st.subheader('Pie Chart Hasil Prediksi')
    # fig_pie = px.pie(hasil, names='Hasil Prediksi', title='Sebaran Hasil Prediksi')
    # st.plotly_chart(fig_pie)
