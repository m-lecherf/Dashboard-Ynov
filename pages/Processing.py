import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader('Upload a file')
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    edited_df = st.data_editor(dataframe)
    st.download_button('Download', edited_df.to_csv(), file_name='data.csv', mime='text/csv')