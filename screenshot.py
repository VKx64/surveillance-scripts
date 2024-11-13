import pyautogui
import datetime
import os
from helper_functions import *

def generate_file_name():
    now = datetime.datetime.now()
    return f"SCREENSHOT-{now.month:02d}-{now.day:02d}-{now.year % 100:02d}-{now.hour:02d}-{now.minute:02d}.png"

def take_screenshot():
    try:
        filename = f"contents/screenshots/{generate_file_name()}"
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        print(f"Screenshot saved {filename}")
        return filename
    except Exception as e:
        print(f"An error occurred while taking the screenshot: {e}")
        return None

if __name__ == "__main__":
    os.makedirs("contents/screenshots", exist_ok=True) 
    file_name = take_screenshot()
    send_image_to_discord(file_name)