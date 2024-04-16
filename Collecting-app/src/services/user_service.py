from repositories.user_repository import user_repository
from entities.user import User


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass

class UserService:
    
    def __init__(self, user_repository):
        print(" UserService __init__() method")
        self.user_repository = user_repository

    def login(self, username, password):
        print(" Userservice Login() method")
      
        user = self.user_repository.find_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        
        self._user = user

        return user
    
    def logout(self):
        self._user =None

    def delete_user(self, user):
        user:id = user.get_user_id()


user_service = UserService(user_repository)