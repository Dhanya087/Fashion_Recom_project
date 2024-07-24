import streamlit as st
import pandas as pd

# Load the dataset
try:
    df = pd.read_csv('fashion.csv')
except Exception as e:
    st.error(f"Error loading dataset: {e}")

# Streamlit app
st.title('Fashion Recommender System')

# Input form
with st.form(key='input_form'):
    gender = st.selectbox('Gender', df['gender'].unique())
    master_category = st.selectbox('Master Category', df['masterCategory'].unique())
    sub_category = st.selectbox('Sub Category', df['subCategory'].unique())
    article_type = st.selectbox('Article Type', df['articleType'].unique())
    base_colour = st.selectbox('Base Colour', df['baseColour'].unique())
    season = st.selectbox('Season', df['season'].unique())
    year = st.number_input('Year', min_value=df['year'].min(), max_value=df['year'].max(), value=df['year'].max())
    usage = st.selectbox('Usage', df['usage'].unique())

    # Submit button
    submit_button = st.form_submit_button(label='Get Recommendation')

# Predict button
if submit_button:
    try:
        input_data = pd.DataFrame({
            'gender': [gender],
            'masterCategory': [master_category],
            'subCategory': [sub_category],
            'articleType': [article_type],
            'baseColour': [base_colour],
            'season': [season],
            'year': [year],
            'usage': [usage]
        })
        
        # Matching the input data with the dataset to find similar items
        matching_items = df[
            (df['gender'] == gender) &
            (df['masterCategory'] == master_category) &
            (df['subCategory'] == sub_category) &
            (df['articleType'] == article_type) &
            (df['baseColour'] == base_colour) &
            (df['season'] == season) &
            (df['year'] == year) &
            (df['usage'] == usage)
        ]

        if not matching_items.empty:
            recommended_product = matching_items.sample(1)['productDisplayName'].values[0]
            st.write(f"Recommended Product: {recommended_product}")
        else:
            st.write("No matching product found. Please try different options.")
    except Exception as e:
        st.error(f"Error making recommendation: {e}")



