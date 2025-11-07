import streamlit as st
import pandas as pd
import requests

# Set page configuration
st.set_page_config(page_title="SuperKart Sales Revenue Prediction", layout="wide")
# Page title
st.title("SuperKart Sales Revenue Prediction")
# Page subheader
st.subheader("Single Prediction")
# Input fields for user to enter product and store details
product_weight = st.number_input("Product Weight", min_value=0.1, max_value=25.0, step=0.1, value=12.15)
product_allocated_area = st.number_input("Product Allocated Area", min_value=0.000, max_value=0.400, step=0.001, value=0.150)
product_mrp = st.number_input("Product MRP", min_value=20.0, max_value=500.0, step=0.1, value=27.0)
store_age = st.number_input("Store Age", min_value=0, max_value=50, step=1, value=16)
product_sugar_content = st.selectbox("Product Sugar Content", options=["Low Sugar", "Regular", "No Sugar"], index=1)
store_id = st.selectbox("Store Id", options=["OUT001", "OUT002", "OUT003", "OUT004"], index=0)
store_size = st.selectbox("Store Size", options=["Small", "Medium", "High"], index=1)
store_location_city_type = st.selectbox("Store Location City Type", options=["Tier 1", "Tier 2", "Tier 3"], index=0)
store_type = st.selectbox("Store Type", options=["Food Mart", "Supermarket Type1", "Supermarket Type2", "Departmental Store"], index=1)
product_category = st.selectbox(
    "Product Category", 
    options=[
        'Packaged',
        'Fresh',
        'Non-Consumable',
        'Beverages'
    ],
    index=1
)
# Create a DataFrame from the input data
input_data = pd.DataFrame({
    "Product_Weight": [product_weight],
    "Product_Allocated_Area": [product_allocated_area],
    "Product_MRP": [product_mrp],
    "Store_Age": [store_age],
    "Product_Sugar_Content": [product_sugar_content],
    "Store_Id": [store_id],
    "Store_Size": [store_size],
    "Store_Location_City_Type": [store_location_city_type],
    "Store_Type": [store_type],
    "Product_Category": [product_category],
})
# Predict button to send data to the backend API for prediction
if st.button("Predict Sales Revenue"):
    # Make a POST request to the backend API
    response = requests.post("https://ferruss-superkart-backend.hf.space/v1/predict", json=input_data.to_dict(orient='records')[0])
    # Display the prediction result
    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Predicted Sales Revenue: {prediction['Predicted Sales Revenue']:.2f}")
    else:
        st.error("Error in prediction. Please try again.")
# Section for batch prediction
st.subheader("Batch Prediction")
# File uploader for uploading CSV file
uploaded_file = st.file_uploader("Upload CSV file for batch prediction", type=["csv"])
# Predict button for batch prediction
if uploaded_file is not None:
    if st.button("Predict Batch"):
        # Make a POST request to the backend API for batch prediction
        response = requests.post("https://ferruss-superkart-backend.hf.space/v1/batch_predict", files={"file": uploaded_file})
        if response.status_code == 200:
            predictions = response.json()
            st.success("Batch Prediction Successful!")
            predictions_df = pd.DataFrame(list(predictions.items()), columns=["Product_Id", "Predicted Sales Revenue"])
            st.dataframe(predictions_df)
        else:
            st.error("Error in batch prediction. Please try again.")
