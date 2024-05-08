from tkinter import ttk, constants, StringVar, Frame, Label, Button, Listbox, messagebox
from services.collecting_service import collecting_service

class ProjectView:
    def __init__(self, root, user, handle_login, handle_add):
        self._root = root
        self.user =user
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
        self._listbox.delete(0, 'end')

        headers = f"{'Image':<20}{'Series':<15}{'Model Year':<15}{'Price':<10}"#{item['id']}|
        self._listbox.insert(constants.END, headers)
   
        data = collecting_service.fetch_data() 
        
        for item in data:
        
            formatted_row = f"{item['image']:<20}{item['series']:<15}{item['model_year']:<15}{item['price']:<10}"
            self._listbox.insert(constants.END, formatted_row)
        

    def _delete_selected(self):
        selected_indices = self._listbox.curselection()
        if not selected_indices:
            messagebox.showerror("Virhe", "Valitse poistettava rivi.")
            return
        selected_index = selected_indices[0]
        selected_item = self._listbox.get(selected_index)
        phone_id = selected_item.split()[0]  # Oletetaan, että id on ensimmäinen arvo
        print(selected_item)

        if messagebox.askyesno("Vahvista poisto", "Haluatko varmasti poistaa valitun puhelimen?"):
            collecting_service.delete_phone(phone_id)
            print(phone_id)
            self.update_list()



    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

   
        header_label = ttk.Label(self._frame, text="Projektien Yhteenveto")
        header_label.pack(fill=constants.X)


        self._listbox = Listbox(self._frame, height=10)
        self._listbox.pack(fill=constants.BOTH, expand=True)
        

        self.update_list()

        # Buttons
        add_button = ttk.Button(self._frame, text="Lisää Uusi Puhelin", command=self._handle_add)
        add_button.pack(fill=constants.X)

        logout_button = ttk.Button(self._frame, text="Kirjaudu Ulos", command=self._handle_login)
        logout_button.pack(fill=constants.X)

        delete_button = ttk.Button(self._frame, text="Poista Valittu", command=self._delete_selected)
        delete_button.pack(fill=constants.X)

        self._frame.pack(fill=constants.BOTH, expand=True)
