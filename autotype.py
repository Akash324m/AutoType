from flask import Flask, request, jsonify
import pyautogui
import time
import random

app = Flask(__name__)

def type_like_human(text):
    """Types text with realistic delays and handles special keys."""
    for char in text:
        if char == '\n':
            pyautogui.press('enter')
        elif char == '\t':
            pyautogui.press('tab')
        else:
            pyautogui.write(char)
        time.sleep(random.uniform(0.0001, 0.005))  # Random typing speed

@app.route('/type', methods=['GET'])
def type_text():
    text = request.args.get('text', '')  # Get text from URL (?text=Hello)
    print(f"Received: {text}")  # Debug log 
    
    if not text:
        return jsonify({"status": "error", "message": "No text provided"}), 400
    
    try:
        type_like_human(text)
        return jsonify({"status": "success", "message": f"Typed: '{text}'"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)