import requests, datetime

MY_LAT = 20.616228
MY_LNG = -100.474420

def is_close():
    r = requests.get("http://api.open-notify.org/iss-now.json")
    r.raise_for_status()
    iss_data = r.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if ( MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 ) and ( MY_LNG - 5 <= iss_longitude <= MY_LNG + 5 ):
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
       
    time_now = datetime.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    
