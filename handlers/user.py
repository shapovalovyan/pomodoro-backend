from typing import Annotated
from fastapi import APIRouter, Depends

from schema import UserLoginSchema, UserCreateSchema
from service import UserService
from dependecy import get_user_service




router = APIRouter(prefix='/user', tags=['user'])



@router.post('', response_model=UserLoginSchema)
def create_user(
    body: UserCreateSchema,
    user_service: Annotated[UserService, Depends(get_user_service)]
) -> UserLoginSchema:
    
    return user_service.create_user(body.username, body.password)
