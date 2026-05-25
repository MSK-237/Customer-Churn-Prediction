import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.title("Customer Churn Prediction")

st.write(
    "This application predicts whether a customer will churn or not."
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

senior = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.slider(
    "Tenure",
    0,
    72,
    12
)

phoneservice = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiplelines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

internetservice = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

onlinesecurity = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

onlinebackup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

deviceprotection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

techsupport = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streamingtv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streamingmovies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperlessbilling = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

paymentmethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthlycharges = st.number_input(
    "Monthly Charges",
    value=70.0
)

totalcharges = st.number_input(
    "Total Charges",
    value=1000.0
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phoneservice],
        "MultipleLines": [multiplelines],
        "InternetService": [internetservice],
        "OnlineSecurity": [onlinesecurity],
        "OnlineBackup": [onlinebackup],
        "DeviceProtection": [deviceprotection],
        "TechSupport": [techsupport],
        "StreamingTV": [streamingtv],
        "StreamingMovies": [streamingmovies],
        "Contract": [contract],
        "PaperlessBilling": [paperlessbilling],
        "PaymentMethod": [paymentmethod],
        "MonthlyCharges": [monthlycharges],
        "TotalCharges": [totalcharges]
    })

    input_data = pd.get_dummies(input_data)

    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is likely to stay.")

