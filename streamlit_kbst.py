import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Function to perform prediction
def predict(df, model):
    # Preprocess the data if necessary
    # For example, encode categorical variables
    # Encode categorical columns if any
    label_encoders = {}
    for column in df.select_dtypes(include=['object']).columns:
        label_encoders[column] = LabelEncoder()
        df[column] = label_encoders[column].fit_transform(df[column])

    # Perform prediction
    predictions = model.predict(df)
    
    return predictions

# Main function to run the web app
def main():
    st.title("Sistem Prediksi Keluarga Beresiko Stunting")

    # Upload Excel file
    uploaded_file = st.file_uploader("Unggah file Excel", type=["xlsx"])
    if uploaded_file is not None:
        # Read Excel file
        df = pd.read_excel(uploaded_file)
        st.write("Data Awal:")
        st.write(df)

        # Load model
        model = pickle.load(open('kbst_model.sav', 'rb'))

        # Perform prediction
        predictions = predict(df, model)
        df['Hasil Prediksi'] = predictions

        # Download Excel file with predictions
        st.write("Data dengan Hasil Prediksi:")
        st.write(df)
        excel_file = df.to_excel(index=False)
        st.download_button("Unduh Data dengan Hasil Prediksi", data=excel_file, file_name='predicted_data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        # Visualisasi prediksi
        st.subheader('Visualisasi Prediksi')
        plt.figure(figsize=(8, 6))
        sns.countplot(data=df, x='Hasil Prediksi')
        plt.title('Distribusi Prediksi Keluarga Beresiko Stunting')
        st.pyplot()

if __name__ == "__main__":
    main()
