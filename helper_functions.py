import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_image_to_discord(file_name):
    try:
        with open(file_name, "rb") as f:
            result = requests.post(WEBHOOK_URL, files={"file": f})
        if 200 <= result.status_code < 300:
            print("Screenshot sent to Discord successfully!")
        else:
            print(f"Failed to send screenshot. Status code: {result.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
