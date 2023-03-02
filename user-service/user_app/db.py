import configurations.base_db as base_db
from configurations.base_db import (
    DatabaseConfiguration,
    start_db
)
from .models import User, UpdateUser
import bcrypt
from bson.objectid import ObjectId


class Datebase(DatabaseConfiguration):

    async def hash_password(self, password: str):
        salt = b'$2b$12$BP41xhckoXNw9/fhotVpH.'
        return bcrypt.hashpw(password.encode() , salt)

    @start_db()
    async def get_user(self, user_id):
        query = await base_db.client.user_collection.find_one({"_id": user_id})
        query["_id"] = str(query["_id"])
        query.pop('password')
        return query


    @start_db()
    async def create_user(self, user: User):
        user.password = await self.hash_password(user.password)
        query = await base_db.client.user_collection.insert_one(user.dict())
        result = await self.get_user(query.inserted_id)
        return result

    @start_db()
    async def update_user(self, user_id: str, user: UpdateUser):
        user_update = {}
        for key in user.dict():
            if user.dict()[key]:
                user_update[key] = user.dict()[key]
        await base_db.client.user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_update})
        return await self.get_user(ObjectId(user_id))