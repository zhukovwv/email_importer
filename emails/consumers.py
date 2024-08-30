import json
from channels.generic.websocket import WebsocketConsumer
from .models import EmailMessage
from .utils import fetch_emails


class EmailConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)
        email = data.get('email')
        password = data.get('password')
        provider = data.get('provider')

        messages = fetch_emails(email, password, provider)
        for msg in messages:
            self.send(text_data=json.dumps(msg))

    def disconnect(self, close_code):
        pass
