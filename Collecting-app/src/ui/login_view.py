from tkinter import ttk, constants, StringVar
from services.user_service import user_service, InvalidCredentialsError

class LoginView:
    """Käyttäjän rekisteröitymisestä vastaava näkymä."""

    def __init__(self, root, handle_login, handle_show_create_user_view):
        """Luokan konstruktori, joka alustaa kirjautumisnäkymän.

        Args:
            root (Tk): Pääikkunan viite, johon tämä näkymä piirretään.
            handle_login (function): Käyttäjänäkymä, kutsutaan, kun käyttäjä on kirjautunut onnistuneesti.
            handle_show_create_user_view (function): Kutsutaan, kun käyttäjä haluaa siirtyä rekisteröitymisnäkymään.
        """

        self._handle_show_create_user_view = handle_show_create_user_view
        self._handle_login = handle_login

        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self.initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def _login(self):
        """kirjautua sisään käyttäjätunnuksella.

        Noutaa käyttäjänimen ja salasanan syötekentistä ja kirjautua sisään.
        Jos kirjautuminen onnistuu, käyttäjä siirry käyttäjänäkymään. Jos kirjautuminen
        epäonnistuu, näyttää virheviestin.
        """

        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user = user_service.login(username, password)
            self._handle_login(user)

        except InvalidCredentialsError:
            self._show_error("Virheellinen käyttäjätunnus tai salasana")

    def _show_error(self, message):
        """Näyttää virheviestin käyttäjälle.

        Args:
            message (str): Virheviesti, joka näytetään.
        """

        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """Piilottaa virheviestin näkymästä.
        """

        self._error_label.grid_remove()

    def initialize(self):
        if self._frame is None:
            self._frame = ttk.Frame(master=self._root)

            self._error_variable = StringVar(self._root)

            self._username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus:")
            self._username_label.grid(padx=5,pady=5)
            self._username_entry = ttk.Entry(master=self._frame)
            self._username_entry.grid(row=0, column=1, sticky=(constants.E, constants.W))

            self._password_label = ttk.Label(master=self._frame, text="Salasana:")
            self._password_label.grid(row=2, column=0, sticky=constants.E)
            self._password_entry = ttk.Entry(master=self._frame, show="*")
            self._password_entry.grid(row=2, column=1, sticky=constants.W)

            self._login_button = ttk.Button(master=self._frame, text="Kirjaudu", command=self._login)
            self._login_button.grid(row=3, column=0, columnspan=2, pady=(10, 20))

            self._register_button = ttk.Button(master=self._frame, text="Luo käyttäjätunnus", command=self._handle_show_create_user_view)
            self._register_button.grid(row=4, column=0, columnspan=2)

            self._error_label = ttk.Label(self._frame, textvariable=self._error_variable, foreground='red')
            self._error_label.grid(row=5, column=0, columnspan=2)



            self._frame.pack()
            
