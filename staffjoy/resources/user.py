from ..resource import Resource
from .session import Session
from .apikey import ApiKey


class User(Resource):
    PATH = "users/{user_id}"
    ID_NAME = "user_id"

    def get_sessions(self):
        return Session.get_all(parent=self)

    def get_session(self, id):
        return Session.get(parset=self, id=id)

    def get_apikeys(self):
        return ApiKey.get_all(parent=self)

    def get_apikey(self, id):
        return ApiKey.get(parent=self, id=id)
