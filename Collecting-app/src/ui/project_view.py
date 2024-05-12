from tkinter import ttk, constants, StringVar, Frame, Label, Button, Listbox, messagebox
from services.collecting_service import collecting_service
from PIL import Image, ImageTk


class ProjectView:
    """Projektinäkymän lisäämisestä vastaava näkymä."""

    def __init__(self, root, user, handle_userview, handle_add):

        """Luokan konstruktori. Luo uuden projektinäkymän.

        Args:
            handle_userview: Funktio käyttäjänäkymään siirtymistä varten.
            handle_add: Funktio uuden puhelimen lisäämistä varten.
            user: Käyttäjäolio
        
            Attributes:    
                _listbox: Listbox elementti puhelintiedojen näyttämistä varten.
                _phone_ids: Lista puhelimien id:stä hakua varten
                _entries: Sanakirja, joka sisältää puhelimen tiedokenttiin liittyvät kentät.
        """

        self._root = root
        self.user = user
        self._handle_userview = handle_userview
        self._handle_add = handle_add
        self._frame = None
        self._listbox = None
        self._phone_ids = []
        self.ret =False


        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _add_handler(self, user):
        """Siirtymä kirjautuneen käyttäjän projektin lisäys näkymään"""
        self._handle_add(user)

    def _back(self):
        """Siirtymä käyttäjänäkymään"""
        self._handle_userview(self.user)


    def update_list(self):
        """Päivitettään pyhelimentiedot lista näkymään.
        
        Metodi päivittää näkymässä olevan puhelintiedojen listan.
        Metodi poistaa ensin kaikki nykyiset tiedot listasta ja luo uuden rivin kehyksineen jokaiselle käyttäjän lisämälle puhelimelle erikseen.
        Jokainen puhelin näytetään omassa kehyksessä8(for-loop), poiston mahdollistamista varten. 
        """
        self._listbox.delete(0,'end')
        self._phone_ids.clear()
        
        """Hakee tiedostot tiedokannasta ja lisää otsikon mukaiset tiedot listbox:iin."""
        headers = f"{'Image':<20}{'Series':<15}{'Model Year':<15}{'Price':<10}"
        self._listbox.insert(constants.END, headers)
        data = collecting_service.fetch_data()

        for item in data:
            """Luo kehyksen tulevalle listalle jossa jokaine puhelin on omalla rivillä"""
            item_frame = ttk.Frame(self._listbox)
            item_frame.pack(fill=constants.X)

            try:
                image = Image.open(item['image'])
                image.thumbnail((50, 50))
                photo_image = ImageTk.PhotoImage(image)
                image_label = ttk.Label(item_frame, image=photo_image)
                image_label.image = photo_image
                image_label.pack(side=constants.LEFT, padx=5)
            except FileNotFoundError:
                print("FileNotFound")
        
            
            item_label_text = f"{item['series']:<15}{item['model_year']:<15}{item['price']:<10}"
            text_label = ttk.Label(item_frame, text=item_label_text)
            text_label.pack(side=constants.LEFT, padx=5)

            """Lisäätän poista nappi. Nappi vastaa puhelimen poistamisesta puhelimien id listassa. """
            delete_button = ttk.Button(
                item_frame, text="Poista", command=lambda id=item["id"]: self._delete_item(id))
            delete_button.pack(side=constants.RIGHT)

            self._phone_ids.append(item["id"])

    def _delete_item(self, phone_id):
        """Poistetan puhelin puhelimen id:n perusteella.
        
        Metodi poista puhelimen käyttämällä tkinterin messageboxi. näkymä päivitetään, mikäli poisto ruoritetaan.
        """
        selected_index = self._phone_ids.index(phone_id)

        
        if messagebox.askyesno("Varmista poisto", "Haluatko varmasti poistaa tämän puhelimen?"):
            collecting_service.delete_phone(phone_id)
            self._listbox.delete(selected_index)
            item_frame = self._listbox.pack_slaves()[selected_index]
            item_frame.pack_forget()

 
    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(self._frame, text="Project Summary")
        header_label.pack(fill=constants.X)

        item_label_text = f"{'Kuva':<15}{'Series':<15}{'Model Year':<15}{'Price':<15}"
        item_label = ttk.Label(self._frame, text=item_label_text)
        item_label.pack(fill=constants.X)

        self._listbox = Listbox(self._frame, height=10)
        self._listbox.pack(fill=constants.BOTH, expand=True)

        self.update_list()

        """buttons"""
        add_button = ttk.Button(self._frame, text="Lisä uusi puhelin", command=lambda: self._add_handler(self.user))
        add_button.pack(fill=constants.X)

        logout_button = ttk.Button(self._frame, text="Siirry käyttäjä-näkymään", command=self._back)
        logout_button.pack(fill=constants.X)

        self._frame.pack(fill=constants.BOTH, expand=True)
