import csv
from tkinter import ttk, constants
from services.user_service import user_service
from entities.user import User
from ui.project_view import ProjectView
from services.collecting_service import collecting_service


class UserView:
    def __init__(self, root, user, handle_add_project, handle_project_summary, handle_logout):
        print(" UserView __init__() method")
        self._root = root
        self.user = user
        self._handle_add_project = handle_add_project
        self._handle_project_summary = handle_project_summary
        self._handle_logout = handle_logout

        self._frame = None
        self._username_entry = None
        self._entry = None
        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _add_handler(self, user):
        self._handle_add_project(user)

    def _handler_project(self, user):
        self._handle_project_summary(user)

    def _logout_handler(self):
        user_service.logout()
        self._handle_logout()
        print("Logout successful")

    def update_stats(self):
        stats = collecting_service.get_phone_stats()
        self._stats_label.config(
             text=f"Sinulla on puhelimiä {stats['total_phones']}, ja olet maksanut yhteensä {stats['total_value']} euroa.")

    def initialize(self):
        """ if self.projectView ret == True
            ret = False
                self._handler_project """

        if self._frame is None:
            self._frame = ttk.Frame(master=self._root)

            # Tervehdysteksti
            self.welcome_label = ttk.Label(
                self._frame, text=f"Welcome {self.user.username}!")
            self.welcome_label.pack()

            button_frame = ttk.Frame(self._frame)
            button_frame.pack()

            self.button_add_project = ttk.Button(
                self._frame, text="Lisää projekti", command=lambda: self._add_handler(self.user))
            self.button_add_project.pack(side="left", padx=5)

            self.button_project_summary = ttk.Button(
                self._frame, text="Projektin tilanne", command=lambda: self._handler_project(self.user))
            self.button_project_summary.pack(side="left", padx=5)

            self.button_logout = ttk.Button(
                self._frame, text="Kirjaudu ulos", command=self._logout_handler)
            self.button_logout.pack(side="left", padx=5)

            button_frame.pack(expand=True, pady=10)

            self._stats_label = ttk.Label(self._frame, text="Phone summary")
            self._stats_label.pack(fill=constants.X)

            self.update_stats()

        # Pakkaa komponentit kehykseen
            self._frame.pack()
