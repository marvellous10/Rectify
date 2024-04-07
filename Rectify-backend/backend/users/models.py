from mongoengine import *


class UserSession(Document):
    session_id = StringField(required=True, unique=True)
    spotify_user_id = StringField()
    spotify_user_name = StringField()
    access_token = StringField()
    refresh_token = StringField()
