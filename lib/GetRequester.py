import requests
import json

class GetRequester:

    def __init__(self, url):
        # initializes requester with a target API url
        self.url = url

    def get_response_body(self):
        # Sends an HTTP GET request and returns raw bytes content
        response = requests.get(self.url)
        return response.content
    
    def load_json(self):
        # Fetches raw data, deserialziing it into a python object
        raw_text = self.get_response_body()
        data = json.loads(raw_text)
        return data