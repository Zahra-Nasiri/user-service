from fastapi.testclient import TestClient
from main import app
from .test_setup import TestSetup

test_client = TestClient(app)

class TestRouter(TestSetup):

    def test_user_can_create_user(self):
        response = test_client.post("/register", json=self.fake_user)
        response = response.json()
        print(response)
        user = self.get_user(response["_id"])
        assert user["username"] == self.fake_user["username"]
        assert user["first_name"] == self.fake_user["first_name"]
        assert user["last_name"] == self.fake_user["last_name"]
        assert user["is_admin"] == self.fake_user["is_admin"]

    def test_user_can_partial_update_user(self):
        query = self.create_fake_user()
        del self.fake_user["_id"]
        response = test_client.patch(
            f"/{query.inserted_id}", json=self.fake_user_update
        )
        response = response.json()
        user = self.get_user(response["_id"])
        assert user["first_name"] == self.fake_user_update["first_name"]
        assert user["last_name"] == self.fake_user_update["last_name"]

    def test_user_can_login(self):
        self.create_fake_user_login()
        response = test_client.post("/login", json=self.fake_user_login)
        response = response.json()
        user = self.get_user(response["uid"])
        assert user["username"] == self.fake_user_login["username"]
