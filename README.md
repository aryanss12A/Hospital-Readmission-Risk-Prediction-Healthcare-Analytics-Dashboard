# 🏥 Hospital Readmission Risk Prediction & Healthcare Analytics Dashboard

An end-to-end healthcare data analytics and machine learning project
that predicts the probability of hospital readmission using patient
health data.\
The project also includes an interactive analytics dashboard and
explainable AI system to understand model predictions.

------------------------------------------------------------------------

# 📌 Project Overview

Hospital readmissions are a major challenge in healthcare systems. Early
prediction of readmission risk can help hospitals:

-   Improve patient care
-   Reduce healthcare costs
-   Optimize hospital resource allocation
-   Provide early intervention for high-risk patients

This project builds a machine learning system to predict readmission
risk and explains predictions using Explainable AI techniques.

------------------------------------------------------------------------

# 🚀 Features

### 🔹 Machine Learning Prediction

Predicts the probability of patient readmission based on medical and
demographic factors.

### 🔹 Explainable AI

Uses **LIME (Local Interpretable Model-Agnostic Explanations)** to
explain how each feature affects the prediction.

### 🔹 Interactive Streamlit Application

Users can input patient information and receive:

-   Readmission prediction
-   Risk probability
-   Feature importance visualization
-   AI explanation of prediction

### 🔹 Healthcare Analytics Dashboard

Provides visual insights including:

-   Readmission distribution
-   Age distribution
-   Length of stay vs readmission
-   Comorbidities impact
-   Feature correlation heatmap

------------------------------------------------------------------------

# 📊 Dataset

The dataset contains patient hospitalization records including:

  Feature                  Description
  ------------------------ -------------------------------------------------------
  age                      Patient age
  comorbidities_count      Number of chronic diseases
  prev_readmissions        Previous hospital readmissions
  medications_count        Number of medications
  length_of_stay           Duration of hospital stay
  readmission_risk_score   Estimated risk score
  label                    Target variable (0 = No Readmission, 1 = Readmission)

------------------------------------------------------------------------

# 🧠 Machine Learning Model

The project uses supervised learning algorithms to predict readmission
risk.

### Models Used

-   Random Forest Classifier
-   Support Vector Machine (SVM)

### Evaluation Metrics

-   Accuracy
-   Precision
-   Recall
-   F1 Score

------------------------------------------------------------------------

# 🔍 Explainable AI

To make the model transparent and interpretable, **LIME** is used.

Example explanation output:

age \> 65 +0.22\
comorbidities_count +0.18\
prev_readmissions +0.14\
length_of_stay +0.10

------------------------------------------------------------------------

# 🖥️ Streamlit Application

The Streamlit app allows users to:

1.  Enter patient details\
2.  Predict hospital readmission risk\
3.  View probability of readmission\
4.  See feature importance visualization\
5.  Understand model reasoning

------------------------------------------------------------------------

# 📈 Analytics Dashboard

The project includes a data analytics dashboard for exploring patterns
in the dataset.

Visualizations include:

-   Readmission vs No Readmission distribution
-   Patient age distribution
-   Length of stay vs readmission rate
-   Comorbidity impact on readmission
-   Feature correlation heatmap

------------------------------------------------------------------------

# 🛠️ Tech Stack

### Programming Language

-   Python

### Libraries Used

-   Pandas
-   NumPy
-   Scikit-learn
-   Matplotlib
-   Seaborn
-   Streamlit
-   LIME
-   Joblib

### Tools

-   Jupyter Notebook
-   PyCharm
-   GitHub

------------------------------------------------------------------------

# 📂 Project Structure

Healthcare_Project

├── healthcare_analysis.ipynb\
├── hospital_readmission_dataset.csv\
├── readmission_model.pkl\
├── model_columns.pkl\
├── streamlit_app.py\
├── mysql_analysis.sql

pages\
└── analytics_dashboard.py

------------------------------------------------------------------------

# ▶️ How to Run the Project

### Step 1: Clone Repository

git clone
https://github.com/your-username/healthcare-readmission-prediction.git

### Step 2: Install Dependencies

pip install -r requirements.txt

### Step 3: Run Streamlit App

streamlit run streamlit_app.py

------------------------------------------------------------------------

# 💡 Key Insights

Insights derived from the dataset:

-   Patients with multiple comorbidities have higher readmission risk.
-   Longer hospital stays correlate with increased readmission
    probability.
-   Older patients show a higher likelihood of readmission.
-   Previous hospitalizations strongly influence future readmission
    risk.

------------------------------------------------------------------------

# 🔮 Future Improvements

-   Add SHAP explainability
-   Deploy application on Streamlit Cloud
-   Add real-time hospital data integration
-   Implement deep learning models
-   Build REST API for prediction service

------------------------------------------------------------------------

# 👨‍💻 Author

Aryan Sachdeva

Data Analytics & Machine Learning Enthusiast

------------------------------------------------------------------------

# ⭐ If you like this project

Please consider giving the repository a **star ⭐**.
