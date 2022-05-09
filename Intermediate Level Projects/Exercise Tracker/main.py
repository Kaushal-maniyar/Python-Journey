import os
import requests
from datetime import datetime

today = datetime.now()

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": os.environ.get("id"),
    "x-app-key": os.environ.get("key"),
    "Content-Type": "application/json"
}

parameter = {
    "query": input("Which exercise did you perform today? :"),
    "gender": "male",
    "weight_kg": 115,
    "height_cm": 172,
    "age": 21
}

response = requests.post(url=exercise_endpoint, json=parameter, headers=header)
data = response.json()['exercises']

sheet_endpoint = "https://api.sheety.co/a206d7ca0cdc6e23544a5a1fe57a50f9/myExercise/workouts"
for exercise in data:
    exercise_dict = {
        'workout': {
            'date': today.strftime("%d/%m/%Y"),
            'time': f"{today.hour}:{today.minute}:{today.second}",
            'exercise': exercise['user_input'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=exercise_dict, auth=(os.environ.get("user"),os.environ.get(
        "password")))
    print(sheet_response.text)
