from api.models.users import User
from django.core.exceptions import ObjectDoesNotExist


class CurrentUserService:
    def __init__(self, inputs=None, *args, **kwargs):
        self.result = None
        self.errors = None
        self.response_status = None
        self.inputs = inputs

    def process(self):
        try:
            self.result = User.objects.get(uid=self.inputs['uid'])
            self.response_status = 200
        except ObjectDoesNotExist:
            self.errors = {
                'error': 'Пользователь не найден.', 
                'details': f"Пользователь с uid={self.inputs['uid']} не существует."
            }
            self.response_status = 404

        return self