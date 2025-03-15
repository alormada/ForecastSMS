import requests
import os
from twilio.rest import Client
#twilio
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
#weather
API_KEY = os.environ.get("OWM_API_KEY")
LATITUDE = 51.107883
LONGITUDE = 17.038538

print(API_KEY)

PHONE_NUMBER=os.environ.get("PHONE_NUMBER")
CITY="Wrocław"

message_text=f"The weather forcast for today in {CITY}:"

params = {
    "appid": API_KEY,
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "cnt":4,
}
print(params)
r = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
r.raise_for_status()
data = r.json()
# print(data)

is_raining = False
weather_id = None
for hour_data in data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    hour = hour_data['dt_txt'].split(" ")[1].split(":")[0]
    temp = hour_data["main"]["temp"] - 272.15
    temp = round(temp)
    message_text += f"\n{hour}:00 Temperature: {temp}°C "
    if weather_id < 700:
        message_text += "| Rainy"
        is_raining = True
        break

print(message_text)

if is_raining:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_text,
        from_='TWILIO NUMBER',
        to=PHONE_NUMBER
    )

    print(message.status)
else:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message_text,
        from_="TWILIO NUMBER",
        to=PHONE_NUMBER
    )

    print(message.status)

