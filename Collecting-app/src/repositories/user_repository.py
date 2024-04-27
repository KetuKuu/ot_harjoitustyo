from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection


    def add_user(self,new_user):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_user.username, new_user.password))
        self._connection.commit()
        return new_user

    def find_by_username(self, username):
        # Toteuta käyttäjän etsiminen ID:n perusteella tarvittaessa
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

        rows = cursor.fetchone()

        if rows:
            return User(rows["username"], rows["password"])
        else:
            return None
        
    def find_user(self, username, password):


        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        row = cursor.fetchone()
        if row:
            return User(row["username"], row["password"])
        else:
            return None 


    def remove_user(self, user_id):

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self._connection.commit()
    

user_repository = UserRepository(get_database_connection())