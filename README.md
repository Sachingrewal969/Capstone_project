# Real Estate Price Prediction

**Project Overview**

This project aims to predict real estate property prices based on various attributes such as location, size, number of bedrooms, property type, and amenities using machine learning models. The goal is to build an accurate model that helps users estimate property prices and make informed investment decisions.

**Dataset**
The dataset used for this project contains real estate property details, including location, BHK, area, price, property type, and amenities. The data is cleaned, preprocessed, and analyzed for better model performance. The dataset can be found in the data directory.

## Tech Stack

**Programming Language:** Python 3.10

**Libraries:** Pandas, NumPy, Scikit-Learn, XGBoost, Matplotlib, Seaborn

**ML Models:** Linear Regression, Random Forest, XGBoost, SVM

**Deployment:** Streamlit for web app

## Data Processing & Feature Engineering

✔ Data Cleaning (Handling missing values, outliers)

✔ Feature Engineering (Scaling numerical features, encoding categorical variables)

✔ Exploratory Data Analysis (EDA) with visualizations

✔ Model Training & Hyperparameter Tuning

## Model Performance

**Evaluation Metrics**: RMSE, R² Score

**Best Model:** XGBoost with optimized hyperparameters

## How to Run the Project

1. Clone the repository

git clone https://github.com/yourusername/Real_Estate_Price_Prediction.git  

cd Real_Estate_Price_Prediction  

2. Install dependencies

pip install -r requirements.txt  

3. Run the Streamlit app

streamlit run app.py  

Access the web interface at http://localhost:8501/

## Results & Insights

Location and area are the most influential factors in determining property prices

Property type and number of bedrooms significantly impact pricing

Feature scaling and encoding improved model performance

## Project Structure

Real_Estate_Price_Prediction  
 ├── datasets            # Contains raw and processed datasets  
 ├── pages               # Streamlit app pages  
 ├── Home.py                # Main entry point for the Streamlit app  
 ├── df.pkl                 # Processed dataset stored as a pickle file  
 ├── latlong_scrapper.py    # Script to extract latitude and longitude data  
 ├── pipeline.pkl           # Trained machine learning model pipeline  
 ├── requirements.txt       # Dependencies and package requirements  
 ├── README.md   

 ## Future Enhancements
 
Implement deep learning models for better accuracy

# Live Demo

https://capstoneproject-mjs3n29gjzkdiwvuytv7k9.streamlit.app/
