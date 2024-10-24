from flask import Flask, request, jsonify, render_template
from model_loader import load_model
import numpy as np

app = Flask(__name__)

# Load the model using the function from model_loader.py
# model = load_model()

# Serve the front-end page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to handle prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['input_text']  # Input string from the front-end
    # Here, you can process the input data and generate predictions.
    # For simplicity, let's just reverse the string (as an example).

    #TODO: Load model and generate question

    result = data[::-1]  # Reverse the string for demonstration purposes.
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
