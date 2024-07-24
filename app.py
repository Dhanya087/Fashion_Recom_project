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
    gender = st.selectbox('Gender', ['Men', 'Women'])
    master_category = st.selectbox('Master Category', ['Apparel', 'Footwear', 'Accessories'])
    sub_category = st.selectbox('Sub Category', ['Topwear', 'Bottomwear', 'Footwear', 'Accessories', 'Bottomwear'])
    article_type = st.selectbox('Article Type', ['Shirts', 'Jeans', 'Jackets', 'Shoes', 'T Shirt', 'Track Pants'])
    base_colour = st.selectbox('Base Colour', ['Black', 'White', 'Blue', 'Red', 'Yellow', 'Gold', 'Navy Blue', 'Silver', 'Orange', 'Maroon', 'Grey'])
    season = st.selectbox('Season', ['Winter', 'Summer', 'Fall', 'Spring'])
    year = st.number_input('Year', min_value=2000, max_value=2024, value=2024)
    usage = st.selectbox('Usage', ['Casual', 'Formal', 'Party', 'Sports'])

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




