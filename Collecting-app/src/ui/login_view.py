from tkinter import ttk, constants, StringVar
from ui.user_view import UserView
from services.user_service import user_service, InvalidCredentialsError



class LoginView:
    def __init__(self, root, handle_login, handle_show_create_user_view):
        print(" LoginView __init__() method")
        self._handle_show_create_user_view = handle_show_create_user_view # rekisteröitymisnäkymään.
        self._handle_login = handle_login

        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self.initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    

    def destroy(self):
        self._frame.destroy()

    def _login(self):

        username = self._username_entry.get()
        password = self._password_entry.get()
        print("Kirjaudu:", username, password)
        
        try:
            user = user_service.login(username, password)
            print("Login successful")
            #self._handle_login(user)
            self._handle_show_user_view(user) 
        except InvalidCredentialsError:
            self._show_error("Invalid username or password")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _handle_register(self):
        print("Luo käyttäjätunnus")


    def initialize(self):
        #print("Tervetuloa käyttäjänäkymään!")

        #welcome_label = ttk.Label(master=self._root, text="Tervetuloa Nokiin!")
        #welcome_label.pack()
        if self._frame is None:
            self._frame = ttk.Frame(master=self._root)
            self._error_variable = StringVar(self._root)
            

            self._username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus:")
            self._username_label.grid(row=0, column=0, sticky=constants.E)
            self._username_entry = ttk.Entry(master=self._frame)
            self._username_entry.grid(row=0, column=1, sticky=constants.W)

            self._password_label = ttk.Label(master=self._frame, text="Salasana:")
            self._password_label.grid(row=1, column=0, sticky=constants.E)
            self._password_entry = ttk.Entry(master=self._frame, show="*")
            self._password_entry.grid(row=1, column=1, sticky=constants.W)

            #self._login_button = ttk.Button(master=self._frame, text="Kirjaudu", command=UserView)
            self._login_button = ttk.Button(master=self._frame, text="Kirjaudu", command=self._login)
            self._login_button.grid(row=2, column=0, columnspan=2, pady=10)

            self._register_button = ttk.Button(master=self._frame, text="Luo käyttäjätunnus", command=self._handle_show_create_user_view)
            self._register_button.grid(row=3, column=0, columnspan=2)

            self._error_label = ttk.Label(self._frame, textvariable=self._error_variable, foreground='red')
            self._error_label.grid(row=4, column=0, columnspan=2)
            
            self._frame.pack()
