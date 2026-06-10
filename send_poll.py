import os
import requests

INSTANCE_ID = os.environ["INSTANCE_ID"]
API_TOKEN = os.environ["API_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.green-api.com/waInstance{INSTANCE_ID}/sendPoll/{API_TOKEN}"

payload = {
    "chatId": CHAT_ID,
    "message": "What's the plan for Friday? 🙏",
    "multipleAnswers": False,
    "options": [
        {"optionName": "🍞 Bread"},
        {"optionName": "🍷 Wine"},
        {"optionName": "📖 1st reading"},
        {"optionName": "📖 2nd reading"},
    ]
}

response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
print(response.text)
