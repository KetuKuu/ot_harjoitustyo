import tkinter as tk

class LoginView(tk.Frame):
    """Käyttäjän kirjautumisesta vastaava näkymä."""

    def __init__(self, master, show_todos_view_callback):
        """Luokan konstruktori. Luo uuden kirjautumisnäkymän.

        Args:
            master:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            show_todos_view_callback:
                Kutsuttava-arvo, jota kutsutaan kun käyttäjä kirjautuu sisään.
        """

        super().__init__(master)
        self.master = master
        self.show_todos_view_callback = show_todos_view_callback
        self.create_widgets()

    def create_widgets(self):
        self.label_username = tk.Label(self, text="Käyttäjätunnus:")
        self.label_username.pack()

        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        self.label_password = tk.Label(self, text="Salasana:")
        self.label_password.pack()

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(self, text="Kirjaudu", command=self.login)
        self.button_login.pack()

    def login(self):
        # Tarkista tässä kirjautumistiedot ja siirry eteenpäin, jos kirjautuminen onnistuu
        self.show_todos_view_callback()

def main():
    root = tk.Tk()
    root.title("Käyttäjän kirjautuminen")
    root.geometry("300x200")

    def show_todos_view():
        # Voit luoda täällä TodosView-näkymän ja näyttää sen

        # Tämä on tilapäinen esimerkki
        todos_view_label = tk.Label(root, text="TodosView")
        todos_view_label.pack()

    login_view = LoginView(root, show_todos_view)
    login_view.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
