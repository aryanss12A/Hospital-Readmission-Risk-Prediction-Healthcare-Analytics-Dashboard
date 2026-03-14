import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Hospital Readmission Analytics Dashboard")

df = pd.read_csv("hospital_readmission_dataset.csv")

st.subheader("Dataset Overview")
st.write(df.head())

# -----------------------------
# Readmission Distribution
# -----------------------------
st.subheader("Readmission Distribution")

fig, ax = plt.subplots()

sns.countplot(x="label", data=df, ax=ax)

ax.set_title("Readmission vs No Readmission")

st.pyplot(fig)

# -----------------------------
# Age Distribution
# -----------------------------
st.subheader("Age Distribution")

fig, ax = plt.subplots()

sns.histplot(df["age"], bins=20, ax=ax)

ax.set_title("Patient Age Distribution")

st.pyplot(fig)

# -----------------------------
# Length of Stay vs Readmission
# -----------------------------
st.subheader("Length of Stay vs Readmission")

fig, ax = plt.subplots()

sns.boxplot(x="label", y="length_of_stay", data=df, ax=ax)

ax.set_title("Hospital Stay vs Readmission")

st.pyplot(fig)

# -----------------------------
# Comorbidities Impact
# -----------------------------
st.subheader("Comorbidities Impact")

fig, ax = plt.subplots()

sns.barplot(
    x="comorbidities_count",
    y="label",
    data=df,
    ax=ax
)

ax.set_title("Comorbidities vs Readmission Rate")

st.pyplot(fig)

# -----------------------------
# Correlation Heatmap
# -----------------------------
st.subheader("Feature Correlation")

fig, ax = plt.subplots(figsize=(10,6))

sns.heatmap(
    df.corr(numeric_only=True),
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)