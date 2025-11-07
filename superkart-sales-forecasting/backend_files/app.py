# Import necessary libraries
import numpy as np
import joblib  # For loading the serialized model
import pandas as pd  # For data manipulation
from flask import Flask, request, jsonify  # For creating the Flask API

# Initialize the Flask application
superkart_api = Flask("SuperKart Sale Revenue Forecasting API")
# Load the trained model
model = joblib.load("xgb_tuned_model.joblib")

# Define the home route
@superkart_api.get('/')
def home():
    return "Welcome to the SuperKart Sale Revenue Forecasting API!"

# Define the prediction route
@superkart_api.post('/v1/predict')
def predict_revenue():
    # Get the JSON data from the request
    product_data = request.get_json()
    # Create a sample input for prediction
    sample = {
        "Product_Weight": product_data["Product_Weight"],
        "Product_Allocated_Area": product_data["Product_Allocated_Area"],
        "Product_MRP": product_data["Product_MRP"],
        "Store_Age": product_data["Store_Age"],
        "Product_Sugar_Content": product_data["Product_Sugar_Content"],
        "Store_Id": product_data["Store_Id"],
        "Store_Size": product_data["Store_Size"],
        "Store_Location_City_Type": product_data["Store_Location_City_Type"],
        "Store_Type": product_data["Store_Type"],
        "Product_Category": product_data["Product_Category"],
    }
    # Convert the sample input into a DataFrame
    input_data = pd.DataFrame([sample])
    # Make prediction using the loaded model
    predicted_revenue = model.predict(input_data)[0]
    # Return the prediction as a JSON response
    return jsonify({"Predicted Sales Revenue": round(float(predicted_revenue), 2)})

# Define the batch prediction route
@superkart_api.post('/v1/batch_predict')
def batch_predict_revenue():
    # Get the file from the request
    file = request.files['file']
    input_data = pd.read_csv(file)
    # Make predictions using the loaded model
    predicted_revenue = model.predict(input_data).tolist()
    # Round the predictions to 2 decimal places
    predicted_revenue_rounded = [round(float(rev), 2) for rev in predicted_revenue]
    # Extract Product_Id for mapping predictions
    property_ids = input_data["Product_Id"].tolist()
    # Create a dictionary mapping Product_Id to predicted revenue
    output_dict = dict(zip(property_ids, predicted_revenue_rounded))
    # Return the predictions as a JSON response
    return output_dict

# Run the Flask application
if __name__ == "__main__":
    superkart_api.run(debug=True)
