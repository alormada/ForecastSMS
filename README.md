# ☔ Weather Forecast SMS Notifier

This Python script checks the weather forecast using OpenWeatherMap API and sends a summary of the upcoming hours via SMS using the Twilio API. If rain is predicted, you’ll be alerted immediately.

---

## 📌 Features

- Checks weather for the next few hours for a specific location
- Detects if rain is forecasted
- Sends SMS notifications with temperature and rain alert
- Configurable via environment variables

---

## 🛠️ Technologies Used

- Python 3
- [OpenWeatherMap API](https://openweathermap.org/forecast5)
- [Twilio API](https://www.twilio.com/)
- `.env` for managing API keys securely
- `requests` for HTTP communication

---

## 🔐 Environment Variables

Create a `.env` file with the following content:

```env
# Twilio
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
PHONE_NUMBER=your_target_phone_number

# Weather
OWM_API_KEY=your_openweathermap_api_key

