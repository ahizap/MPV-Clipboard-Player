import os
import time
import pyperclip


def play_url(url):
    command = f'mpv "{url}"'
    os.system(command)


previous_url = ""

print("Copy a URL to the clipboard and it will play with MPV.")

while True:
   
    clipboard_url = pyperclip.paste()

 
    if clipboard_url.startswith("http") and clipboard_url != previous_url:
        previous_url = clipboard_url
        print(f"Playing URL: {clipboard_url}")
        play_url(clipboard_url)

 
    time.sleep(2)
