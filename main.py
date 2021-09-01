import requests
from twilio.rest import Client
from decouple import config

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
PHONE_NUMBER = "+1 407 890 7431"
api_key = config("API_KEY")
account_sid = 'AC8371b95d0fccc4ceb78b999a5731a0fb'
auth_token = config("AUTH_TOKEN")


data = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=-5.147665&lon=119.432732&exclude"
                        "=current,minutely,daily&appid=6b61ea360a3d8d633ec9f47fa3979b5f")
data.raise_for_status()
weather_list = data.json()["hourly"][0:12]

final_weather_list = []
for weather in weather_list:
    final_weather_list.append(weather['weather'][0]['id'])

print("Weather id list\n")
# print(final_weather_list)
is_rain = False

for e in final_weather_list:
    if 500 <= e <= 800:
        is_rain = True
        break

if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Woi, Daily reminder to bring your raincoat. It's going to rain today.",
            from_=PHONE_NUMBER,
            to='+62 856-5685-0494'
        )
    print(message.sid)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's not going to rain.",
        from_=PHONE_NUMBER,
        to='+62 856-5685-0494'
    )
    print(message.sid)


