"""_summary_
"""

import logging, requests, json

class Wled_Strip():
    def __init__ (self, config):
        # Load the config file values:
        with open(config) as f:
            config = json.load(f)

            self.server_ip = config["server_ip"]
            self.start_time = config["start_time"]
            self.end_time = config["end_time"]
            self.brightness = 0
            self.state = "on"
            self.segment = 0
    
    def update(self):
        # Update the WLED strip
        url = "http://" + self.server_ip + "/json/state"
        payload = json.dumps({
            "on": True,
            "bri": self.brightness,
            "transition": 0,
            "ps": self.preset
        })
        headers = {
            'content-Type': 'application/json'
        }
        response = requests.post(url, data=payload, headers=headers)

    def redlight(self):
        self.brightness = 255
        self.segment = 1
        self.state = "on"
        self.update()
