import streamlit as st
import pandas as pd
import numpy as np

st.title("Mateo's App")
st.subheader("Upload a CSV to analyze")

upload = st.file_uploader("Choose File")
if upload is not None:
    df = pd.read_csv(upload)
    st.write(df)

st.subheader("Then choose a column and visit the tabs to analyze it!")

st.selectbox("Choose a column", df.columns)

tab1, tab2, tab3,  = st.tabs(['At First Glance', 'Numerical Analysis', 'Categorical Analysis'])

print(df.info)

with tab1:
    st.header("At First Glance")
    nrow = df.shape[0]
    ncol = df.shape[1]
    n_cat = 0
    n_num = 0
    for i in df.info[0]:
        if type(i) in ('int', 'float'):
            n_num = n_num + 1
        else:
            n_cat = n_cat + 1
    st.text(f"This data set has {nrow} rows and {ncol} columns, very interesting! There are {n_num} numerical variables and {n_cat} categorical variables.")
    st.text(df.info)

