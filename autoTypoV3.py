from flask import Flask, request, jsonify
import pyautogui
import time
import random
import json
from urllib.parse import unquote

app = Flask(__name__)

def type_like_human(text):
    lines = text.splitlines()
    for line in lines:
        pyautogui.write(line, interval=0.1)  # type line slowly
        pyautogui.press('enter')


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