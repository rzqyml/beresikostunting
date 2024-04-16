import streamlit as st
import pandas as pd
import pickle
pip install openpyxl


# Fungsi untuk melakukan prediksi
def predict_stunting_risk(data, model):
    predictions = model.predict(data)
    return predictions

# Main function untuk menjalankan aplikasi web
def main():
    st.title("Sistem Prediksi Keluarga Beresiko Stunting")

    # Upload file Excel
    uploaded_file = st.file_uploader("Unggah file Excel", type=["xlsx"])

    if uploaded_file is not None:
        # Baca data dari file Excel
        df = pd.read_excel(uploaded_file)

        # Load model KBST
        kbst_model = pickle.load(open('kbst_model.sav', 'rb'))

        # Tombol untuk melakukan prediksi
        if st.button('Lakukan Prediksi'):
            # Lakukan prediksi
            predictions = predict_stunting_risk(df, kbst_model)

            # Tambahkan kolom hasil prediksi ke DataFrame
            df['Beresiko Stunting'] = predictions

            # Tampilkan DataFrame dengan hasil prediksi
            st.write("Data dengan hasil prediksi:")
            st.write(df)

            # Unduh data dengan hasil prediksi
            csv_file = df.to_csv(index=False)
            st.download_button("Unduh Data dengan Hasil Prediksi", data=csv_file, file_name='predicted_data.csv', mime='text/csv')

if __name__ == "__main__":
    main()
