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