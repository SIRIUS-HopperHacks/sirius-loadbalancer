from flask import Flask
import requests


class API:
    TARGET_API = ""

    def __init__(self):
        pass

    @classmethod
    def init_app(cls, app: Flask):
        cls.TARGET_API = app.config["TARGET_API"]

    def send_request(self, data):
        response = requests.post(f"{self.TARGET_API}/alert", json=data)
        return response.json()
