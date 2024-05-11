from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """Käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: tietokantayhteys.
        """

        self._connection = connection

    def add_user(self, new_user):
        """Lisää uuden käyttäjän tietokantaan.

        Args:
            new_user (User): User-olio, joka sisältää käyttäjän tiedot.

        Returns:
            User: Tietokantaan lisätty käyttäjä-olio.
        """

        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (new_user.username, new_user.password))
        self._connection.commit()
        return new_user

    def find_by_username(self, username):
        """Etsii käyttäjän käyttäjänimen perusteella.

        Args:
            username (str): Etsittävä käyttäjänimi.

        Returns:
            User|None: Löydetty käyttäjä-olio tai None, jos käyttäjää ei löydy.
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

        rows = cursor.fetchone()

        if rows:
            return User(rows["username"], rows["password"])
        else:
            return None

    def find_user(self, username, password):
        """Etsii käyttäjän käyttäjänimen ja salasanan perusteella tietokannasta.

        Args:
            username (str): Käyttäjänimi.
            password (str): Salasana.

        Returns:
            User|None: Löydetty käyttäjä-olio tai None, jos käyttäjää ei löydy.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        row = cursor.fetchone()
        if row:
            return User(row["username"], row["password"])
        else:
            return None


    def remove_user_by_username(self, username):
        """Poistaa käyttäjän tietokannasta käyttäjätunnuksen perusteella.

        Args:
            username (int): Käyttäjän yksilöivä tunniste.
        """
 
        cursor = self._connection.cursor()    
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        self._connection.commit()



        

user_repository = UserRepository(get_database_connection())
