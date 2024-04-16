from tkinter import Tk
from ui.ui import UI
#from ui.create_user_view import CreateUserView




def main():
    window = Tk()
    window.title("Nokia")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()