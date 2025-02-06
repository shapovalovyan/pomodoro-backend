from dataclasses import dataclass
import random
import string


from repository import UserRepository
from schema import UserLoginSchema


@dataclass
class UserService:

    user_repository: UserRepository
    

    @staticmethod
    def _generate_access_token() -> str:

        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    

    def create_user(self, username: str, password: str ) ->  UserLoginSchema:

        access_token = self._generate_access_token()

        user = self.user_repository.create_user(username=username, password=password, access_token=access_token)

        return UserLoginSchema(user_id=user.id, access_token=access_token)
