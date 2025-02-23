from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load
import pandas as pd

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return "Server is running!"

# Load the trained model
MODEL_FILE = "random_forest_model.joblib"
model = load(MODEL_FILE)

expected_features = ['Distance to the nearest Industrial zones', 'Number of Businesses', 'Area (WH) - CBM']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Validate input
        if 'distance' not in data or not isinstance(data['distance'], (int, float)) or data['distance'] <= 0:
            return jsonify({'error': 'Invalid value for "distance". It must be a positive number.'}), 400

        if 'businesses' not in data or not isinstance(data['businesses'], int) or data['businesses'] <= 0:
            return jsonify({'error': 'Invalid value for "businesses". It must be a positive integer.'}), 400

        if 'area' not in data or not isinstance(data['area'], (int, float)) or data['area'] <= 0:
            return jsonify({'error': 'Invalid value for "area". It must be a positive number.'}), 400

        # Convert input to DataFrame
        features = pd.DataFrame([{
            'Distance to the nearest Industrial zones': data['distance'],
            'Number of Businesses': data['businesses'],
            'Area (WH) - CBM': data['area']
        }])[expected_features].values

        # Predict
        predicted_price = model.predict(features)
        return jsonify({'price': float(predicted_price[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
