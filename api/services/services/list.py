import requests
from decouple import config


class ListIMEIServiceService:
    def __init__(self, inputs=None, *args, **kwargs):
        self.result = None
        self.errors = None
        self.response_status = None
        self.inputs = inputs

    def process(self):
        url = f'{config('IMEICHECK_API_BASEURL', cast=str)}/v1/services'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config('IMEICHECK_API_TOKEN_LIVE', cast=str)}',
            'Accept-Language': 'en',
        }   
        response = requests.request(
            method='GET', 
            url=url, 
            headers=headers
        )

        if response.status_code == 200:
            self.result = response.json()
        else:
            self.errors = {'error': 'Не удалось получить список сервисов.', 'details': response.text}
        
        self.response_status = response.status_code
        return self
