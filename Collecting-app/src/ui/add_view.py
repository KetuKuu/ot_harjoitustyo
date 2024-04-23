from tkinter import ttk, constants, StringVar, filedialog, messagebox
from entities.user import User

class AddView:
    def __init__(self, root, handle_add_phone):
        self._root = root
        self._handle_add_phone = handle_add_phone
        #self._handle_update_project_status = handle_update_project_status
        #self._handle_back = handle_back
        self._frame = None
        self._fields = ['kuva', 'sarja', 'vuosimalli', 'hinta']
        self._entries = {}

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _add_phone(self):
        phone_data = {}
        for field in self._fields:
            phone_data[field] = self._entries[field].get()
        self._handle_add_phone(phone_data)
        self.clear_entries()

    def _clear_entries(self):
        for entry in self._entries.values():
            entry.delete(0, 'end')

    def _load_csv(self):
            filepath = filedialog.askopenfilename(
                title="Valitse CSV-tiedosto",
                filetypes=(("CSV-tiedostot", "*.csv"), ("Kaikki tiedostot", "*.*"))
            )
            if filepath:
                try:
                    with open(filepath, newline='', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            self._handle_update_project_status(row)
                    messagebox.showinfo("Lataus onnistui", "Tiedot on ladattu onnistuneesti.")
                except Exception as e:
                    messagebox.showerror("Virhe", "Tiedoston latauksessa tapahtui virhe:\n" + str(e))


    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for i, field in enumerate(self._fields):
            label = ttk.Label(master=self._frame, text=field.capitalize() + ':')
            label.grid(row=i, column=0, sticky=constants.W)
            entry = ttk.Entry(master=self._frame)
            entry.grid(row=i, column=1, sticky=(constants.W, constants.E))
            self._entries[field] = entry

        button_add = ttk.Button(master=self._frame, text='Lisää puhelin', command=self._add_phone)
        button_add.grid(row=len(self._fields), columnspan=2, pady=10)

        button_clear = ttk.Button(master=self._frame, text='Tyhjennä', command=self._clear_entries)
        button_clear.grid(row=len(self._fields) + 1, columnspan=2, pady=5)

        button_load_csv = ttk.Button(master=self._frame, text='Lataa CSV', command=self._load_csv)
        button_load_csv.grid(row=len(self._fields) + 2, columnspan=2, pady=5)

        
        self._frame.pack()

        """button_return = ttk.Button(
            master=self._frame,
            text="Palaa edelliseen valikkoon",
            command=self._handle_back  
        )
        button_return.grid(row=len(self._fields) + 2, columnspan=2, pady=5)

        self._frame.pack()"""