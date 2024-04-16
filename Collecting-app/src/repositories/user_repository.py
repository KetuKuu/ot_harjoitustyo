from entities.user import User


class UserRepository:
    def __init__(self):
        pass
        # Voit lisätä tarvittaessa tänne tietokantayhteyden alustamisen

    def find_user(self, username, password):
        # Tällä hetkellä kovakoodataan käyttäjätunnus ja salasana
        if username == "testi" and password == "testi":
            return User(username, password)
        else:
            return None

    def add_user(self, user):
        # Toteuta käyttäjän lisäys tarvittaessa
        pass

    def find_user_id(self, username):
        # Toteuta käyttäjän etsiminen ID:n perusteella tarvittaessa
        pass

    def remove_user(self, user_id):
        # Toteuta käyttäjän poisto tarvittaessa
        pass


user_repository = UserRepository()