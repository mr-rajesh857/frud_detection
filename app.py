from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd

# Initialize the app
app = Flask(__name__)

# Load the trained model pipeline
model = joblib.load("fraud_detection_pipeline.pkl")  # this includes preprocessing + model

@app.route("/")
def index():
    return render_template("index.html")  # Your UI form

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON input from frontend
        input_data = request.get_json()

        # Extract values in the same order as used in training
        features = [
            input_data['Policy_Num'],
            input_data['Accident_Location'],
            input_data['Insured_Zip'],
            input_data['Policy_Premium'],
            input_data['DL_Expiry_Before_Accident_Days']
        ]

        # Convert into DataFrame (important for pipeline)
        input_df = pd.DataFrame([features], columns=[
            'Policy_Num', 'Accident_Location', 'Insured_Zip',
            'Policy_Premium', 'DL_Expiry_Before_Accident_Days'
        ])

        # Make prediction
        prediction = model.predict(input_df)[0]  # 0 or 1

        return jsonify({'prediction': int(prediction)})
    
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
