import tkinter as ttk
from user_view import UserView


class CreateUserView(ttk.Frame):
    def __init__(self, master, handle_create_user, handle_cancel):
        super().__init__(master)
        self.master = master
        self.handle_create_user = handle_create_user
        self.handle_cancel = handle_cancel

        self.create_widgets()
    
    def create_widgets(self):
        self.label_username = ttk.Label(self, text="Uusi käyttäjätunnus:")
        self.label_username.pack()

        self.entry_username = ttk.Entry(self)
        self.entry_username.pack()

        self.label_password = ttk.Label(self, text="Uusi salasana:")
        self.label_password.pack()

        self.entry_password = ttk.Entry(self, show="*")
        self.entry_password.pack()

        self.button_create_user = ttk.Button(self, text="Luo käyttäjä", command=self.create_user)
        self.button_create_user.pack()

        self.button_cancel = ttk.Button(self, text="Peruuta", command=self.handle_cancel)
        self.button_cancel.pack()

    def create_user(self):
        # Haetaan syötetyt käyttäjätunnus ja salasana
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Tarkistetaan, että käyttäjätunnus ja salasana ovat kelvollisia (voit lisätä oman tarkistuslogiikkasi tähän)
        if username and password:
            # Kutsutaan handle_create_user -funktiota ja välitetään sille luodut käyttäjätunnus ja salasana
            self.handle_create_user(username, password)
        else:
            # Jos käyttäjätunnus tai salasana puuttuu, näytetään virheviesti
            print("Syötä käyttäjätunnus ja salasana")

    #def pack(self):
        """"Näyttää näkymän."""
        #self._frame.pack()

    #def destroy(self):
        #self._frame.destroy()

        
def main():
    root = ttk.Tk()
    root.title("Käyttäjän luominen")
    root.geometry("300x200")

    def handle_create_user(username, password):
        print(f"Luodaan käyttäjä: {username}, salasana: {password}")
        create_user_view.destroy()  # Tuhotaan CreateUserView-näkymä
        user_view = UserView(root)
        user_view.pack()

    def handle_cancel():
        print("Käyttäjän luominen peruttu")

    create_user_view = CreateUserView(root, handle_create_user, handle_cancel)
    create_user_view.pack()

    root.mainloop()

if __name__ == "__main__":
    main()