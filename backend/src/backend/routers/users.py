from typing import Annotated
from fastapi import APIRouter, Depends

from backend.models import User
from backend.routers.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
