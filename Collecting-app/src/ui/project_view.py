from tkinter import ttk, constants, StringVar, Frame, Label, Button, Listbox, messagebox
from services.collecting_service import collecting_service
from PIL import Image, ImageTk 

class ProjectView:
    def __init__(self, root, user, handle_login, handle_add):
        self._root = root
        self.user =user
        self._handle_login = handle_login
        self._handle_add = handle_add
        self._frame = None
        self._listbox = None
        self._stats_label = None
        self._image_label = None
        self._phone_ids = []
        
        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _add_handler(self, user):
        self._handle_add(user)

    def _back(self):
        self._handle_login(self.user)

    def update_list(self):
        self._listbox.delete(0, 'end')
        self. _phone_ids.clear()#lisäys

        headers = f"{'Image':<20}{'Series':<15}{'Model Year':<15}{'Price':<10}"
        self._listbox.insert(constants.END, headers)
        data = collecting_service.fetch_data() 
        
        for item in data:
        
            formatted_row = f"{item['id']}|{item['image']:<20}{item['series']:<15}{item['model_year']:<15}{item['price']:<10}"#{item['id']}|
            #self._listbox.insert(constants.END, headers)
            self._listbox.insert(constants.END, formatted_row)
            self._phone_ids.append(item["id"])
            self. _display_image(item['image'])
        

    def _delete_selected(self):
        selected_indices = self._listbox.curselection()
        if not selected_indices:
            messagebox.showerror("Virhe", "Valitse poistettava rivi.")
            return
        
        selected_index = selected_indices[0]
        if selected_index > 0 and selected_index <= len(self._phone_ids):
            phone_id = self._phone_ids[selected_index - 1] 
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this phone?"):
                collecting_service.delete_phone(phone_id)
                self.update_list()
        else:
            messagebox.showerror("Error", "Invalid selection")

    def _display_image(self, filepath):

        try: 
            image = Image.open(filepath) 
            self.photo_image = ImageTk.PhotoImage(image)  

        except FileNotFoundError:
            print("FileNotFound")


      


    def update_stats(self):
        stats = collecting_service.get_phone_stats()
        self._stats_label.config(text=f"Sinulla on {stats['total_phones']} puhelinta, joiden yhteisarvo on {stats['total_value']} euroa.")






    def initialize(self):
        self._frame = ttk.Frame(master=self._root)
   
        header_label = ttk.Label(self._frame, text="Projektien Yhteenveto")
        header_label.pack(fill=constants.X)

        self._stats_label = ttk.Label(self._frame, text="")
        self._stats_label.pack(fill=constants.X)

        self._listbox = Listbox(self._frame, height=10)
        self._listbox.pack(fill=constants.BOTH, expand=True)
        self.update_list()
        self.update_stats()

        #self._image_label = Label(self._frame) 
        #self._image_label.grid(row=0, column=2, sticky=constants.E)



        # Buttons
        add_button = ttk.Button(self._frame, text="Lisää Uusi Puhelin", command=lambda: self._add_handler(self.user))
        add_button.pack(fill=constants.X)

        delete_button = ttk.Button(self._frame, text="Poista Valittu", command=self._delete_selected)
        delete_button.pack(fill=constants.X)

        logout_button = ttk.Button(self._frame, text="User view",  command=self._back)#command=self._handle_login)
        logout_button.pack(fill=constants.X)

        self._frame.pack(fill=constants.BOTH, expand=True)
