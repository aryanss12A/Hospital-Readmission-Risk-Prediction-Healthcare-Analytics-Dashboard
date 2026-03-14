import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from lime.lime_tabular import LimeTabularExplainer

# Load model
model = joblib.load("readmission_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("🏥 Hospital Readmission Risk Predictor")

st.header("Enter Patient Information")

age = st.slider("Age",18,100)
comorbidities = st.slider("Comorbidities Count",0,10)
prev_readmissions = st.slider("Previous Readmissions",0,5)
medications = st.slider("Medications Count",0,20)
length_of_stay = st.slider("Hospital Stay Length",1,30)

if st.button("Predict Risk"):

    patient_data = pd.DataFrame({
        "age":[age],
        "comorbidities_count":[comorbidities],
        "prev_readmissions":[prev_readmissions],
        "medications_count":[medications],
        "length_of_stay":[length_of_stay]
    })

    input_data = pd.DataFrame(columns=model_columns)
    input_data.loc[0] = 0

    for col in patient_data.columns:
        if col in input_data.columns:
            input_data.loc[0,col] = patient_data[col].values[0]

    input_data = input_data.fillna(0)

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠ High Readmission Risk")
    else:
        st.success("✅ Low Readmission Risk")

    st.metric("Probability",f"{probability*100:.2f}%")

    # LIME explanation
    st.subheader("Model Explanation")
    try:
        data = pd.read_csv("hospital_readmission_dataset.csv")
        data = pd.get_dummies(data)
        X = data.drop("label",axis=1)
        # Debug: Show columns and shapes
        st.write("input_data columns:", input_data.columns.tolist())
        st.write("X columns:", X.columns.tolist())
        st.write("input_data shape:", input_data.shape)
        st.write("X shape:", X.shape)
        explainer = LimeTabularExplainer(
            X.values,
            feature_names=X.columns.tolist(),
            class_names=["No Readmission","Readmission"],
            mode="classification"
        )
        exp = explainer.explain_instance(
            input_data.values[0],
            model.predict_proba,
            num_features=10
        )
        fig = exp.as_pyplot_figure()
        st.pyplot(fig)
    except Exception as e:
        st.error(f"LIME explanation failed: {e}")
