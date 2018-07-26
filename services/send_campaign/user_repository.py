from src.models.users.user import User


class UserRepository(object):
    def __init__(self, user_model: User):
        self.user_model = user_model

    def users_list(self):
        return self.user_model.query.all()