import json
from decouple import config
from requests import request


API_BASE_URL = config('API_BASE_URL', cast=str)

def current_user(uid: int) -> dict:
    url = f'{API_BASE_URL}/api/users/?uid={uid}'
    headers = {
        'Content-Type': 'application/json',
    }
    response = request(
        method='GET',
        url=url,
        headers=headers,
    )

    return response.json()


def create_user(uid: int) -> dict:
    url = f'{API_BASE_URL}/api/users/'
    headers = {
        'Content-Type': 'application/json',
    }
    body = json.dumps({
        'uid': uid
    })
    response = request(
        method='POST',
        url=url,
        headers=headers,
        data=body,
    )

    return response.json()


def create_imei_check(imei: str, uid: int, service=15) -> list:
    url = f'{API_BASE_URL}/api/checks/'
    token = current_user(uid=uid)['token']

    headers = {
        'Authorization': f'Bearer {token}', 
        'Content-Type': 'application/json',
    }
    body = json.dumps({
        'deviceId': imei,
        'serviceId': service
    })

    response = request(
        method='POST',
        url=url,
        headers=headers,
        data=body
    )

    return response.json()


def get_service_list(uid):
    url = f'{API_BASE_URL}/api/services/'
    token = current_user(uid=uid)['token']
    headers = {
        'Authorization': f'Bearer {token}',  
        'Content-Type': 'application/json',
    }
    response = request(
        method='GET',
        url=url,
        headers=headers,
    )

    return response.json()