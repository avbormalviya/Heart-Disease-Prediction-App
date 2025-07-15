# ❤️ Heart Disease Prediction App

This project is a machine learning-based web application that predicts the risk of heart disease based on a patient's medical data. Built using **Python**, **scikit-learn**, and **Streamlit**, it demonstrates a complete ML pipeline — from data cleaning and model training to deployment-ready UI.

---

## 📌 Features

- Accepts key medical inputs: age, sex, cholesterol, chest pain type, etc.
- Predicts the presence of heart disease using a trained Random Forest model
- User-friendly web interface built with Streamlit
- 85% accuracy on test data
- Code follows clean and modular ML pipeline practices

---

## 🧠 Machine Learning Overview

- **Dataset**: UCI Heart Disease Dataset
- **Target**: Binary classification → `0 = No disease`, `1 = Disease`
- **Model**: `RandomForestClassifier` (tuned with sensible defaults)
- **Accuracy**: ~85% on held-out test set

---

## 📊 Dataset Features

| Feature     | Description                                      |
|-------------|--------------------------------------------------|
| age         | Age of the patient                               |
| sex         | Male/Female (converted to binary)                |
| cp          | Chest pain type (categorical, one-hot encoded)   |
| trestbps    | Resting blood pressure                           |
| chol        | Serum cholesterol (mg/dl)                        |
| fbs         | Fasting blood sugar > 120 mg/dl (True/False)     |
| restecg     | Resting ECG results (categorical)                |
| thalach     | Maximum heart rate achieved                      |
| exang       | Exercise-induced angina (True/False)             |
| oldpeak     | ST depression induced by exercise                |
| slope       | Slope of the ST segment (categorical)            |
| ca          | Major vessels colored by fluoroscopy             |
| thal        | Heart defect type (categorical)                  |
| num         | Target (0 = no disease, 1 = disease)             |

---

## 🛠️ Installation

1. **Clone the repo**
```bash
git clone https://github.com/avbormalviya/Heart-Disease-Prediction-App.git
cd Heart-Disease-Prediction-App
