from tkinter import ttk, constants, StringVar, filedialog, messagebox, Label
from services.collecting_service import collecting_service
from entities.user import User
import csv


class AddView:
    def __init__(self, root, handle_add_phone, handle_project_view, handle_back, user):
        self._root = root
        self._handle_add_phone = handle_add_phone
        self._handle_project_view = handle_project_view
        self._handle_back = handle_back
        self.user = user
        self._frame = None
        self._fields = ['image', 'series', 'model_year', 'price']
        self._entries = {}

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _add_phone(self):
        phone_data = {
            'image': self._entries['image'].get(),
            'series': self._entries['series'].get(),
            'model_year': self._entries['model_year'].get(),
            'price': self._entries['price'].get()
        }
        collecting_service.add_phone(phone_data)
        self._clear_entries()
        self._handle_project_view(self.user)

    def _clear_entries(self):
        for entry in self._entries.values():
            entry.delete(0, 'end')

    def _select_image(self, entry_widget):
        filepath = filedialog.askopenfilename(
            title="Valitse kuva",
            filetypes=(("JPEG files", "*.jpg;*.jpeg"),
                       ("PNG files", "*.png"), ("All files", "*.*"))
        )
        print(filepath)

        if filepath:
            entry_widget.delete(0, constants.END)
            entry_widget.insert(0, filepath)

    def _back(self):
        self._handle_back(self.user)
        # siirry userview näkymään

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # load valokuva "image" kenttä:
        self._frame = ttk.Frame(master=self._root)
        for i, field in enumerate(self._fields):
            label = ttk.Label(master=self._frame,
                              text=field.capitalize() + ':')
            label.grid(row=i, column=0, sticky=constants.W)
            if field == 'image':
                entry = ttk.Entry(master=self._frame)
                entry.grid(row=i, column=1, sticky=(constants.W, constants.E))
                self._entries[field] = entry
                button = ttk.Button(master=self._frame, text='Valitse kuva',
                                    command=lambda e=entry: self._select_image(e))
                button.grid(row=i, column=2)
            else:
                entry = ttk.Entry(master=self._frame)
                entry.grid(row=i, column=1, sticky=(constants.W, constants.E))
                self._entries[field] = entry

        button_add = ttk.Button(
            master=self._frame, text='Lisää puhelin', command=self._add_phone)
        button_add.grid(row=len(self._fields), columnspan=2, pady=10)

        button_clear = ttk.Button(
            master=self._frame, text='Tyhjennä', command=self._clear_entries)
        button_clear.grid(row=len(self._fields) + 1, columnspan=2, pady=5)

        button_return = ttk.Button(
            master=self._frame, text="Siirry käyttäjä-näkymään", command=self._back)
        button_return.grid(row=len(self._fields) + 3, columnspan=2, pady=5)

        self._frame.pack()
