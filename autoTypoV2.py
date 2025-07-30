from flask import Flask, request, jsonify
import pyautogui
import time
import random
import json
from urllib.parse import unquote

app = Flask(__name__)

def type_like_human(text):
    """Types text with realistic delays and special character handling."""
    for char in text:
        if char == '\n':
            pyautogui.press('enter')
        elif char == '\t':
            pyautogui.press('tab')
        elif char in r"""!@#$%^&*()_+-=[]{}|;':",./<>?""":
            pyautogui.write(char, interval=random.uniform(0.01, 0.02))
        else:
            pyautogui.write(char)
        time.sleep(random.uniform(0.01, 0.03))

# @app.route('/type', methods=['POST'])
# def type_text():
#     text = request.form.get('text', '')
#     print(f"[RECEIVED]: {repr(text)}")

#     if not text:
#         return jsonify({"status": "error", "message": "No text provided"}), 400

#     try:
#         type_like_human(text)
#         return jsonify({"status": "success", "message": f"Typed: '{text}'"})
#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/type', methods=['POST'])
def type_text():
    text = request.form.get('text', '')
    print(f"[RECEIVED]: {repr(text)}")

    if not text:
        return jsonify({"status": "error", "message": "No text provided"}), 400

    try:
        type_like_human(text)
        return jsonify({"status": "success", "message": f"Typed: '{text}'"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)