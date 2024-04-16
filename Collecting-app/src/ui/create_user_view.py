import tkinter as ttk
from tkinter import ttk, StringVar, constants
from services.user_service import user_service, UsernameExistsError


class CreateUserView:
    def __init__(self, root, handle_create_user, handle_cancel):
        print("CreateUserView __init__() method")
        self.root = root
        self._handle_create_user = handle_create_user
        self._handle_cancel = handle_cancel

        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self.initialize()
    
    def pack(self):
        self._frame.pack(fill='both', expand=True)

    def destroy(self):
        self._frame.destroy()


    def _handle_create_user(self):
        # Haetaan syötetyt käyttäjätunnus ja salasana
        username = self._username_entry.get()
        password = self._password_entry.get()

        # Tarkistetaan, että käyttäjätunnus ja salasana ovat kelvollisia (voit lisätä oman tarkistuslogiikkasi tähän)
        if username and password:
            # Kutsutaan handle_create_user -funktiota ja välitetään sille luodut käyttäjätunnus ja salasana
            self._handle_create_user(username, password)
        else:
            # Jos käyttäjätunnus tai salasana puuttuu, näytetään virheviesti
            print("Syötä käyttäjätunnus ja salasana")

    
    def initialize(self):
        if self._frame is None:
            self._frame = ttk.Frame(master=self._root)

            self._username_label = ttk.Label(master=self._frame, text="Uusi käyttäjätunnus:")
            self._username_label.grid(row=0, column=0, sticky='e')

            self._username_entry = ttk.Entry(master=self._frame)
            self._username_entry.grid(row=0, column=1, sticky='w')

            self._password_label = ttk.Label(master=self._frame, text="Uusi salasana:")
            self._password_label.grid(row=1, column=0, sticky='e')

            self._password_entry = ttk.Entry(master=self._frame, show='*')
            self._password_entry.grid(row=1, column=1, sticky='w')

            self._create_button = ttk.Button(master=self._frame, text="Luo käyttäjä", command=self._handle_create_user)
            self._create_button.grid(row=2, column=0, columnspan=2, pady=10)

            self._cancel_button = ttk.Button(master=self._frame, text="Peruuta", command=self._handle_cancel)
            self._cancel_button.grid(row=3, column=0, columnspan=2)

            self._frame.pack()