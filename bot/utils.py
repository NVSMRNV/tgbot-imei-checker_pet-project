import json
import requests

from decouple import config


WHITELIST = [1172137145]


def is_user_allowed(uid: int) -> bool:
    return uid in WHITELIST


def is_imei_valid(imei: str) -> bool:
    return imei.isdigit() and len(imei) == 15

