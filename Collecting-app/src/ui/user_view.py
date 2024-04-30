import csv
from tkinter import ttk, constants
from services.user_service import user_service
from entities.user import User


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

    

    def _logout_handler(self):
        user_service.logout(self.user) 
        self._handle_logout()
        print("Logout successful")






    def initialize(self):
        #print(f"Welcome {self.user.username}!")


        if self._frame is None:
            self._frame = ttk.Frame(master=self._root)

             # Tervehdysteksti
            self.welcome_label = ttk.Label(self._frame, text=f"Welcome {self.user.username}!")
            self.welcome_label.pack()

  

            self.button_add_project = ttk.Button(self._frame, text="Lisää projekti", command=lambda: self._add_handler(self.user))
            self.button_add_project.pack()

            self.button_project_summary = ttk.Button(self._frame, text="Projektin tilanne", command=self._handle_project_summary)
            self.button_project_summary.pack()

            self.button_logout = ttk.Button(self._frame, text="Kirjaudu ulos", command=self._handle_logout)
            self.button_logout.pack()

        # Pakkaa komponentit kehykseen
            
            self._frame.pack()

        
