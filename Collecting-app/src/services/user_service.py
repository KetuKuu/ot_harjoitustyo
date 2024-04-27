from repositories.user_repository import user_repository
from entities.user import User
import re

class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass

class InvalidInputError(Exception):
    pass

class UserService:
    
    def __init__(self, user_repository):
        print(" UserService __init__() method")
        self.user_repository = user_repository


    def create_user(self, username: str, password: str):
        existing_user = self.user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")
        
        if len(username) < 4 or len(username) >20:
            raise InvalidInputError("Käyttäjätunnuksen on oltava vähintään 4 merkkiä pitkä.")
        
        new_user = User(username, password)

        new_user = User(username, password)
        self.user_repository.add_user(new_user)
        return new_user

    def login(self, username, password):
        print(" Userservice Login() method")
      
        user =self.user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        
        self._user = user

        return user
    #todo create user
    

    def logout(self):
        self._user =None

    def _validate_username(self, username):
        return len(username) >= 4

    def _validate_password(self, password):
        return len(password) >= 4 

    def delete_user(self, user):
        user:id = user.get_user_id()

    


user_service = UserService(user_repository)