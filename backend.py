import os

import requests
from dotenv import load_dotenv

# Load env variable - token needed to access https://openweathermap.org/forecast5
load_dotenv()
API_KEY = os.getenv("ACCESS_API_TOKEN")

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Tokio", forecast_days=3))