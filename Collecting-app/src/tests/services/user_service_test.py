import unittest
from services.user_service import UserService
from entities.user import User
from repositories.user_repository import UserRepository
from database_connection import get_database_connection_test
from services.user_service import InvalidCredentialsError, UsernameExistsError, InvalidInputError

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository(get_database_connection_test())
        self.user_service = UserService(self.user_repository)
        self.user = User("testi", "testi" )

    
    def test_login_valid_user(self):
        response = self.user_service.login("testi", "testi")
        valid = isinstance(response,User)

        self.assertEqual(valid,True)


    def test_login_invalide_user(self):    

        self.assertRaises(InvalidCredentialsError, lambda:self.user_service.login("test", "testii"))    


    def test_logout(self):
        response = self.user_service.logout()
        self.assertEqual(response, None)


    def test_create_existing_username(self):
        username = self.user.username
        self.assertRaises(UsernameExistsError, lambda:self.user_service.create_user(username, "random"))


    def test_create_if_username_too_long(self):
        self.user_service.logout()
        self.assertRaises(InvalidInputError, lambda:self.user_service.create_user("tamaonliianpitkakayttajatunnus", "random") )


    def test_create_if_username_too_short(self):
        self.user_service.logout()
        self .assertRaises(InvalidInputError, lambda:self.user_service.create_user("lyh", "random"))
   