
import requests
from twilio.rest import Client
import http.client
import json
import os

# OpenWeatherMap API setup
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
my_api = os.environ.get("OWM_API_KEY")

# Twilio credentials
account_sid = os.environ.get("account_sid")
auth_token =os.environ.get("auth")

# List of WhatsApp numbers to send the message to
phone_numbers = [
    'whatsapp:+Phone Number',  # Replace with verified Twilio numbers
    'whatsapp:+Phone Number'

]

# Weather Parameters
weather_parms = {
    "lat": -6.175110,  # Replace with your latitude
    "lon": 106.865036,  # Replace with your longitude
    "appid": my_api,
}

# Fetch weather data
response = requests.get(OWM_Endpoint, params=weather_parms)
response.raise_for_status()
weather_data = response.json()

# Check for rain
will_rain = False
for hour_data in weather_data["list"]:
    conditions_code = hour_data["weather"][0]["id"]
    if int(conditions_code) < 700:  # Weather condition codes < 700 indicate rain or similar
        will_rain = True
        break

# Fetch a motivational quote from RapidAPI
conn = http.client.HTTPSConnection("quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "Api KEY",
    'x-rapidapi-host': "quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com"
}
conn.request("GET", "/quote?token=ipworld.info", headers=headers)
res = conn.getresponse()
data = res.read()

# Parse the quote JSON and extract fields
quote_data = json.loads(data.decode("utf-8"))
quote_text = quote_data.get("text", "Stay motivated!")  # Default message if text is missing
quote_author = quote_data.get("author", "Unknown")  # Default author if missing

# Format the quote
formatted_quote = f'"{quote_text}"\n- {quote_author}'

# Initialize Twilio Client
client = Client(account_sid, auth_token)

# Message content based on weather
if will_rain:
    message_body = f'It looks like it will rain today. Bring an umbrella! 🌧\n\nHere is a quote to brighten your day:\n{formatted_quote}'
else:
    message_body = f'Here is a quote to brighten your day:\n{formatted_quote}'

# Send the message to all numbers
for number in phone_numbers:
    message = client.messages.create(
        from_='whatsapp:+Phone in Twilio',  # Twilio's WhatsApp sandbox number
        to=number,
        body=message_body
    )
    print(f"Message sent to {number} with SID: {message.sid}")

