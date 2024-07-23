import streamlit as st
import pandas as pd
import pickle

# Load the model
try:
    with open('best_model.pkl', 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")

# Streamlit app
st.title('Fashion Recommender System')

# Input form
with st.form(key='input_form'):
    gender = st.selectbox('Gender', ['Men', 'Women'])
    master_category = st.selectbox('Master Category', ['Apparel', 'Footwear', 'Accessories'])
    sub_category = st.selectbox('Sub Category', ['Topwear', 'Bottomwear', 'Footwear', 'Accessories','Bottomwear'])
    article_type = st.selectbox('Article Type', ['Shirts', 'Jeans', 'Jackets', 'Shoes','T Shirt','Track Pants'])
    base_colour = st.selectbox('Base Colour', ['Black', 'White', 'Blue', 'Red','Yellow','Gold','Navy Blue','Silver','Orange','Maroon','Grey'])
    season = st.selectbox('Season', ['Winter', 'Summer', 'Fall', 'Spring'])
    year = st.number_input('Year', min_value=2000, max_value=2024, value=2024)
    usage = st.selectbox('Usage', ['Casual', 'Formal', 'Party', 'Sports'])

    # Submit button
    submit_button = st.form_submit_button(label='Get Recommendation')

# Predict button
if submit_button:
    if 'model' in locals():
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
        
        try:
            prediction = model.predict(input_data)
            st.write(f"Recommended Product: {prediction[0]}")
        except Exception as e:
            st.error(f"Error making prediction: {e}")
    else:
        st.error("Model not loaded.")



