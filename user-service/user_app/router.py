from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from .models import User, UpdateUser
from .db import Datebase

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