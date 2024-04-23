from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_user(self, username, password):


        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        row = cursor.fetchone()
        if row:
            return User(row["username"], row["password"])
        else:
            return None


        # Tällä hetkellä kovakoodataan käyttäjätunnus ja salasana
        #if username == "testi" and password == "testi":
            #return User(username, password)
        #else:
            #return None

    def add_user(self, user):

        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user.username, user.password))
        self._connection.commit()

    def find_user_id(self, username):
        # Toteuta käyttäjän etsiminen ID:n perusteella tarvittaessa
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        if rows:
            return User(rows["username"], rows["password"])
        else:
            return None

    def remove_user(self, user_id):

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self._connection.commit()
    
    def create(self, user):
        

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

user_repository = UserRepository(get_database_connection())