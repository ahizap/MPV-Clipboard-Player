import os
import time
import pyperclip
import threading
import keyboard

def play_url(url):
    command = f'mpv "{url}"'
    os.system(command)

def check_keyboard_input():
    global previous_url, monitoring_active
    while True:
        if keyboard.is_pressed('shift+p'):
            if previous_url:
                print(f"Replaying: {previous_url}")
                play_url(previous_url)
            else:
                print("No previous URL to play.")
        elif keyboard.is_pressed('shift+m'):
            monitoring_active = not monitoring_active
            status = "activated" if monitoring_active else "deactivated"
            print(f"Clipboard monitoring {status}")
        time.sleep(0.1)

previous_url = ""
monitoring_active = True

print("Copy a URL to the clipboard and it will play with MPV.")
print("Press Shift+P to replay.")
print("Press Shift+M to toggle clipboard monitoring on/off.")

# Start the keyboard input checking in a separate thread
keyboard_thread = threading.Thread(target=check_keyboard_input)
keyboard_thread.daemon = True
keyboard_thread.start()

while True:
    if monitoring_active:
        clipboard_url = pyperclip.paste()

        if clipboard_url.startswith("http") and clipboard_url != previous_url:
            previous_url = clipboard_url
            print(f"Playing URL: {clipboard_url}")
            play_url(clipboard_url)

    time.sleep(0.1)
