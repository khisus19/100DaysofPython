import requests, os

####-------------------- Message ---------------------###

from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console

# and set the environment variables. See http://twil.io/secure

account_sid = os.getenv("ACCOUNT_SID")

auth_token = os.getenv("AUTH_TOKEN")

client = Client(account_sid, auth_token)



####-------------------- Weather ---------------------###
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = os.environ.get("OWM_API_KEY")

weather_params_rancho = {
    "lat": 20.616228,
    "lon": -100.474419,
    "cnt": 4,
    "appid": api_key
}

weather_params_brazil = {
    "lat": -7.634500,
    "lon": -72.668579,
    "cnt": 4,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, weather_params_brazil)
data = response.json()["list"]

will_rain = False

for hour_data in data:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True


if will_rain:
    message = client.messages.create(

        body="It's going to rain today. Remember to bring an ☂",

        from_="+15074316619",

        to="+523322502445",

    )

