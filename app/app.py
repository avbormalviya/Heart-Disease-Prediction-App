from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("../saved_model/heart_model.pkl", "rb"))
model_columns = pickle.load(open("../saved_model/columns.pkl", "rb"))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
        input_dict = {
            'age': float(request.form['age']),
            'sex': float(request.form['sex']),
            'trestbps': float(request.form['trestbps']),
            'chol': float(request.form['chol']),
            'fbs': float(request.form['fbs']),
            'thalach': float(request.form['thalach']),
            'exang': float(request.form['exang']),
            'oldpeak': float(request.form['oldpeak']),
            'ca': float(request.form['ca']),
            'cp': int(request.form['cp']),
            'restecg': int(request.form['restecg']),
            'slope': int(request.form['slope']),
            'thal': int(request.form['thal'])
        }

        import pandas as pd
        df = pd.DataFrame([input_dict])

        # One-hot encode
        df = pd.get_dummies(df, columns=['cp', 'restecg', 'slope', 'thal'], drop_first=True)

        # Add missing columns
        for col in model_columns:
            if col not in df.columns:
                df[col] = 0

        # Ensure correct column order
        df = df[model_columns]

        prediction = model.predict(df)[0]
        if int(prediction) == 0:
            message = "You are normal. I am glad you are fine!"
            result_class = "result-green"
        else:
            message = "Danger: Please consult a doctor as soon as possible."
            result_class = "result-red"
        return render_template("index.html", prediction_text=message, result_class=result_class)

    except Exception as e:
        return f"Oops! Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
