import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        my_id = self.scope['user']
        other_client_id = self.scope["url_route"]["kwargs"]
        username = self.scope["url_route"]["kwargs"].get("username")

        print(other_client_id)
        print(my_id)
        self.accept()
        
        s = f"{my_id} established a connection with {username}"
        self.send(text_data = json.dumps({
            "type":"connection",
            "message":s
        }))
        print(s)

    def receive(self,text_data):
        data = json.loads(text_data)
        message = data['message']
        print("Message from :","=>",message)
        
        self.send(text_data=json.dumps({
            "type":"message_received",
            "message":"Message Received"
        }))

