import datetime
import numpy as np
import pickle

# Load the pre-trained models using pickle
with open(r'D:\Uzair\Programming\KASBIT Space Hackathon\Models\model_battery_temp.pkl', 'rb') as f:
    model_voltage = pickle.load(f)

with open(r'D:\Uzair\Programming\KASBIT Space Hackathon\Models\model_current.pkl', 'rb') as f:
    model_current = pickle.load(f)

with open(r'D:\Uzair\Programming\KASBIT Space Hackathon\Models\model_battery_temp.pkl', 'rb') as f:
    model_battery_temp = pickle.load(f)

with open(r'D:\Uzair\Programming\KASBIT Space Hackathon\Models\model_wheel_rpm.pkl', 'rb') as f:
    model_wheel_rpm = pickle.load(f)

with open(r'D:\Uzair\Programming\KASBIT Space Hackathon\Models\model_wheel_temp.pkl', 'rb') as f:
    model_wheel_temp = pickle.load(f)


def predict_anomalies(data):
    anomalies = []

    # Extract date_time, hour, and day_of_week from date_time string
    date_time_str = data['date_time']
    date_time = datetime.datetime.strptime(date_time_str, '%m/%d/%Y, %H:%M:%S')
    data['hour'] = date_time.hour
    data['day_of_week'] = date_time.weekday()

    # Remove date_time from data
    data.pop('date_time')

    models = {
        'Voltage': model_voltage,
        'Current': model_current,
        'battery_temp': model_battery_temp,
        'wheel_rpm': model_wheel_rpm,
        'wheel_temp': model_wheel_temp
    }

    for field, model in models.items():
        input_data = data.get(field)
        if input_data is not None:
            if field == 'Current':
                # For 'Current' model, only day_of_week and Current are used
                input_features = np.array([[data['hour'], data['day_of_week'], input_data]])  # Convert to NumPy array
                prediction = model.predict(input_features)  # Predict using the model
            else:
                # For other models, day_of_week and the corresponding field are used
                input_features = np.array([[data['hour'], data['day_of_week'], input_data]])  # Convert to NumPy array
                prediction = model.predict(input_features)  # Predict using the model

            if prediction[0] == 0:
                anomalies.append(field)
    return anomalies
