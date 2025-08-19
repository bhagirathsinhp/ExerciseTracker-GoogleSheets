import requests
import os
from dotenv import load_dotenv
from datetime import datetime as dt

load_dotenv()

# ENVIRONMENT VARIABLES:
NIX_API_ID = os.getenv("NIX_API_ID")
NIX_API_KEY = os.getenv("NIX_API_KEY")
NIX_ENDPOINT = os.getenv("NIX_ENDPOINT")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")

# PERSONAL INFORMATION:
gender = "male"
weight_kg = 78
height_cm = 178
age = 27

# CONFIGURATION:
NIX_HEADER = {
    "Content-Type": "application/json",
    "x-app-id": NIX_API_ID,
    "x-app-key": NIX_API_KEY,
}

nix_query = input("Tell me which exercises you did: ")

nix_payload = {
    "query": nix_query,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

SHEETY_HEADER = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_AUTH
}

date = dt.now()
today = date.strftime("%d/%m/%Y")
time = date.strftime("%H:%M:%S")
print(today, time)

# NIX RESPONSE:
nix_response = requests.post(url=NIX_ENDPOINT, json=nix_payload, headers=NIX_HEADER)
nix_data = nix_response.json()
print(nix_data)

# sheety_get_rows = requests.get(url=SHEETY_ENDPOINT)
# print(sheety_get_rows.json())

for exercise in nix_data["exercises"]:
    ex_name = exercise["name"]
    ex_duration = exercise["duration_min"]
    ex_calories = exercise["nf_calories"]

    #SHEETY PAYLOAD:
    sheety_payload = {
        "workout": {
             "date": today,
             "time": time,
             "exercise": ex_name.title(),
             "duration": ex_duration,
             "calories": ex_calories
        }
    }

    #SHEETY NEW ROW PER EXERCISE:
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_payload, headers=SHEETY_HEADER)
    print(sheety_response.text)