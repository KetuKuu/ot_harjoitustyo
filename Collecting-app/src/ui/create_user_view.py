import tkinter as ttk
from tkinter import ttk, StringVar, constants
from services.user_service import user_service, UsernameExistsError


class CreateUserView:
    def __init__(self, root, handle_show_user_view, handle_show_login_view):
        print("CreateUserView __init__() method")
        self._root = root
        self._handle_show_user_view = handle_show_user_view
        self._handle_show_login_view = handle_show_login_view
        
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = StringVar()

        self.initialize()
    
    def pack(self):
        self._frame.pack(fill='both', expand=True)

    def destroy(self):
        self._frame.destroy()


    def _register_user(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if username and password:
            try:
                user = user_service.create_user(username, password)  # Luodaan käyttäjä
                print("_register_user, Kirjauduminen onnistui")
                self._handle_show_user_view(user)  # Siirry käyttäjänäkymään onnistuneen rekisteröinnin jälkeen
            except UsernameExistsError:
                self._error_variable.set("Käyttäjätunnus on jo käytössä")
                print("_register_user, käyttäjätunnus käytössä")
        else:
            self._error_variable.set("Syötä käyttäjätunnus ja salasana")

    
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

            self._password_label = ttk.Label(master=self._frame, text="Uusi salasana:")
            self._password_label.grid(row=1, column=0, sticky='e')

            self._password_entry = ttk.Entry(master=self._frame, show='*')
            self._password_entry.grid(row=1, column=1, sticky='w')

            self._create_button = ttk.Button(master=self._frame, text="Luo käyttäjä", command=self._register_user)
            self._create_button.grid(row=2, column=0, columnspan=2, pady=10)

            self._cancel_button = ttk.Button(master=self._frame, text="Peruuta", command=self._handle_show_login_view)
            self._cancel_button.grid(row=3, column=0, columnspan=2)

            self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable, foreground="red")
            self._error_label.grid(row=4, column=0, columnspan=2)  

            self._frame.pack()