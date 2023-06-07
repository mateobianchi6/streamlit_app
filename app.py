import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Mateo's App")
st.subheader("Upload a CSV to analyze")

upload_df = st.file_uploader("Choose File")

if upload_df is not None:
    df = pd.read_csv(upload_df)

st.subheader("Then choose a column and visit the tabs to analyze it!")

col = st.selectbox("Choose a column", df.columns)

tab1, tab2, tab3,  = st.tabs(['At First Glance', 'Numerical Analysis', 'Categorical Analysis'])

#print(df.info)

with tab1:
    st.header("At First Glance")
    nrow = df.shape[0]
    ncol = df.shape[1]
    n_cat = sum(df.dtypes != 'object')
    n_num = sum(df.dtypes == 'object')
    st.text(f"This data set has {nrow} rows and {ncol} columns, very interesting!") 
    st.text(f"There are {n_num} numerical variables and {n_cat} categorical variables.")
    st.text(f"You've chosen to take a deeper look at: {col}")

with tab2:
    st.header('Numerical Analysis')
    if df[col].dtype != 'object':
        st.subheader("Count and Five Number Summary")
        st.text(df[col].describe())

        st.subheader('Distribtution Plot')
        dist = plt.hist(df[col])
        st.write(dist)
    else:
        st.text('Not the right type of variable')
