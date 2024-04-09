import tkinter as ttk

class LoginView(ttk.Frame):
    def __init__(self, master, handle_login, handle_create_user_view):
        super().__init__(master)
        self.master = master
        self.handle_login = handle_login
        self.handle_create_user_view = handle_create_user_view

        self.create_widgets()
    
    def create_widgets(self):
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

    def login(self):
        # Tarkista tässä kirjautumistiedot ja siirry eteenpäin, jos kirjautuminen onnistuu
        self.handle_login()

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

    def handle_login():
        print("Kirjautuminen")

    def handle_create_user_view():
        print("Käyttäjän luominen")

    def handle_logout():
        print("Uloskirjautuminen")

    def handle_add_project():
        print("Projektin lisääminen")

    def handle_project_summary():
        print("Projektin tilanne")

    login_view = LoginView(root, handle_login, handle_create_user_view)
    login_view.pack()

    user_view = UserView(root, handle_logout, handle_add_project, handle_project_summary)

    root.mainloop()

if __name__ == "__main__":
    main()