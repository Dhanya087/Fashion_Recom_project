import streamlit as st
import pandas as pd

# Load the dataset
try:
    df = pd.read_csv('fashion.csv')
    st.success(" File Loaded successfully.")
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

# Provide recommendation
if submit_button:
    if 'df' in locals():
        # Filter the DataFrame based on user input
        filtered_df = df[
            (df['gender'] == gender) &
            (df['masterCategory'] == master_category) &
            (df['subCategory'] == sub_category) &
            (df['articleType'] == article_type) &
            (df['baseColour'] == base_colour) &
            (df['season'] == season) &
            (df['year'] == year) &
            (df['usage'] == usage)
        ]

        if not filtered_df.empty:
            st.write("Recommended Products:")
            for _, row in filtered_df.iterrows():
                st.write(f"- {row['productDisplayName']}")
        else:
            st.write("No recommendations found based on the selected criteria.")
    else:
        st.error("Dataset not loaded.")






