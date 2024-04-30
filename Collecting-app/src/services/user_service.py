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
    """Luokka, jonka avulla toteutetaan käyttäjiin liittyvä sovelluslogiikka.

    Attributes:
        user_repository: UserRepository-olion UserRepository-luokasta
        
    """

    def __init__(self, user_repository):
        """Luokan konstruktori, joka luo Service-olion.
            Argumenttina annettava repositori tuodaan sen omista luokista.

            Args:
                user_repository: user_repository
                current_user (User): Kirjautunut käyttäjä, oletusarvo None.
        """

        
        self.user_repository = user_repository
        self.current_user = None


    def create_user(self, username: str, password: str):       
        """Luo uuden käyttäjän annetulla käyttäjänimellä ja salasanalla.

        Args:
            username (str): Uuden käyttäjän käyttäjänimi.
            password (str): Uuden käyttäjän salasana.

        Returns:
            User: Juuri luotu käyttäjä-olio.

        Raises:
            UsernameExistsError: Jos käyttäjänimi on jo käytössä.
            InvalidInputError: Jos käyttäjänimi ei täytä vaadittuja ehtoja.
        """

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
        """Kirjaa käyttäjän sisään annetulla käyttäjänimellä ja salasanalla.

        Args:
            username (str): KMerkkijonoarvo, joka kuvaa kirjautuvan käyttäjän käyttäjätunnusta.
            password (str): Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän salasanaa.

        Returns:
            User: Kirjautunut käyttäjä-olio.

        Raises:
            InvalidCredentialsError: Jos käyttäjänimi tai salasana eivät täsmää.
        """
        
      
        user = self.user_repository.find_user(username, password)
        if user and user.password == password:
            self.current_user = user
            return user
        raise InvalidCredentialsError("Invalid username or password")

    
    def get_current_user(self):         
        """Palauttaa tällä hetkellä kirjautuneen käyttäjän.

        Returns:
            User: Tällä hetkellä kirjautunut käyttäjä, tai None jos kukaan ei ole kirjautuneena.
        """

        return self.current_user


    def logout(self):
        """Kirjaa nykyisen käyttäjän ulos.
        """

        self.current_user =None
        print("logout")

    

    def _validate_username(self, username):               
        """Tarkistaa onko käyttäjänimi kelvollinen.

        Args:
            username (str): Tarkistettava käyttäjänimi.

        Returns:
            bool: True, jos käyttäjänimi on kelvollinen, muuten False.
        """

        return len(username) >= 4

    def _validate_password(self, password):
        """Tarkistaa onko salasana kelvollinen.

        Args:
            password (str): Tarkistettava salasana.

        Returns:
            bool: True, jos salasana on kelvollinen, muuten False.
        """

        return len(password) >= 4 
    


    def delete_user(self, user):
        """Poistaa käyttäjän järjestelmästä.

        Args:
            user (User): Poistettava käyttäjä.
        """

        user:id = user.get_user_id()

    


user_service = UserService(user_repository)