from configurations.base_test import TestConfiguration
from bson.objectid import ObjectId
import bcrypt

class TestSetup(TestConfiguration):

    def hash_password(password: str):
        salt = b'$2b$12$BP41xhckoXNw9/fhotVpH.'
        return bcrypt.hashpw(password.encode() , salt)

    fake_user = {
        "username": "test user",
        "password": "a123gsdga3423",
        "first_name": "test first_name",
        "last_name": "test last_name",
        "is_admin": False
    }

    fake_user_update = {
        "first_name": "updated first_name",
        "last_name": "updated last_name"
    }

    fake_user_login = {
        "username": "myuserloginname",
        "password": "a123gsdga3423"
    }

    fake_user_create = {
        "username": "myuserloginname",
        "password": hash_password("a123gsdga3423"),
        "first_name": "test first_name",
        "last_name": "test last_name"
    }

    def create_fake_user(self):
        return self.user_collection.insert_one(self.fake_user)

    def get_user(self, user_id):
        return self.user_collection.find_one({"_id": ObjectId(user_id)})

    def create_fake_user_login(self):
        return self.user_collection.insert_one(self.fake_user_create)