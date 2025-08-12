## AutoType

## 📲 MIT App → PC Auto Typing via Flask & PyAutoGUI

This project lets you send text or Python code from a MIT App Inventor mobile app directly to your PC, where it is automatically typed into any active text editor (VS Code, Thonny, etc.) — simulating human keystrokes.

Perfect for:

-> Quickly sending code snippets from your phone to your PC.

-> Avoiding formatting issues from copy-paste in code editors.

-> Real-time control of your PC typing from a mobile interface.

---

## 🚀 How It Works
MIT App Inventor sends a POST request with the text/code to the Flask server running on your PC.

The Flask server:

-> Removes all leading indentation (so the editor auto-indents naturally).

-> Types the text character-by-character using PyAutoGUI.

You see your code appear instantly in your editor.

---

## 📦 Requirements

Python 3.7+

Flask

PyAutoGUI

---

## 📂 Project Structure

auto_code_typer/
│
├── app.py # Main Flask server
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## How To run?

# Install dependencies:

pip install flask pyautogui

# 🖥 Server Setup

Run the Python script on your PC:
  python app.py

The server will run on:
  http://<your-pc-ip>:5000

---

## ⚠️ Notes

This script removes indentation before typing, so your editor’s auto-indent handles formatting.

Works best with Python-friendly editors like VS Code, Thonny, or IDLE.

The active window must be the editor where you want to type — PyAutoGUI sends keystrokes to whichever window is active.

## Screenshots

# Mobile app:
![WhatsApp Image 2025-08-12 at 22 32 42_534499a0](https://github.com/user-attachments/assets/51da8edb-6ea7-49bd-b518-6cd65116a5c7)
