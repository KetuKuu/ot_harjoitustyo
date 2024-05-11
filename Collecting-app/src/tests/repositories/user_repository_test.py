import unittest
from entities.user import User
from database_connection import get_database_connection_test
from repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):

        self.connection = get_database_connection_test()
        self.user_repository = UserRepository(self.connection)


    def test_add_user(self):
        new_user = User("Matti", "salasana")
        
        add_user = self.user_repository.add_user(new_user)
    
        response = self.user_repository.find_by_username("Matti")      
        
        self.assertIsNotNone(response)
        self. assertEqual(response.username, add_user.username)

        self.user_repository.remove_user_by_username("Matti")

   

    def test_find_user_when_exists(self):
        
        response = self.user_repository.find_user("testi", "testi")
        self.assertIsNotNone(response)

    def test_find_user_when_doesent_exist(self):
        response = self.user_repository.find_user("kalle","salasana")
        self.assertEqual(response, None)
        
