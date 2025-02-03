import streamlit as st
import sklearn
print(sklearn.__version__)
# Set page config (only once, at the top)
st.set_page_config(page_title="Real Estate App", page_icon="🏠")

# Welcome message
st.write("# Welcome to the Real Estate Price Prediction App! 👋")

# Sidebar message
st.sidebar.success("Select a section to explore.")

# Project description
st.markdown("""
### About this Project

This project is a **Real Estate Price Prediction App** developed to assist users in predicting property prices based on various features. The application leverages machine learning techniques to analyze property details such as:
- Number of bedrooms and bathrooms
- Built-up area
- Availability of servant and store rooms
- Sector and age of the property

### Key Features
 - **Price Predictor**: Estimate property prices based on selected features.
 - **Analysis App**: Visualize and analyze various aspects of real estate data.
 - **Recommend Apartments**: Get recommendations for similar apartments based on your preferences.

### Usage
Use the sidebar to navigate through different sections of the app. You can try out different demos or input specific property details to see real-time predictions.

This app was created as part of a capstone project to showcase machine learning and data science skills.
""")
