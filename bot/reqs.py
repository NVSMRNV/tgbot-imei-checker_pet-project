import json
from decouple import config
from requests import request


API_BASE_URL = config('API_BASE_URL', cast=str)


def create_imei_check(imei: str, service: int=22) -> list:
    url = f'{API_BASE_URL}/api/checks/'
    token = get_user_token()
    headers = {
        'Authorization': token, 
        'Content-Type': 'application/json',
    }
    body = json.dumps({
        'deviceId': 'imei',
        'serviceId': service
    })

    response = request(
        method='POST',
        url=url,
        headers=headers,
        data=body
    )

    return response.json()


def get_services_list():
    url = f'{API_BASE_URL}/api/services/'
    token = get_user_token()
    headers = {
        'Authorization': token, 
        'Content-Type': 'application/json',
    }
    response = request(
        method='GET',
        url=url,
        headers=headers,
    )

    return response.json()