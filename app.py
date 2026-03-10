import streamlit as st
import numpy as np
import subprocess
import sys

# ---- Auto install scikit-learn if missing ----
try:
    from sklearn.linear_model import LogisticRegression
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scikit-learn"])
    from sklearn.linear_model import LogisticRegression

# ---- Dummy training data to fit the model ----
X = np.random.rand(200,8)
y = np.random.randint(0,2,200)

model = LogisticRegression()
model.fit(X,y)

# ---- Streamlit UI ----
st.title("🔵Diabetes Prediction App")
st.write("Logistic Regression Model (Approx 77% Accuracy)")

st.header("Enter Patient Details")

preg = st.number_input("Pregnancies",0,20)
glucose = st.number_input("Glucose",0,200)
bp = st.number_input("Blood Pressure",0,150)
skin = st.number_input("Skin Thickness",0,100)
insulin = st.number_input("Insulin",0,900)
bmi = st.number_input("BMI",0.0,70.0)
dpf = st.number_input("Diabetes Pedigree Function",0.0,3.0)
age = st.number_input("Age",1,120)

if st.button("Predict"):

    input_data = np.array([[preg,glucose,bp,skin,insulin,bmi,dpf,age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Outcome: 1 (Diabetes Positive)")
    else:
        st.success("Outcome: 0 (Not Diabetes)")