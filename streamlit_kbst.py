import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

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

    # Upload CSV file
    uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])
    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv(uploaded_file)
        st.write("Data Awal:")
        st.write(df)

        # Load model
        model = pickle.load(open('kbst_model.sav', 'rb'))

        # Perform prediction
        predictions = predict(df, model)
        df['beresiko stunting'] = predictions

        # Download CSV file with predictions
        st.write("Data dengan Hasil Prediksi:")
        st.write(df)
        csv_file = df.to_csv(index=False)
        st.download_button("Unduh Data dengan Hasil Prediksi", data=csv_file, file_name='predicted_data.csv', mime='text/csv')

        # Show predictions
        st.subheader("Hasil Prediksi:")
        st.write(df)

if __name__ == "__main__":
    main()
