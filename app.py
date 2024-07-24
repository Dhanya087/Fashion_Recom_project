import streamlit as st
import pandas as pd

# Load the dataset
try:
    df = pd.read_csv('fashion.csv')
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# Streamlit app
st.title('Fashion Recommender System')

# Input form
with st.form(key='input_form'):
    gender = st.selectbox('Gender', options=df['gender'].unique(), index=df['gender'].unique().tolist().index('Men'))
    master_category = st.selectbox('Master Category', options=df['masterCategory'].unique(), index=df['masterCategory'].unique().tolist().index('Apparel'))
    sub_category = st.selectbox('Sub Category', options=df['subCategory'].unique(), index=df['subCategory'].unique().tolist().index('Topwear'))
    article_type = st.selectbox('Article Type', options=df['articleType'].unique(), index=df['articleType'].unique().tolist().index('Tshirts'))
    base_colour = st.selectbox('Base Colour', options=df['baseColour'].unique(), index=df['baseColour'].unique().tolist().index('Grey'))
    season = st.selectbox('Season', options=df['season'].unique(), index=df['season'].unique().tolist().index('Summer'))
    year = st.number_input('Year', min_value=df['year'].min(), max_value=df['year'].max(), value=2011)
    usage = st.selectbox('Usage', options=df['usage'].unique(), index=df['usage'].unique().tolist().index('Sports'))

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





