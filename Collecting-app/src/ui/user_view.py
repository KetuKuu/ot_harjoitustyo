from tkinter import ttk, constants
from services.user_service import user_service
from services.collecting_service import collecting_service


class UserView:
    """Käyttäjän näkymästä vastaava näkymä."""

    def __init__(self, root, user, handle_add_project, handle_project_view, handle_logout):
        """Luokan konstruktori.

        Args:
            user: käyttäjäolio, jolle näkymä liitty.
            handle_add_project: Kutusttava funktio projektin lisämiseen.
            handle_project_viewr: Kutsuttava funktio näyttää projekti näkymään.
            handle_logout: Funktio ulos kirjautumista varten.

        """
        self._root = root
        self.user = user
        self._handle_add_project = handle_add_project
        self._handle_project_view = handle_project_view
        self._handle_logout = handle_logout

        self._frame = None
        self._username_entry = None
        self._entry = None
        self._stats_label = None
        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _add_handler(self, user):
        """sisään kirjautunut käyttäjä näkee ja hallitse projektin lisäämisen """
        self._handle_add_project(user)

    def _handler_project(self, user):
        """sisään kirjautunut käyttäjä näkee ja hallitse projektin näkymään """
        self._handle_project_view(user)

    def _logout_handler(self):
        user_service.logout()
        self._handle_logout()
     

    def update_stats(self):
        """Yhteenvetoon päivitys käyttäjäsivulle"""
        stats = collecting_service.get_phone_stats()
        self._stats_label.config(
             text=f"Sinulla on puhelimiä {stats['total_phones']}, ja olet maksanut yhteensä {stats['total_value']} euroa.")

    def initialize(self):
        """Näkymän käsittely"""
        if self._frame is None:
            self._frame = ttk.Frame(master=self._root)

            # Tervehdysteksti
            self.welcome_label = ttk.Label(
                self._frame, text=f"Tervetuloa {self.user.username}!")
            self.welcome_label.pack()


            button_frame = ttk.Frame(self._frame)

            # Napit
            self.button_add_project = ttk.Button(
                button_frame, text="Lisää projekti", command=lambda: self._add_handler(self.user))
            self.button_add_project.pack(side="left", padx=5)

            self.button_project_summary = ttk.Button(
                button_frame, text="Projektin tilanne", command=lambda: self._handler_project(self.user))
            self.button_project_summary.pack(side="left", padx=5)

            self.button_logout = ttk.Button(
                button_frame, text="Kirjaudu ulos", command=self._logout_handler)
            self.button_logout.pack(side="left", padx=5)

            button_frame.pack(expand=True, pady=(10, 50))

    
            #Label
            stats_label_frame = ttk.Frame(self._frame)
            
            self._stats_label = ttk.Label(stats_label_frame, text="")
            self._stats_label.pack()

            stats_label_frame.pack()
            self.update_stats()

        self._frame.pack()
