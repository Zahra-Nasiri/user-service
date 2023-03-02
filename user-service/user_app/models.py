from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    is_admin: bool

class UpdateUser(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    is_admin: str | None = None