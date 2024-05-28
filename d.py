import requests
import json

def send_message(webhook_url, message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message. Status code:", response.status_code)

def main():
    webhook_url = input("Enter the webhook URL: ")
    message = input("Enter the message you want to send: ")
    send_message(webhook_url, message)

if __name__ == "__main__":
    main()
