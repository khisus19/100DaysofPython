import requests

API = "https://opentdb.com/api.php?"
params = {
    "amount": 10,
    "type": "boolean"
}

r = requests.get(API, params=params)
data = r.json()["results"]

question_data = data
