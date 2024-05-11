from tkinter import ttk, constants, StringVar, Frame, Label, Button, Listbox, messagebox
from services.collecting_service import collecting_service
from PIL import Image, ImageTk


class ProjectView:
    def __init__(self, root, user, handle_login, handle_add):
        self._root = root
        self.user = user
        self._handle_login = handle_login
        self._handle_add = handle_add
        self._frame = None
        self._listbox = None
        self._stats_label = None
        self._phone_ids = []
        self.ret =False


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
        self._listbox.delete(0,'end')
        self._phone_ids.clear()

        headers = f"{'Image':<20}{'Series':<15}{'Model Year':<15}{'Price':<10}"
        self._listbox.insert(constants.END, headers)
        data = collecting_service.fetch_data()

        for item in data:
            # Create a frame for each item
            item_frame = ttk.Frame(self._listbox)
            item_frame.pack(fill=constants.X)

            # Load image
            try:
                image = Image.open(item['image'])
                image.thumbnail((50, 50))
                photo_image = ImageTk.PhotoImage(image)
                image_label = ttk.Label(item_frame, image=photo_image)
                image_label.image = photo_image
                image_label.pack(side=constants.LEFT, padx=5)
            except FileNotFoundError:
                print("FileNotFound")

            # Create label for text
            item_label_text = f"{item['series']:<15}{item['model_year']:<15}{item['price']:<10}"
            text_label = ttk.Label(item_frame, text=item_label_text)
            text_label.pack(side=constants.LEFT, padx=5)

            # ADDED
            delete_button = ttk.Button(
                item_frame, text="Delete", command=lambda id=item["id"]: self._delete_item(id))
            delete_button.pack(side=constants.RIGHT)

            self._phone_ids.append(item["id"])

    def _delete_item(self, phone_id):
        selected_index = self._phone_ids.index(phone_id)

        
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this phone?"):
            collecting_service.delete_phone(phone_id)
            self._listbox.delete(selected_index)
            item_frame = self._listbox.pack_slaves()[selected_index]
            item_frame.pack_forget()
            

    def update_stats(self):
        stats = collecting_service.get_phone_stats()
        self._stats_label.config(
            text=f"Sinulla on puhelimiä {stats['total_phones']}, ja olet maksanut yhteensä {stats['total_value']} euroa.")

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(self._frame, text="Project Summary")
        header_label.pack(fill=constants.X)

        item_label_text = f"{'Kuva':<15}{'Series':<15}{'Model Year':<15}{'Price':<15}"
        item_label = ttk.Label(self._frame, text=item_label_text)
        item_label.pack(fill=constants.X)

        self._stats_label = ttk.Label(self._frame, text="")
        self._stats_label.pack(fill=constants.X)

        self._listbox = Listbox(self._frame, height=10)
        self._listbox.pack(fill=constants.BOTH, expand=True)

        self.update_list()
        self.update_stats()

        # Buttons
        add_button = ttk.Button(
            self._frame, text="Lisä uusi puhelin", command=lambda: self._add_handler(self.user))
        add_button.pack(fill=constants.X)

        logout_button = ttk.Button(
            self._frame, text="Siirry käyttäjä-näkymään", command=self._back)
        logout_button.pack(fill=constants.X)


        """   ret_button = ttk.Button(
            self._frame, text="ret" self.ret = True, command=self._back, )
        ret_button.pack(fill=constants.X) """
        #kaksi komeno, 

        self._frame.pack(fill=constants.BOTH, expand=True)
