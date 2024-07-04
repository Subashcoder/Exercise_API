import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'

user_input = input("What is the status: ")

parameters = {
    'query': user_input,
    'gender': 'male',
    'weight_kg': 72,
    'height_cm': 155,
    'age': 26
}

header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

google_endpoint = 'https://api.sheety.co/83e9af11b026cc9c1b7dcf01b26fbf05/myWorkouts/workouts'


response = requests.post(URL, json=parameters, headers=header)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(google_endpoint, json=sheet_inputs)

    print(sheet_response.text)

