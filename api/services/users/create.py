from api.models.users import User


class CreateUserService:
    def __init__(self, inputs=None, *args, **kwargs):
        self.result = None
        self.errors = None
        self.response_status = None
        self.inputs = inputs

    def process(self):
        self.result = User.objects.create_user(
            uid=self.inputs['uid'],
            password=self.inputs['uid']
        )
        self.response_status = 201
        return self
