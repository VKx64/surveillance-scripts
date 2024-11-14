from flask import Flask, jsonify
import pyautogui
import datetime
import os
from helper_functions import *

app = Flask(__name__)

def create_required_folders():
    os.makedirs("contents/screenshots", exist_ok=True) 

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
    
@app.route('/screenshot', methods=['GET'])
def screenshot_endpoint():
    file_name = take_screenshot()
    if file_name:
        return jsonify({"message": "Screenshot taken successfully", "file_path": file_name}), 200
    else:
        return jsonify({"message": "An error occurred while taking the screenshot"}), 500
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)