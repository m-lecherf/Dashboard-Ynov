import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader('Upload a file', type='csv')
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    # select column
    column = st.multiselect("Sélectionner les colonnes",dataframe.columns.sort_values())
    if(st.checkbox("Détails")):
        if(column):
            st.write('Summary statistics:')
            st.write(dataframe[column].describe())
    edited_df = st.data_editor(dataframe[column])
    st.download_button('Download', edited_df.to_csv(), file_name='data.csv', mime='text/csv')