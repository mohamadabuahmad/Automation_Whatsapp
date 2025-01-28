# 🌦️ Weather Alert and Motivational Quote Bot

A Python-based bot that sends daily weather alerts and motivational quotes via WhatsApp using **OpenWeatherMap**, **RapidAPI**, and **Twilio APIs**.

---

## 🚀 Features

- **Weather Forecast Alerts**: Alerts users about potential rain using OpenWeatherMap.
- **Daily Motivation**: Sends inspirational quotes from RapidAPI.
- **WhatsApp Integration**: Uses Twilio's WhatsApp API to send messages to multiple recipients.
- **Automated Scheduling**: Can run daily at a specified time.

---

## 📋 Requirements

### 🛠️ APIs and Services

1. **[OpenWeatherMap API](https://openweathermap.org/api)**:
   - Provides weather forecast data.
   - Free tier available.

2. **[RapidAPI - Inspirational Quotes](https://rapidapi.com/)**:
   - Fetches daily motivational quotes.
   - Sign up for a free API key.

3. **[Twilio API for WhatsApp](https://www.twilio.com/whatsapp)**:
   - Enables sending WhatsApp messages.
   - Free trial available (requires verified numbers).

---

### 💻 Environment and Dependencies

- **Python 3.7+**
- Required Python Libraries:
  - `requests`
  - `twilio`

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/weather-alert-bot.git
cd weather-alert-bot

python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
OWM_API_KEY=<Your OpenWeatherMap API Key>
account_sid=<Your Twilio Account SID>
auth=<Your Twilio Auth Token>

OUTPUT
It looks like it will rain today. Bring an umbrella! 🌧

Here is a quote to brighten your day:
"From error to error one discovers the entire truth."
- Sigmund Freud

