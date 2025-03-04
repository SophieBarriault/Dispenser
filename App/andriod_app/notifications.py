# Example code for receiving push notifications and storing them in the app
import json

def receive_push_notification(notification):
    with open('notifications.json', 'r+') as file:
        data = json.load(file)
        data.append(notification)
        file.seek(0)
        json.dump(data, file)
