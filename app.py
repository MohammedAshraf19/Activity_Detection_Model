
import pickle
from flask import Flask, request, jsonify

# Import the equation function from your Equations.py file
from Equations import Equation

app = Flask(__name__)

# Load the XGBoost model
model = pickle.load(open('model.pkl', 'rb'))

# Define the route for predicting activities
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the input data from the request
    data = request.get_json(force=True)

    activity = Equation(data['acc_x'], data['acc_y'], data['acc_z'], data['gyro_x'], data['gyro_y'], data['gyro_z'])

    # Make predictions using the loaded model
    predictions = model.predict(activity)
    
    activity_labels = ['Fall', 'Up Stairs', 'Jumping', 'Standing', 'Walking', 'Down Stairs', 'Joging', 'Sitting']

    predicted_activities = [activity_labels[i] for i in predictions]
    
    # Return the predictions as a JSON response
    return jsonify(predicted_activities)

if __name__ == '__main__':
    app.run(debug=True)
