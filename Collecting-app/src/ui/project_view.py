from tkinter import ttk, constants, StringVar, Frame, Label, Button, Listbox

class ProjectView:
    def __init__(self, root, handle_login, handle_add):
        self._root = root
        self._handle_login = handle_login
        self._handle_add = handle_add
        self._frame = None
        self._listbox = None
        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X, expand=True)

    def destroy(self):
        self._frame.destroy()

    def update_list(self):
        self._listbox.delete(0, constants.END)  # Poista vanhat arvot
        # Haetaan uudet tiedot tietokannasta tai sovelluksen tilasta
        updated_data = fetch_phone_data()  # Tämä on esimerkki funktiosta, joka haetaan tietokannasta
        for item in updated_data:
            self._listbox.insert(constants.END, item)




    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # Header label
        header_label = ttk.Label(self._frame, text="Projektien Yhteenveto")
        header_label.pack(fill=constants.X)

        # Listbox to display projects
        self._listbox = Listbox(self._frame, height=10)
        self._listbox.pack(fill=constants.BOTH, expand=True)
        
        # Populate the listbox with sample data (This should be dynamic based on actual data)
        sample_data = ["Nokia 3310 - 2000 - 50", "Nokia 1100 - 2003 - 30"]
        for item in sample_data:
            self._listbox.insert(constants.END, item)

        # Add and Logout Buttons
        add_button = ttk.Button(self._frame, text="Lisää Uusi Puhelin", command=self._handle_add)
        add_button.pack(fill=constants.X)

        logout_button = ttk.Button(self._frame, text="Kirjaudu Ulos", command=self._handle_login)
        logout_button.pack(fill=constants.X)

        self._frame.pack(fill=constants.BOTH, expand=True)
