import os
import requests

INSTANCE_ID = os.environ["INSTANCE_ID"]
API_TOKEN = os.environ["API_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.green-api.com/waInstance{INSTANCE_ID}/sendPoll/{API_TOKEN}"

payload = {
    "chatId": CHAT_ID,
    "message": "Automation Test - What's the plan for Friday? 🙏",
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
