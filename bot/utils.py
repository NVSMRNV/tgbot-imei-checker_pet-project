import json
import requests

from decouple import config


WHITELIST = [1172137145, '@GooS69', 'GooS69', '@Rider87', 'Rider87', '@ansukhareva', 'ansukhareva']


def is_user_allowed_by_username(username: str) -> bool:
    return username in WHITELIST


def is_user_allowed_by_id(uid: int) -> bool:
    return uid in WHITELIST


def is_imei_valid(imei: str) -> bool:
    return imei.isdigit() and len(imei) == 15

