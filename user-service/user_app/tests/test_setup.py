from configurations.base_test import TestConfiguration
from bson.objectid import ObjectId

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

    def create_fake_user(self):
        return self.user_collection.insert_one(self.fake_user)

    def get_user(self, user_id):
        return self.user_collection.find_one({"_id": ObjectId(user_id)})