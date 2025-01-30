from reqs import accept_user


def is_user_allowed_by_id(uid: int) -> bool:
    user = accept_user(uid=uid)

    if 'error' not in user:
       return True
    return False


def is_imei_valid(imei: str) -> bool:
    return imei.isdigit() and len(imei) == 15

