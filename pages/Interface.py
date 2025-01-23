import streamlit as st
import pandas as pd
import seaborn as sns

uploaded_file = st.file_uploader('Upload a file', type='csv')
if uploaded_file is not None:
    # Configuration de la page
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    # select column
    column = st.multiselect("Sélectionner les colonnes",dataframe.columns.sort_values())
    if(column):
        if(st.checkbox("Détails")):
            st.write('Summary statistics:')
            st.write(dataframe[column].describe())

        graph_type = st.multiselect("Sélectionner les graphs à visualiser", ['Historigramme', 'Lignes', 'Area Chart'])
        # display if the column is integer or float
        if(graph_type): 
            if dataframe[column].select_dtypes(include=['int64', 'float64']).shape[1] > 0:
                # graphs
                data = dataframe[column].select_dtypes(include=['int64', 'float64'])
                if(graph_type.__contains__('Historigramme')):
                    st.bar_chart(data)

                if(graph_type.__contains__('Lignes')):
                    st.line_chart(data)

                if(graph_type.__contains__('Area Chart')):
                    st.area_chart(data)

    edited_df = st.data_editor(dataframe[column])
    st.download_button('Download', edited_df.to_csv(), file_name='data.csv', mime='text/csv')