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
            # Kirjautuminen epäonnistui, tulostetaan virheviesti
            print("Virheellinen käyttäjätunnus tai salasana")
        
        #self.handle_login()

class CreateUserView(ttk.Frame):
    def __init__(self, master, handle_login):
        super().__init__(master)
        self.master = master
        self.handle_login = handle_login

        self.create_widgets()

    def create_widgets(self):
        # Lisää tarvittavat elementit ja toiminnot käyttäjän luomiseksi
        pass

class UserView(ttk.Frame):
    def __init__(self, master, handle_logout, handle_add_project, handle_project_summary):
        super().__init__(master)
        self.master = master
        self.handle_logout = handle_logout
        self.handle_add_project = handle_add_project
        self.handle_project_summary = handle_project_summary

        self.create_widgets()

    def create_widgets(self):
        self.button_logout = ttk.Button(self, text="Kirjaudu ulos", command=self.handle_logout)
        self.button_logout.pack()

        self.button_add_project = ttk.Button(self, text="Lisää projekti", command=self.handle_add_project)
        self.button_add_project.pack()

        self.button_project_summary = ttk.Button(self, text="Projektin tilanne", command=self.handle_project_summary)
        self.button_project_summary.pack()




def main():
    root = ttk.Tk()
    root.title("Käyttäjän kirjautuminen")
    root.geometry("300x200")
    currentview= None
    
    #handle_login()

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
        currentview = CreateUserView(root, handle_login)
        currentview.pack()
        print("Käyttäjän luominen")

    login_view = LoginView(root, handle_login, handle_create_user_view)
    login_view.pack()

    root.mainloop()

if __name__ == "__main__":
    main()




import tkinter as ttk

class UserView(ttk.Frame):
    def __init__(self, master, handle_logout, handle_add_project, handle_project_summary):
        super().__init__(master)
        self.master = master
        self.handle_logout = handle_logout
        self.handle_add_project = handle_add_project
        self.handle_project_summary = handle_project_summary

        self.create_widgets()

    def create_widgets(self):
        self.button_logout = ttk.Button(self, text="Kirjaudu ulos", command=self.handle_logout)
        self.button_logout.pack()

        self.button_add_project = ttk.Button(self, text="Lisää projekti", command=self.handle_add_project)
        self.button_add_project.pack()

        self.button_project_summary = ttk.Button(self, text="Projektin tilanne", command=self.handle_project_summary)
        self.button_project_summary.pack()

        #self.button_summary = ttk.Button(self, text="Yhteenveto", command=self.handle_summary)
        #self.button_summary.pack()
        
def main():
    root = ttk.Tk()
    root.title("User View")
    root.geometry("400x300")

    def handle_logout():
        print("Kirjaudu ulos")

    def handle_add_project():
        print("Lisää projekti")

    def handle_project_summary():
        print("Projektitilanne")

    #def handle_summary():
        #print("Yhteenveto")

    user_view = UserView(root, handle_logout, handle_add_project, handle_project_summary)
    user_view.pack(expand=True, fill="both")
    root.mainloop()

if __name__ == "__main__":
    main()