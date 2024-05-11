class User:
    """Luokka kuvaa yksittäistä käyttäjä

    Attributes:
        username: Merkkijono, kuivailee käyttäjätunnusta
        password: Merkkijono, kuvailee salasana
    """

    def __init__(self, username, password):
        """Luokan konstruktori käyttäälle

        Args:
        username: Merkkijono, kuivailee käyttäjätunnusta
        password: Merkkijono, kuvailee salasana


        """

        self.username = username
        self.password = password


