import os
import requests
from datetime import datetime, timedelta

INSTANCE_ID = os.environ["INSTANCE_ID"]
API_TOKEN = os.environ["API_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# Calculate next Sunday's date
today = datetime.utcnow()
days_until_sunday = (6 - today.weekday()) % 7 or 7
next_sunday = today + timedelta(days=days_until_sunday)
sunday_str = next_sunday.strftime("%-d %b")  # e.g. "14 Jun"

url = f"https://api.green-api.com/waInstance{INSTANCE_ID}/sendPoll/{API_TOKEN}"

payload = {
    "chatId": CHAT_ID,
    "message": f"Mass Sunday {sunday_str} 🙏",
    "multipleAnswers": True,
    "options": [
        {"optionName": "📖 1st Reading"},
        {"optionName": "🎵 Psalm"},
        {"optionName": "📖 2nd Reading + Acclamation"},
        {"optionName": "Bread"},
        {"optionName": "Wine"},
        {"optionName": "Body 1"},
        {"optionName": "Blood 1"},
        {"optionName": "Blood 2"},
        {"optionName": "📢 Announcements"},
    ]
}

response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
print(response.text)
