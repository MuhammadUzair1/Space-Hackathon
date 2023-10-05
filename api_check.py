import requests

# Define the API URL
api_url = 'http://127.0.0.1:8000/detect_anomalies/'

# Define the input data as a dictionary
data = {
    "date_time": "12/10/2023, 00:15:00",
    "battery_temp": '30.0',
    "Voltage": '11.4',
    "Current": '15.0',
    "wheel_rpm": '2000.0',
    "wheel_temp": '40.0'
}

try:
    # Send a POST request with the input data
    response = requests.post(api_url, json=data)

    # Check the response status code
    if response.status_code == 200:
        result = response.json()
        print("API Response:")
        print(result)
    else:
        print(f"API request failed with status code {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"An error occurred: {str(e)}")
