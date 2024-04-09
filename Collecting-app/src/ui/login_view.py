import tkinter as ttk
#from create_user_view import CreateUserView


class LoginView(ttk.Frame):
    def __init__(self, master, handle_login, handle_create_user_view):
        super().__init__(master)
        self.master = master
        self.handle_login = handle_login
        self.handle_create_user_view = handle_create_user_view
        self._frame= None

        self.create_widgets()
    
    def create_widgets(self):
        self._frame = ttk.Frame(master=self.master)
        self.label_username = ttk.Label(self, text="Käyttäjätunnus:")
        self.label_username.pack()

        self.entry_username = ttk.Entry(self)
        self.entry_username.pack()

        self.label_password = ttk.Label(self, text="Salasana:")
        self.label_password.pack()

        self.entry_password = ttk.Entry(self, show="*")
        self.entry_password.pack()

        self.button_login = ttk.Button(self, text="Kirjaudu", command=self.login)
        self.button_login.pack()

        self.button_create_user = ttk.Button(self, text="Luo käyttäjä", command=self.handle_create_user_view)
        self.button_create_user.pack()
    
    #def pack(self):
        """"Näyttää näkymän."""
        #self._frame.pack()

    #def destroy(self):
        #self._frame.destroy()
    

    def login(self):
        # Tarkista tässä kirjautumistiedot ja siirry eteenpäin, jos kirjautuminen onnistuu
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Tarkistetaan, onko käyttäjätunnus ja salasana oikein (tässä vain esimerkkinä)
        if username == "kayttaja" and password == "salasana":
            # Kirjautuminen onnistui, kutsutaan handle_login -funktiota
            self.handle_login()
        else:
    
            print("Virheellinen käyttäjätunnus tai salasana")
        
        #self.handle_login()




def main():
    root = ttk.Tk()
    root.title("Käyttäjän kirjautuminen")
    root.geometry("300x200")
    currentview= None


    def handle_login():
        
        destroycurrentview()
        currentview = LoginView(root, handle_login, handle_create_user_view)
        currentview.pack()
        print("Kirjautuminen")

    def destroycurrentview():
        if currentview != None: 
            currentview.destroy()

    def handle_create_user_view():
        
        destroycurrentview()
        currentview = LoginView(root, handle_login, handle_create_user_view)
        currentview.pack()
        print("Käyttäjän luominen")

    login_view = LoginView(root, handle_login, handle_create_user_view)
    login_view.pack()

    root.mainloop()

if __name__ == "__main__":
    main()