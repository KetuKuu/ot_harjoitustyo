from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    def __init__(self, connection):

        self._connection = connection

def find_user(self, username, password):
    cursor = self._connection.corsor()
    cursor. execute ("SELECT * FROM users WHERE username=?", (username,password))
    row = cursor.fetchone()
    if row is None:
        return False
    return row[1] == username

def add_user(self, user):
    cursor = self._connection.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?,?)",(user.username, user.password,)
    )
    self._connection.commit()
    return user

def find_user_id(self, username):
    cursor = self._connection.cursor()
    cursor.execute("SELECT id FROM user WHERE username=?", (username,))
    row = cursor.fetchone()
    user_id = row[0]
    return user_id

def remove_user(self, user_id):
    cursor = self._connection.cursor()
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
    self._connection.commit()







user_repository = UserRepository(get_database_connection())