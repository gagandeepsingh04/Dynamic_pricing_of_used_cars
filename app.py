import streamlit as st
import joblib
import numpy as np

# Load the model
model = xgb.XGBRegressor()
model.load_model("used_car_price_xgb.json")

# Streamlit UI
st.title("🚘 Used Car Price Prediction")

# Input fields
months_posted = st.number_input("📅 Months Posted on Platform:", min_value=0, step=1)
fuel_type = st.selectbox("⛽ Fuel Type:", ["Diesel", "Petrol", "CNG/Electric"])
owner = st.selectbox("👤 Owner:", ["1st", "2nd", "3rd"])
transmission = st.selectbox("⚙ Transmission:", ["Manual", "Automatic"])
km_driven = st.number_input("🏁 KM Driven:", min_value=0, step=100)
age = st.number_input("📆 Age of Car:", min_value=0, step=1)
year_passing = st.number_input("🗓 Year of Passing:", min_value=2000, max_value=2025, step=1)
brand = st.text_input("🏷 Brand:")  # Take brand as input

# Convert categorical inputs
fuel_type_map = {"Diesel": 0, "Petrol": 1, "CNG/Electric": 2}
owner_map = {"1st": 1, "2nd": 2, "3rd": 3}
transmission_map = {"Manual": 0, "Automatic": 1}

# Encode Brand using hash (for simplicity, use One-Hot Encoding if your model requires it)
brand_encoded = hash(brand) % 1000  # Converts string to a unique number

# Predict button
if st.button("🚀 Predict Price"):
    # Prepare input data (Now with 8 features!)
    input_data = np.array([[months_posted, fuel_type_map[fuel_type], owner_map[owner], 
                            transmission_map[transmission], km_driven, age, year_passing, brand_encoded]])

    # Predict price (log-transformed value)
    log_predicted_price = model.predict(input_data)[0]

    # Convert log-transformed price back to normal price
    predicted_price = np.exp(log_predicted_price)

    # Display corrected price
    st.success(f"🚘 Predicted Car Price: ₹{predicted_price:,.2f}")
