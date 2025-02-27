from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, Request, Security
from sqlalchemy.orm import Session
from fastapi import security

from database import get_db_session
from cache import get_redis_connection
from exception import TokenExpired, TokenNotCorrect
from repository import TaskRepository, TaskCache, UserRepository
from service import TaskService, UserService, AuthService
from settings import Settings



def get_tasks_repository(db_session: Session = Depends(get_db_session)) -> TaskRepository:

    return TaskRepository(db_session)


def get_tasks_cashe_repository() -> TaskCache:

    redis_connection = get_redis_connection()

    return TaskCache(redis_connection)


def get_task_service(
        task_repository: TaskRepository = Depends(get_tasks_repository),
        task_cache: TaskCache = Depends(get_tasks_cashe_repository)
) -> TaskService:

    return TaskService(
        task_repository=task_repository,
        task_cache=task_cache
    )



def get_user_repository(
        db_session: Session = Depends(get_db_session)
) -> UserRepository:
    
    return UserRepository(db_session=db_session)





def get_auth_service(
        user_repository: UserRepository = Depends(get_user_repository)
) -> AuthService:
    
    return AuthService(user_repository=user_repository, settings=Settings())


def get_user_service(
        user_repository: UserRepository = Depends(get_user_repository),
        auth_service: AuthService = Depends(get_auth_service)
) -> UserService:
    
    return UserService(user_repository=user_repository, auth_service=auth_service)

reusable = security.HTTPBearer()


def get_request_user_id(
        auth_service: AuthService = Depends(get_auth_service),
        token: HTTPAuthorizationCredentials = Security(reusable)) -> int:
    

    try:
        user_id = auth_service.generate_user_id_access_token(token.credentials)

    except TokenExpired as exc:
        raise HTTPException(
            status_code=401,
            detail=exc.detail
        )
    except TokenNotCorrect as exc:
        raise HTTPException(
            status_code=401,
            detail=exc.detail
        )
    
    return user_id