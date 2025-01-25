import requests


WHITELIST = [1172137145]


def is_user_allowed(uid: int) -> bool:
    return uid in WHITELIST


def is_imei_valid(imei: str) -> bool:
    return imei.isdigit() and len(imei) == 15


def get_imei_info_from_api(imei: str) -> None:
    url = f'http://localhost:8000/api/check-imei/'
    token = ''

    response = requests.post(
        url,
        json={
            'imei': imei
        },
        headers={
            'Authorization': f'Token {token}'
        }
    )

    if response.status_code == 200:
        return response.json()
    return {'error': f'Ошибка запроса: {response.status_code}'}
