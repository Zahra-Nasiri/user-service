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

    def test_user_can_get_user_information_by_token(self):
        query = self.create_fake_user_login_for_token()
        user = self.get_user(query.inserted_id)
        user["_id"] = str(user["_id"])
        token_query = self.create_token(user["_id"])
        token_object = self.get_token(token_query.inserted_id)
        token_object["_id"] = str(token_object["_id"])
        token = token_object["token"]
        response = test_client.get("/", headers={'Authorization': f"Bearer {token}"})
        response = response.json()
        print(response)
        assert response["first_name"] == user["first_name"]
        assert response["last_name"] == user["last_name"]
        assert response["username"] == user["username"]
