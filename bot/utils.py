import json
import requests

from decouple import config


WHITELIST = [1172137145]


def is_user_allowed(uid: int) -> bool:
    return uid in WHITELIST


def is_imei_valid(imei: str) -> bool:
    return imei.isdigit() and len(imei) == 15


def get_imei_check(imei: str) -> None:
    url = f'http://localhost:8000/api/imeis/checks/'
    headers = {
        'Content-Type': 'application/json'
    }
    body = json.dumps({
        'imei': imei,
        'token': config('IMEICHECK_API_TOKEN_LIVE', cast=str)
    })
    response = requests.request(
        method='POST',
        url=url,
        headers=headers,
        data=body,
    )
    return response.json()


def get_service_list() -> list:
    url = f'http://localhost:8000/api/imeis/services/'
    headers = {
        'Content-Type': 'application/json'
    }
    body = json.dumps({
        'token': config('IMEICHECK_API_TOKEN_LIVE', cast=str)
    })
    response = requests.request(
        method='POST',
        url=url,
        headers=headers,
        data=body,            
    )

    return response.json()
