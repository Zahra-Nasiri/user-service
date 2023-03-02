from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

router = InferringRouter()

@cbv(router)
class UserRouter:

    @router.get("/")
    async def get_sth(self):
        return {"message": "Hello world"}

