import streamlit as st
import pandas as pd
import pickle

# Load the KBST model
kbst_model = pickle.load(open('kbst_model.sav', 'rb'))

# Main function
def main():
    # Set page title
    st.title('Prediksi Keluarga Beresiko Stunting')

    # File upload
    uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])

    # Check if file is uploaded
    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Display the uploaded data
        st.write("Data yang diunggah:")
        st.write(df)

        # Button for prediction
        if st.button('Lakukan Prediksi'):
            # Perform prediction
            predictions = kbst_model.predict(df)

            # Create a new dataframe with predictions
            result_df = pd.DataFrame({'Hasil Prediksi': predictions})

            # Concatenate the original dataframe and the result dataframe
            result_df = pd.concat([df, result_df], axis=1)

            # Display the result dataframe
            st.write("Hasil Prediksi:")
            st.write(result_df)

            # Download the result dataframe as CSV
            result_csv = result_df.to_csv(index=False)
            st.download_button("Unduh Hasil Prediksi", data=result_csv, file_name='hasil_prediksi.csv', mime='text/csv')

if __name__ == "__main__":
    main()
