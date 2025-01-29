import json
import requests
        
from decouple import config


class CreateIMEICheckservice:
    def __init__(self, inputs=None, *args, **kwargs):
        self.result = None
        self.errors = None
        self.response_status = None
        self.inputs = inputs

    def process(self):
        url = f"{config('IMEICHECK_API_BASEURL', cast=str)}/v1/checks"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {config('IMEICHECK_API_TOKEN_SANDBOX', cast=str)}",
        } 
        body = json.dumps({
            'deviceId': self.inputs['deviceId'],
            'serviceId': self.inputs['serviceId']
        }) 
        response = requests.request(
            method='POST',
            url=url,
            headers=headers,
            data=body
        )
        
        if response.status_code == 201:
            self.result = response.json()
            if isinstance(self.result.get('properties'), list):
                self.result['properties'] = {}
        else:
            self.errors = {'error': 'Не удалось выполнить проверку.', 'details': response.text}
        
        self.response_status = response.status_code
        return self