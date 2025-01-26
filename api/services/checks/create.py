import json
import requests
        
from decouple import config


class CreateIMEICheckservice:
    def __init__(self, inputs, *args, **kwargs):
        self.result = None
        self.errors = None
        self.response_status = None
        self.inputs = inputs

    def process(self):
        url = f'{config('IMEICHECK_API_BASEURL', cast=str)}/v1/checks'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.inputs['token']}',
        } 
        body = json.dumps({
            'deviceId': self.inputs['imei'],
            'serviceId': 22
        }) 
        response = requests.request(
            method='POST',
            url=url,
            headers=headers,
            data=body
        )
        
        if response.status_code == 201:
            self.result = response.json()
        else:
            self.errors = {'error': 'Failed to create check', 'details': response.text}
        
        self.response_status = response.status_code
        return self