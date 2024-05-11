from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database
from repositories.user_repository import user_repository
from repositories.collecting_repository import CollectingRepository


def main():

    initialize_database()
    window = Tk()
    window.title("Nokia")

    window.geometry("600x400")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
