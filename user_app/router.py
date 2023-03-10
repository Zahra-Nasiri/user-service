from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from .models import User, UpdateUser, LoginUser
from .db import Datebase
from fastapi import Header

router = InferringRouter()

db_client = Datebase()

@cbv(router)
class UserRouter:

    @router.post("/register")
    async def register(self, user: User):
        return await db_client.create_user(user)

    @router.patch("/{uid}")
    async def update_user(self, user: UpdateUser, uid:str):
        return await  db_client.update_user(uid, user)

    @router.post("/login")
    async def login(self, user:LoginUser):
        return await db_client.authenticate_user(user)

    @router.get("/")
    async def get_user(self, Authorization: str = Header()):
        token = Authorization.split(" ")[1]
        return await db_client.get_user_by_token(token)
